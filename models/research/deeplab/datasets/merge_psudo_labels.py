import tensorflow as tf
from PIL import Image
from tqdm import tqdm
import numpy as np

import os

label_dir = './DD_full/SegmentationClass/'

psudo_label_dir = './DD_full/SegmentationClassSelf/'


if not os.path.isdir(psudo_label_dir):
	print("creating folder: ",psudo_label_dir)
	os.mkdir(psudo_label_dir)
else:
	print("Folder already exists. Delete the folder and re-run the code!!!")



if not os.path.isdir(label_dir):
	print("creating folder: ",label_dir)
	os.mkdir(label_dir)
else:
	print("Folder already exists. Delete the folder and re-run the code!!!")



label_files = os.listdir(label_dir)
psudo_label_file = os.listdir(psudo_label_dir)


for l_f in tqdm(psudo_label_file):
    arr = np.array(Image.open(psudo_label_file[l_f]))
    arr2d = arr[:,:,0]
    Image.fromarray(arr2d).save(label_dir , l_f)