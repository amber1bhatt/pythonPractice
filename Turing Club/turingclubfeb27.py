# -*- coding: utf-8 -*-
"""turingClubFeb27.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FBQiIAoO7Rr5x8iY7fTw5ohvRJeCyn7A

# DeepLabCut

DeepLabCut is a powerful yet easy-to-use tool for tracking movement in just about any moving object, from a mouse's paws to a horse's legs to a human's facial muscles and everything in between! All you need to do is label some images of your desired animal or object moving, and DeepLabCut will do the rest. Of course, we'll also look at how DeepLabCut works as well!

The first step is to go to "Runtime" ->"change runtime type"->select "Python3", then click on "TPU" (more details below!)
"""

# We'll be using Tensor Processing Units (TPUs), which are specialized versions of graphics cards that are designed for high-performance
# machine learning. Google gives everyone a few TPUs to use in each Colab environment! But remember, with great power comes great responsibility :)

# Don't worry about the code below; we're just checking to make sure that we can access the TPUs!
#!nvcc --version

#let's make sure we see a TPU:
import os
import pprint
import tensorflow as tf

if 'COLAB_TPU_ADDR' not in os.environ:
  print('ERROR: Not connected to a TPU runtime; please see the first cell in this notebook for instructions!')
else:
  tpu_address = 'grpc://' + os.environ['COLAB_TPU_ADDR']
  print ('TPU address is', tpu_address)

  with tf.Session(tpu_address) as session:
    devices = session.list_devices()

  print('TPU devices:')
  pprint.pprint(devices)

"""# New Section

# New Section

Now, download the file we've linked on our github to your computer - this contains the project you'll be working with, including the images you'll be labelling! Run the next code block, click "Choose Files", and select the file you've just downloaded ("workshop_project-Turing-2019-02-22.zip")!
"""

from google.colab import files
uploaded = files.upload()

!unzip workshop_project-Turing-2019-02-27

# Using pip (the python package installer), we will install DeepLabCut! A lot of stuff is going to be printed out; just click the three dots to the right and select "Clear output".
!pip install deeplabcut

# Don't worry about the contents of this code!
# These are some Colab specific work-arounds, but they work! (typically not required, as they are installed with "pip install deeplabcut")

!pip install Pillow==4.0.0

from PIL import Image
def register_extension(id, extension): Image.EXTENSION[extension.lower()] = id.upper()
Image.register_extension = register_extension
def register_extensions(id, extensions):
  for extension in extensions: register_extension(id, extension)
Image.register_extensions = register_extensions

!pip install ruamel.yaml==0.15
!pip install pandas==0.21.0

# The non-Colab version of DeepLabCut lets you label the images for your model using a special interface. Sadly, Colab doesn't support this so we'll
# be labelling the images on our own computers (don't worry, this is very straightforward)! We just need to disable the special interface so that it
# doesn't cause problems.

import os
os.environ["DLClight"]="True"
os.environ["Colab"]="True"

# We can now import the deeplabcut package!
import deeplabcut

"""## Configuring your dataset"""

# Now it's time to tell Colab where our config file is! We will be editing this file later.
path_config_file = 'workshop_project-Turing-2019-02-27/config.yaml'

"""## Create a training dataset:
### You must do this step inside of Colab:
This function generates the training data information for DeepCut (which requires a mat file) based on the pandas dataframes that hold label information. The user can set the fraction of the training set size (from all labeled image in the hd5 file) in the config.yaml file. While creating the dataset, the user can create multiple shuffles.

After running this script the training dataset is created and saved in the project directory under the subdirectory **'training-datasets'**

This function also creates new subdirectories under **dlc-models** and appends the project config.yaml file with the correct path to the training and testing pose configuration file. These files hold the parameters for training the network. Such an example file is provided with the toolbox and named as **pose_cfg.yaml**.

Now it is the time to start training the network!
"""

deeplabcut.create_training_dataset(path_config_file)

"""## Start Training:
This function trains the network for a specific shuffle of the training dataset.
"""

# Shuffle is just a setting for whether or not you'll shuffle the data (just leave it as it is). displayiters lets you set how often
# DeepLabCut will print out data during the training (keeping it at 10 will keep you up to date with the analysis). saveiters lets
# you set how often the model will be saved. This is useful because it lets you restart from a checkpoint if you have to stop the training early.

deeplabcut.train_network(path_config_file, shuffle = 1)

"""When you stop this code it will show a "KeyError". Don't worry, this is supposed to happen :)

## Start Analyzing Videos:
Now, it's time to put the model we've just trained to the test! This function analyzes a new video for the movement you've just trained. The user can choose the best model from the evaluation results and specify the correct snapshot index for the variable **snapshotindex** in the **config.yaml** file. Otherwise, by default the most recent snapshot is used to analyse the video.

The results are stored in an hd5 file in the same directory where the video resides.
"""

videofile_path = ['workshop_project-Turing-2019-02-27/videos/MovieS2_Perturbation_noLaser_compressed.avi'] #Enter the list of videos to analyze.
deeplabcut.analyze_videos(path_config_file, videofile_path)

"""## Create labeled video:
Here, we'll overlay the predicted movement of the animal on the video we've created! This labelled video will be saved in the same directory where the original video resides.
"""

deeplabcut.create_labeled_video(path_config_file, videofile_path)

"""## Plot the trajectories of the analyzed videos:
Lastly, we'll plot the trajectories of the body part movement predicted by the model. Each body part is identified by a unique color.
"""

#for making interactive plots.
# %matplotlib notebook
deeplabcut.plot_trajectories(path_config_file, videofile_path)