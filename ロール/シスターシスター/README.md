# シスターシスター gpt-4o-2024-11-20翻译补丁 v1.0.0

MD5: `CF789DED9BC5F21D22A800F5BE2DF71A`

作者： natsumerinchan(Github) == 雨宮ゆうこ

未完整测试，有bug请反馈（截图加私发存档）

## 使用方法
- 解压压缩包并把所有文件复制到游戏根目录，安装字体"WenQuanYi_msgothic"后转区运行シスシス.exe

# Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-3.5/GPT-4/Newbing/Sakura等大语言模型的Galgame自动化翻译解决方案
- [nanami5270/GARbro-Mod](https://github.com/nanami5270/GARbro-Mod.git) :Galgame解包和打包工具
- [amayra/arc_conv](https://github.com/amayra/arc_conv.git) :由 w8m 以纯 ASM 编写的命令行视觉小说工具包
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本,并使用其jis替换字体

# SExtractor提取正则(TXT引擎)
```
00_skip=^\s*[@^\/\\]
01_search=^,(?P<name>.+?),\[spd,.+\](?P<msg>.+?)\[spd\]$
02_search=^,(?P<name>.+?),(?P<msg>.+?)$
03_search=^.+?,(?P<name>.+?),\[spd,.+\](?P<msg>.+?)\[spd\]$
04_search=^.+?,(?P<name>.+?),(?P<msg>.+?)$
05_search=^\[spd,.+\](.+?)\[spd\]$
06_search=^(.+?)$
structure=paragraph
```

# QLIE引擎arc_conv打包命令(需保持目录结构)
```
.\arc_conv.exe --pack qlie .\data4 .\data4.pack
```
