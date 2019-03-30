Final Report README
Contributors: 
Tyler Hu (qhu27): Implemented the data augmentation, and helped build the model on top of the frozen layers
Tarun Salh (tsalh): Implemented the blocks to read in our data, and helped build the model on top of the frozen layers
Prabhmeet Gill (psgill): Implemented the VGG16 model, and helped build the model on top of the frozen layers


Included Files:
Flower-Recognition-custom.ipynb - Our custom model notebook, which uses the the first two convolutional layers of VGG16 and builds our custom neural network on top of it. 


Flower-Recognition-VGG16.ipynb - The model to run base VGG16 on our dataset


Link to dataset: https://www.kaggle.com/alxmamaev/flowers-recognition/kernels


Instructions for each Notebook:
1. Create a new Kaggle kernel and import our model to the kernel.
2. Then on the right-hand side look up the dataset ("Flowers Recognition") in
Kaggle listed above.
3. Then run all and you should be able to reproduce our result. Our model runs for 20 epochs and it takes about 20-25 minutes to run fully.
4. Do this for both files individually to reproduce the results of each model.
5. However, make sure to not re run the kernel after completing it fully, we kept on encountering a bug where the model never learns, such that the test 
accuracies and loss were flat and never changed.