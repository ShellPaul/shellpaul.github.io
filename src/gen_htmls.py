# -*- coding: utf-8 -*-

import os
import traceback

import jinja2
import markdown

md_dir = os.path.dirname(os.path.realpath(__file__))
html_dir = os.path.dirname(md_dir)

TEMPLATE = r"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <link href="//netdna.bootstrapcdn.com/twitter-bootstrap/2.3.0/css/bootstrap-combined.min.css" rel="stylesheet">
    <style>
        body {
            font-family: sans-serif;
        }
        code, pre {
            font-family: monospace;
        }
        h1 code,
        h2 code,
        h3 code,
        h4 code,
        h5 code,
        h6 code {
            font-size: inherit;
        }
    </style>
</head>
<body>
<div class="container">
{{content}}
</div>
</body>
</html>
"""


def gen_one(filepath):
    try:
        with open(filepath, "rb") as f:
            md = f.read().decode("utf-8", "ignore")
        extensions = ['extra', 'smarty']
        html = markdown.markdown(md, extensions=extensions, output_format='html5')
        doc = jinja2.Template(TEMPLATE).render(content=html)
        return doc
    except:
        print(traceback.format_exc())


def gen_all():
    for filename in os.listdir(md_dir):
        if not filename.endswith(".md"):
            print("Unknown file type: %s" % filename)
            continue
        inpath = os.path.join(md_dir, filename)
        content = gen_one(inpath)
        if content:
            outpath = os.path.join(html_dir, filename[:-3] + ".html")
            with open(outpath, "wb") as f:
                f.write(content.encode("utf-8", "ignore"))


if __name__ == '__main__':
    gen_all()
