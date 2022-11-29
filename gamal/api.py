import os
import random
import base64
from glob import glob


TRANSLATIONS = {
    'english': 'camel',
    'dutch': 'kameel',
    'french': 'chameau',
    'german': 'Kamel',
    'italian': 'cammello',
    'portuguese': 'camelo',
    'spanish': 'camello',
    'swedish': 'kamelfår',
    'turkish': 'güvercin',
    'arabic': 'جمل',
    'hebrew': 'גמל',
    'japanese': 'ヤギ',
    'chinese': '骆驼',
    'russian': 'верблюд',
    'korean': '낙타',
    'thai': 'ม้าน้ำ',
    'vietnamese': 'con lạc đà',
    'indonesian': 'kuda'
}

def random_camel_base64():
    images_path = os.path.join(os.path.dirname(__file__), "images")
    names = [filename.split("/")[-1] for filename in glob(f'{images_path}/*.jpg')]
    name = random.choice(names)
    url = None
    with open(f'{images_path}/metadata.txt', 'r') as f:
        for line in f:
            if name in line:
                url = line.split(" ")[1].strip()
                break
    assert url
    with open(os.path.join(images_path, name), "rb") as f:
        return {
            'name': name.replace('.jpg', ''),
            'url': url,
            'b64': base64.encodebytes(f.read())
        }


def random_camel_html():
    camel = random_camel_base64()
    return f"""
    <html>
        <head>
            <title>גמל</title>
        </head>
        <body style="margin:0;direction: rtl;">
            <h1 style="position: relative; top: 170px; margin-top: -170px; text-align: center;font-size:80px;">גמל</h1>
            <img style="width: 100%" src="data:image/jpg;base64,{camel['b64'].decode('utf-8')}" />
            <h3 style="text-align: left;">{camel['name']}</h3>
            <p style="text-align: left;"><a href="{camel['url']}">Source</a></p>
        </body>
    </html>
    """

def translate(language = None):
    return {
        'translation': TRANSLATIONS.get(language),
        'languages': list(TRANSLATIONS.keys()),
    }
