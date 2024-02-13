import numpy as np
import os
from PIL import Image

def load_dataset(directory):
    images = []
    labels = []  # Assuming there's a label for each image
    for filename in os.listdir(directory):
        if filename.endswith('.png'):  # Adjust based on your data format
            img = Image.open(os.path.join(directory, filename))
            images.append(np.array(img))
            # Example to derive label from filename, adjust as necessary
            labels.append(filename.split('_')[0])  
    return np.array(images), np.array(labels)

def add_to_dataset(dataset, drawing, label):
    dataset['images'].append(drawing)
    dataset['labels'].append(label)
    # Consider saving updated dataset to disk
