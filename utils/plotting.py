import requests
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as num


def set_theme():
    theme_url = "https://gist.githubusercontent.com/RishiSadhir/50b64465b5e8ce6448299da0032fe6c0/raw/6d2dc981b57119b2225def7176ed084c09f549a7/theme.py"
    resp = requests.get(theme_url)
    for l in resp.iter_lines():
        exec(l)


def build_dens(arr, x = None, bw=None, norm=False):
    positions = arr
    density = stats.gaussian_kde(positions)
    if x is None:
        x = np.linspace(min(positions), max(positions), len(arr))
    if bw:
        density.set_bandwidth(bw_method=bw)
    if norm:
        y = density(x)/density(x).sum(axis=0, keepdims=1)
    else:
        y = density(x)
    return y
