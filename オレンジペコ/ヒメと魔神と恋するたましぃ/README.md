# ヒメと魔神と恋するたましぃ claude-3-7-sonnet 翻译补丁

MD5: `54FD4D5B0EA4A1F2CA77B0C2B68483AD`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 使用方法
- 1.本补丁已集成修正补丁1.01，无需另外下载
- 2.解压压缩包并把所有文件复制到游戏根目录下，双击运行ヒメタマ.exe
- 3.建议在文字表示-字体中把字体修改为WenQuanYi Micro Hei，否则字形显示会不统一

# Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-3.5/GPT-4/Newbing/Sakura等大语言模型的Galgame自动化翻译解决方案
- [XP3Viewer](https://github.com/Inori/FuckGalEngine/blob/master/Krkr/XP3Viewer.rar) :可用于解包或封包被加密以及exe被保护的krkr2引擎游戏
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本

## 本作 krkr2 *.ks SExtractor文本提取正则
(TXT引擎+UTF-16+不生成jis配置)
```
00_search=^@talk.+?name=(?P<name>.+?)$
05_skip=^@hitret$
10_search=text\=\"(?P<message>.+?)\"
15_search=^(?P<unfinish>.+?)$
postSkip=^[\s@*;]
structure=paragraph
```

## json二次提取正则
(JSON引擎+UTF-8+不生成jis配置)
```
10_search=(?P<unfinish>[^\x00-\x1a\[\]\{\}.･\_#\s=\"\'%<>\(\)@a-zA-Z0-9－/\r\n,-]+)
```
