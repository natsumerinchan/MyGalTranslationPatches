# 妖精さんといっしょ～遠い空の下で～ kimi-k2 翻译补丁

MD5: `0178E47A4D837767821CA28A5FCC7389`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 使用方法
- 1.解压压缩包并把所有文件复制到游戏根目录下，然后双击运行yousei.exe
- 2.进入游戏后在`文字表示`-`字体`中将字体改为WenQuanYi Micro Hei

# Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-3.5/GPT-4/Newbing/Sakura等大语言模型的Galgame自动化翻译解决方案
- [nanami5270/GARbro-Mod](https://github.com/nanami5270/GARbro-Mod.git) :Galgame解包和打包工具(krkr2引擎)
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [krkr字体选择时如何支持中文字体](https://zhuanlan.zhihu.com/p/21775023)

## krkr2 *.ks SExtractor文本提取正则(仅适用于本游戏)
(TXT引擎+UTF-16编码+不生成JIS替换配置)
```
00_search=^[^;]*char\='(?P<name>.+?)'
04_search=^[^;]*(「.+?」)
05_search=^\s+(.+)\[w\]$
06_search=^\s+(.+)$
07_search=^(.+)\[w\]$
08_search=^(.+)$
postSkip=^[;.@*\{\}\[\]\tA-Za-z0-9\/\\■]
structure=paragraph
```

## json二次提取正则
(JSON引擎+UTF-8编码+不生成JIS替换配置)
```
10_search=(?P<unfinish>[^@a-zA-Z0-9－_/\r\n\[\]\= 「」]+)
```
