# 恋祭☆綺想カメリアノート -夢に忍ばず、斬り咲け乙女！- DeepSeek-R1 翻译补丁

MD5: `FA6678C4A956B0D21B6EF4AB305FFE79`

作者： natsumerinchan(Github) == 雨宮ゆうこ

还未推完，有bug请反馈（截图加发送存档）

## 
- 1.安装修正补丁v1.04
- 2.解压压缩包并把所有文件复制到游戏根目录下，然后双击运行CAMELLIA.exe
- 3.进入游戏后在`設定`-`フォント`中将字体改为WenQuanYi Micro Hei

# Credits

- [GalTransl/GalTransl](https://github.com/GalTransl/GalTransl.git) :支持GPT-4/Claude/Deepseek/Sakura等大语言模型的Galgame自动化翻译解决方案
- [nanami5270/GARbro-Mod](https://github.com/nanami5270/GARbro-Mod.git) :Galgame解包和打包工具(krkr2引擎)
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本

krkr2 *.ks SExtractor文本提取正则(仅适用于本游戏)
```
00_search=^\[name_set text\=\'(?P<name>.+?)\'\]$
01_skip=^[;*@/#\[]
02_skip=^(\sf\.|f\.|\sif|if|\s\[)
03_search=^(?P<unfinish>.+)\[r\]
04_search=f.sel[0-9] = '(?P<msg>.+)'"\]
05_search=^\s(.+)$
06_search=^(.+)\[p2\]
07_search=^(.+)$
structure=paragraph
```
