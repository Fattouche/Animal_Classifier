#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
modified version of https://github.com/RaghavPrabhu/Deep-Learning/blob/master/dogs_breed_classification/classify.py
'''

from __future__ import division
import tensorflow as tf
import sys
import os

# Disable tensorflow compilation warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

'''
Classify images from test folder and predict dog breeds along with score.
'''


def classify_image(image_path, data_type):
    label_lines = [line.rstrip() for line
                   in tf.gfile.GFile(data_type+"/trained_model/retrained_labels.txt")]

    # reads model from file
    with tf.gfile.FastGFile(data_type+"/trained_model/retrained_graph.pb", 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def, name='')

    total_files = 0
    correct_decisions = 0
    for directory in os.listdir(image_path):
        with tf.Session() as sess:
            for file in os.listdir(image_path+directory):
                # Read the image_data
                image_data = tf.gfile.FastGFile(
                    image_path+directory+'/'+file, 'rb').read()
                # Feed the image_data as input to the graph and get first prediction
                softmax_tensor = sess.graph.get_tensor_by_name(
                    'final_result:0')

                predictions = sess.run(softmax_tensor,
                                       {'DecodeJpeg/contents:0': image_data})

                # Get prediction
                human_string = label_lines[predictions[0].argmax()]

                if(human_string == directory):
                    correct_decisions += 1
                total_files += 1
    percentage_correct = (correct_decisions/total_files)*100
    print("total correct: {0}  total_files:{1}".format(
        correct_decisions, total_files))
    print("Total accuracy: {0}%".format(percentage_correct))
    f.close()


def main():
    if(len(sys.argv) > 1):
        data_type = sys.argv[1]
    else:
        data_type = "API"
    test_data_folder = '../../media/{0}/test/'.format(data_type)
    classify_image(test_data_folder, data_type)


if __name__ == '__main__':
    main()
