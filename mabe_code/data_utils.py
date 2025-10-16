import os
import time
import random
import pandas as pd


pretrain_labs = [
    "MABe22_keypoints",
    "MABe22_movies",
]

calcrim = [
    "CalMS21_supplemental",
    "CalMS21_task1",
    "CalMS21_task2",
    "CRIM13"
]

not_in_test_labs = [
    "MABe22_keypoints",
    "MABe22_movies",
    "CalMS21_supplemental",
    "CalMS21_task1",
    "CalMS21_task2",
    "CRIM13"
]

def get_index(iterable):
    return random.randint(0, len(iterable) - 1)


def get_file_names(path):
    return sorted(os.listdir(path))


def get_paths(path):
    file_names = sorted(os.listdir(path))
    return [os.path.join(path, fn) for fn in file_names]


def get_parqt(path):
    return pd.read_parquet(path)


def get_col_names(keyword):
    cols_heads = ["mouse1", "mouse2", "mouse3", "mouse4"]
    return [c+keyword for c in cols_heads]


def sleep(t=4000):
    time.sleep(t)
    
