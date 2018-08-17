创建 Github Pages
=================

我会告诉你我的目标就是添加个背景音乐吗？

<audio controls autoplay preload="metadata" style=" width:300px;">
	<source src="http://other.web.ri01.sycdn.kuwo.cn/resource/n1/7/87/3851412328.mp3" type="audio/mpeg">
	Your browser does not support the audio element.
</audio>

Step 1. 创建仓库
----------------
Github Pages分两种，一种是User&Oganization，另一种是Project
如果是第1种，仓库名称必须是 ```<your-github-username>.github.io```，访问地址```<your-github-username>.github.io```(示例: [https://tianwei1992.github.io/](https://tianwei1992.github.io/) )
如果是第2种，仓库名称任意，访问地址```<your-github-username>.github.io/<your-repo-name>```(示例: [https://tianwei1992.github.io/notice/](https://tianwei1992.github.io/notice/) )

这个页面是第2种

Step 2. 添加 html
-----------------
可以尝试在仓库中创建 index.html，填入喜欢的内容

Step 3. 测试
------------
在项目文件夹下启动个简单的文件服务器用于测试

- python 3 ```python -m http.server```
- python 2 ```python -m SimpleHTTPServer```

访问 [http://127.0.0.1:8000](http://127.0.0.1:8000)

Step 4. 上线
------------
用 git 提交到仓库  
最多等 15 分钟就可以访问了 ```<your-github-username>.github.io```

Step 5. Markdown
----------------
我们还是喜欢用 markdown

先安装 python 的 markdown 转 html 工具  
```
pip install markdown jinja2
```
创建 src 目录，添加一个 markdown 文件  
src 下再创建一个 python 文件 gen_html.py  
```
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
    <link href="http://netdna.bootstrapcdn.com/twitter-bootstrap/2.3.0/css/bootstrap-combined.min.css" rel="stylesheet">
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
```

运行即可把 markdown 文件转换成 html

使用框架
-------
很多人已经开发好了框架等你来用  
[有哪些github pages开源项目可以用来建博客？](https://www.zhihu.com/question/21169368)  


更多
----
[GitHub Pages Basics](https://help.github.com/categories/github-pages-basics/)
