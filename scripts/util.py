import requests
import os
from bs4 import BeautifulSoup
import json


def download(path, url):
    r = requests.get(url, stream=True)
    with open(path, 'wb') as fd:
        print(path, end=' : ')
        for chunk in r.iter_content(1024*100):
            print("=", end='')
            fd.write(chunk)
        print(">", "compeleted")


def save(path, data, encode=False, is_json=False):
    f = None
    if encode:
        f = open(path, 'w', encoding='utf-8')
    else:
        f = open(path, 'w')
    if is_json:
        return f.write(json.dumps(data))
    else:
        return f.write(data)


def load(path, encode=False, is_json=False):
    f = None
    if encode:
        f = open(path, 'r', encoding='utf-8')
    else:
        f = open(path, 'r')
    if is_json:
        data = json.loads(f.read())
    else:
        data = f.read()
    f.close()
    return data


def getSrc(url, encode=False):
    while(True):
        request = requests.get(url)
        if(request.status_code == 200):
            if encode:
                request.encoding = "utf-8"
            return request.text


def getLinkes(src):
    soup = BeautifulSoup(src, features="html.parser")
    divs = soup.findAll("div", {"class": 'article-item-img'})
    links = []
    for div in divs:
        a = div.find("a")
        link = a.get('href')
        links.append(link)
    return links


def getDetails(src):
    soup = BeautifulSoup(src, features="html.parser")
    script = soup.find("script", {"type": "application/ld+json"})
    try:
        temp = json.loads(script.text, strict=False)
        recipe = {}
        keys = ['description', 'image', 'keywords', 'name', 'nutrition', 'prepTime', 'recipeCategory',
                'recipeCuisine', 'recipeIngredient', 'recipeInstructions', 'recipeYield', 'totalTime']
        for key, val in temp.items():
            if key in keys:
                recipe[key] = val
        return recipe
    except Exception as e:
        print(e)
        return None
