1. 加载虚拟环境`source ./env/bin/active`

2. 分割`python slice.py`

3. 生成markdown文件`python load.py`

4. 生成`md/description.json` `python ./generateDescription.py`

5. 组合markdonw成ebook 

```
python ./mark2epub.py ./epub_md test.epub
```
