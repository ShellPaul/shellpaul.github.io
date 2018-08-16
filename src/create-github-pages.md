创建 Github Pages
=================

我会告诉你我的目标就是添加个背景音乐吗？

<div align="left"> 
    <iframe frameborder="no" marginwidth="0" marginheight="0" width=400 height=140 src="https://music.163.com/outchain/player?type=2&id=490602750&auto=0&height=66"></iframe>
</div>

Step 1. 创建仓库
----------------
仓库名称必须是 <your-github-username>.github.io

Step 2. 添加 html
-----------------
可以尝试在仓库中创建 index.html，填入喜欢的内容提交  
应该等待 15 分钟就可以访问了 <your-github-username>.github.io

Step 3. Markdown
----------------
我们还是喜欢用 markdown，先安装 python 的 markdown 转 html 工具  
```
pip install markdown2
```
创建 src 目录，添加一个 markdown 文件  
创建 html 文件目录 dist  
运行
```
python -m markdown2 src/<your-markdown-file>.md > <your-html-file>.html
```

更多
----
[GitHub Pages Basics](https://help.github.com/categories/github-pages-basics/)