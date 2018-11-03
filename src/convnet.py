from tensorflow.keras import layers
from tensorflow.keras import Model
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.preprocessing.image import ImageDataGenerator

BATCH_SIZE = 20


# Returns a trained model
# Parameters:
#   train_dir:              directory containing the training data
#   validation_dir:         directory containing the test data
#   total_training_images:  the total number of training images
#   total_test_images:      the total number of test images
#   
def convnet(train_dir, validation_dir, total_training_images, total_test_images):
    # Model Generation
    # Define input shape to be 150x150 pixels, each with an R, G, B value
    img_input = layers.Input(shape=(150, 150, 3))

    # Create 3 convolutional layers
    x = layers.Conv2D(16, 3, activation='relu')(img_input)
    x = layers.MaxPooling2D(2)(x)

    x = layers.Conv2D(32, 3, activation='relu')(x)
    x = layers.MaxPooling2D(2)(x)

    x = layers.Conv2D(64, 3, activation='relu')(x)
    x = layers.MaxPooling2D(2)(x)

    # Flatten all the convolutional layers into one dimension
    x = layers.Flatten()(x)

    x = layers.Dense(512, activation='relu')(x)

    # Create output layer (might need an activation function? tbd)
    output = layers.Dense(1)(x)

    # Create model
    model = Model(img_input, output)

    # Specify RMSprop optimizer
    model.compile(loss='categorical_crossentropy', optimizer=RMSprop(lr=0.001), metrics=['acc'])

    # Image preprocessing
    train_datagen = ImageDataGenerator(rescale=1./255)
    test_datagen = ImageDataGenerator(rescale=1./255)

    train_generator = train_datagen.flow_from_directory(
        train_dir,
        target_size=(150, 150), 
        batch_size=BATCH_SIZE,
        class_mode='categorical'
    )

    validation_generator = test_datagen.flow_from_directory(
        validation_dir, 
        target_size=(150, 150), 
        batch_size=BATCH_SIZE,
        class_mode='categorical'
    )

    # Train model
    history = model.fit_generator(
        train_generator,
        steps_per_epoch=(total_training_images/BATCH_SIZE),
        epochs=15,
        validation_data=validation_generator,
        validation_steps=(total_test_images/BATCH_SIZE),
        verbose=2
    )

    return history


# Graphs the accuracy of a trained model
# Parameters:
#       history:    A trained model
#
def results(history):
    # Retrieve a list of accuracy results on training and test data
    # sets for each training epoch
    acc = history.history['acc']
    val_acc = history.history['val_acc']

    # Retrieve a list of list results on training and test data
    # sets for each training epoch
    loss = history.history['loss']
    val_loss = history.history['val_loss']

    # Get number of epochs
    epochs = range(len(acc))

    # Plot training and validation accuracy per epoch
    plt.plot(epochs, acc)
    plt.plot(epochs, val_acc)
    plt.title('Training and validation accuracy')

    plt.figure()

    # Plot training and validation loss per epoch
    plt.plot(epochs, loss)
    plt.plot(epochs, val_loss)
    plt.title('Training and validation loss')


if __name__ == '__main__':
    pass