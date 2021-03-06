import os
import sys
sys.path.append(os.getcwd())
from fastai.vision import *
from fastai.callbacks.hooks import *
from pathlib import PosixPath

import numpy as np
from libs.config import LABELS

def load_dataset(dataset, training_chip_size, bs):
    """ Load a dataset, create batches and augmentation """
    import pathlib
    temp = pathlib.PosixPath
    pathlib.PosixPath = pathlib.WindowsPath

    #path = PosixPath(dataset)
    path = pathlib.PosixPath(dataset)
    label_path = path/'label-chips'
    image_path = path/'image-chips'
    image_files = get_image_files(image_path)
    label_files = get_image_files(label_path)
    get_y_fn = lambda x: label_path/f'{x.stem}{x.suffix}'
    codes = np.array(LABELS)
    src = SegmentationItemList.from_folder(image_path).split_by_fname_file('../valid.txt').label_from_func(get_y_fn, classes=codes)
    # some data augmentation here
    #data = src.transform(get_transforms(flip_vert=True, max_warp=0., max_zoom=0., max_rotate=180.), size=training_chip_size, tfm_y=True).databunch(bs=bs)
    data = (src.transform(get_transforms(flip_vert=True, max_lighting=0.1, max_zoom=1.15, max_warp=0., max_rotate=180.), size=training_chip_size, tfm_y=True)
        .databunch(bs=bs)
        .normalize(imagenet_stats))
    return data
