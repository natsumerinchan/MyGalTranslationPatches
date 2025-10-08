# 受精してよ千鶴さん！ ～人妻と恋するひと夏～ gemini-2.5-pro 翻译补丁

MD5: `61E682F1F4779F3F9EF64D7853F7EA41`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 使用方法
- 1.将压缩包内所有文件解压至游戏根目录，双击运行LBL-30040_CHS.eXe

# Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-3.5/GPT-4/Newbing/Sakura等大语言模型的Galgame自动化翻译解决方案
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [nanami5270/GARbro-Mod](https://github.com/nanami5270/GARbro-Mod.git) :Galgame解包和打包工具
- [arcusmaximus/KirikiriTools](https://github.com/arcusmaximus/KirikiriTools.git) :Xp3Pack.exe 打包xp3

## krkr *.ks SExtractor提取正则(仅适用于本作)
(TXT引擎+UTF-16编码+不进行JIS替换)
```
00_search=^\[NAME_M\s+n\=\"(?P<name>.+?)\"\]
05_search=^\[NAME_W\s+n\=\"(?P<name>.+?)\"\]
10_search=^\s+(?P<end_unfinish>.+?)\[T_NEXT
15_search=^(?P<end_unfinish>.+?)\[T_NEXT
20_search=^\s+(?P<start_unfinish>.+?)$
25_search=^(?P<start_unfinish>.+?)$
postSkip=^[A-Za-z0-9\;\*\[\]]
structure=paragraph
```
