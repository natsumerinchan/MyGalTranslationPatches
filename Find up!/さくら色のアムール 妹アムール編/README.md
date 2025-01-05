# さくら色のアムール 妹アムール編 DeepSeek-V3 翻译补丁 v1.0.0

MD5: `781F675A71DF286B839C2D512F90D49C`

作者： natsumerinchan(Github) == 雨宮ゆうこ

未作完整测试，有bug请反馈（截图加私发存档）。

## 使用方法
- 1.重命名`script.iga`如`script.iga.bak`
- 2.解压压缩包并把所有文件复制到游戏根目录，双击运行さくら色のアムール.exe

# Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-3.5/GPT-4/Newbing/Sakura等大语言模型的Galgame自动化翻译解决方案
- [amayra/arc_conv](https://github.com/amayra/arc_conv.git) :由 w8m 使用纯 ASM 编写的命令行视觉小说工具包
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [Inori/FuckGalEngine](https://github.com/Inori/FuckGalEngine.git) :galgame破解工具集，使用其中InnocentGrey引擎的getstring工具(脚本处理)
- [jyxjyx1234/misc_game-chs](https://github.com/jyxjyx1234/misc_game-chs/tree/re_upload/工具) :使用了士佬的FONTCHANGER和DLL代理

### SExtractor getstring.exe文本处理正则(TXT引擎+932编码+JIS替换)
```
04_search=^＃(?P<name>.+?)$
05_search=^(?P<msg>.+?)$
structure=paragraph
```

### arc_conv .iga(iga0) 解包命令
```
arc_conv --unpack iga0 .\script.iga
```