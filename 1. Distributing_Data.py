import numpy as np
import os
# Get the list of pneumonia and normal images in validation set
val_pneumonia_path = 'chest_xray/val/PNEUMONIA/'
val_normal_path = 'chest_xray/val/NORMAL/'
val_pneumonia_images = os.listdir(val_pneumonia_path)
val_normal_images = os.listdir(val_normal_path)

# Get the list of pneumonia and normal images in test set
test_pneumonia_path = 'chest_xray/test/PNEUMONIA/'
test_normal_path = 'chest_xray/test/NORMAL/'
test_pneumonia_images = os.listdir(test_pneumonia_path)
test_normal_images = os.listdir(test_normal_path)

# Check if the number of pneumonia images in test and validation sets are equal
if len(test_pneumonia_images) != len(val_pneumonia_images):
  # Select random images from the test set and move them to the validation set
  num_images_to_move = abs(len(test_pneumonia_images) - len(val_pneumonia_images))//2
  random_images = np.random.choice(test_pneumonia_images, num_images_to_move, replace=False)
  for image in random_images:
    os.rename(os.path.join(test_pneumonia_path, image), os.path.join(val_pneumonia_path, image))

# Check if the number of normal images in test and validation sets are equal
if len(test_normal_images) != len(val_normal_images):
  # Select random images from the test set and move them to the validation set
  num_images_to_move = abs(len(test_normal_images) - len(val_normal_images))//2
  random_images = np.random.choice(test_normal_images, num_images_to_move, replace=False)
  for image in random_images:
    os.rename(os.path.join(test_normal_path, image), os.path.join(val_normal_path, image))