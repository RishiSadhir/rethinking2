import requests
import matplotlib.pyplot as plt


def set_theme():
    theme_url = "https://gist.githubusercontent.com/RishiSadhir/50b64465b5e8ce6448299da0032fe6c0/raw/6d2dc981b57119b2225def7176ed084c09f549a7/theme.py"
    resp = requests.get(theme_url)
    for l in resp.iter_lines():
        exec(l)
