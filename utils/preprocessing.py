import numpy as np


def center(v):
    return v - np.mean(v)


def scale(v):
    return v / np.std(v)


def standardize(v):
    return scale(center(v))


def unstandardize(v_new, v_old):
    return (v_new * np.std(v_old)) + np.mean(v_old)
