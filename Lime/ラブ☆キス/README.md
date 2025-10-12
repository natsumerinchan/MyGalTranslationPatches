# ラブ☆キス claude-3-5-sonnet-20240620 翻译补丁 

MD5: `766F751E2785EE43842765094E9A72EE`

作者： natsumerinchan(Github) == 雨宮ゆうこ(2dfan)

已根据攻略ctrl了所有路线，未出现闪退，有其它bug请反馈（截图加私发存档）

## 使用方法
- 解压压缩包并把所有文件复制到游戏根目录，双击LoveKiss.exe运行(无需手动转区因为UniversalInjectorFramework会自动处理)

# Credits

- [GalTransl/GalTransl](https://github.com/GalTransl/GalTransl.git) :支持GPT-4/Claude/Deepseek/Sakura等大语言模型的Galgame自动化翻译解决方案
- [nanami5270/GARbro-Mod](https://github.com/nanami5270/GARbro-Mod.git) :Galgame解包和打包工具
- [amayra/arc_conv](https://github.com/amayra/arc_conv.git) :由 w8m 以纯 ASM 编写的命令行视觉小说工具包
- [AtomCrafty/UniversalInjectorFramework](https://github.com/AtomCrafty/UniversalInjectorFramework.git) :实现自动转区和更改字体
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本,并使用其jis替换字体
- [xupefei/Locale-Emulator](https://github.com/xupefei/Locale-Emulator.git) :转区软件,使用了其中的dll

# SExtractor提取正则(TXT引擎)
```
00_skip=^[@^\\]
01_search=^.+?,(?P<name>.+?),(?P<msg>.+?)$
02_search=^(.+?)$
sample=
鳩が豆鉄砲を食ったような顔での沈黙。
a_01_SAY011,小百合,「待ちなさい。別に、くだらないとは――」
```

# QLIE引擎arc_conv打包命令(需保持目录结构)
```
.\arc_conv.exe --pack qlie .\data8 .\data8.pack
```
