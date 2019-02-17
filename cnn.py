
import keras
from keras.models import Sequential
from keras.layers import Activation
from keras.layers.core import Dense, Flatten
from keras.layers.normalization import BatchNormalization
from keras.layers.convolutional import *
from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import Adam
from keras.metrics import categorical_crossentropy


# Data directory paths
TEST__PATH="test"
TRAIN_PATH="train"

# Image Size on data
IMG_SIZE= ( 320, 240 )

# Number of Labels
NUM_LABELs = 5

# Function returns a batch of data ( data specified by data_path ),
# and batch the size of the minibatch is given by size
def get_data_batches( data_path, size):
    return ImageDataGenerator().flow_from_directory(data_path,
                                                     target_size=IMG_SIZE,
                                                     batch_size=size)

###############################################################################
## Program Entry Point ########################################################
###############################################################################
if __name__ == '__main__':

    # Get a batch of training data of size 20
    train_batch = get_data_batches( TRAIN_PATH, 50)

    # Image data ( height of 320, length of 240, image channel 3 for RGB )
    shape = ( 320, 240, 3 )
    model = Sequential(
                # Convolution layer with (3,3) filter and relu activation
                [Conv2D(32, (3,3), activation="relu", input_shape=shape),
                 # Flatten layer flatten image to features after convolution
                 Flatten(),
                 # Dense layer
                 Dense( NUM_LABELs, activation='softmax')])
    # CNN with a learning rate of .005
    model.compile( Adam(lr=.05), loss='categorical_crossentropy',
                   metrics=['accuracy'])
    # Train the model
    # WARNING: Running this function may cause an allocation exceeding memory
    model.fit_generator( train_batch, steps_per_epoch=3,epochs=10 )

    # Test the model
    test_batch = get_data_batches(TEST__PATH, 200)
    predictions = model.predict_generator( test_batch, steps=1, verbose=0)