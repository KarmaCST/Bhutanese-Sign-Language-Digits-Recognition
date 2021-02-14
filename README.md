# Bhutanese-Sign-Language-Digits-Recognition

# 1. Introduction
Bhutanese Sign Language (BSL) is language used by the Deaf in Bhutan. BSL, like any other sign languages, is used for communication by using movement of hands, head, and expression. The Research Team in Wangsel Institute for the Deaf is standardizing and documenting BSL. BSL Digits and alphabets are officially documented and published. The deaf school urges people to learn BSL but learning Sign Language (SL) is difficult. This study presents the BSL digits recognition system using the Convolutional Neural Network (CNN). In addition, first-ever BSL dataset was curated with 20,000 sign images of 10 static digits collected from different volunteers. Different SL models were also evaluated and compared with the CNN model. The proposed CNN system has achieved 97.62% training accuracy. The system was also evaluated with precision, recall, and F1-score.

# 2. Dataset
There are 10 digits in BSL. Videos were recorded from different actors and then frames were extracted. In the data pre-processing, these frames were augmented using different augmentation techniques such as morphological transformation, saturation, addition and subtraction of colours, etc. The BSL digits dataset consisted of 20K (2000/class) images of varying resolutions. However, these images are further rescaled to 64x64x3 pixels at the time of training the model to reduce the training time but still it takes more time to train the model.

Therefore, images are serialized using pickling. The pickling reduces the training time almost by half.

# 3. Model Training
Google Colab was used for training the model. The Colab provides 12 hours of free usage of GPU 1xTesla K80 with 2496 cores for the 12 GB GDDR5 and CPU 1xsingle core Xeon Processors @ 2.5 GHz with 45 MB cache. The model was save and deployed using local system (laptop).
