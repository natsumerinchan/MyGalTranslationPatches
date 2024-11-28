# ほしうた gpt-4o-2024-11-20翻译补丁 v1.0.1

MD5: `42DCB07AD4F89DCD04726B0812C61DB8`

作者： natsumerinchan(Github) == 雨宮ゆうこ(2dfan)

未完整测试，有bug请反馈（截图加私发存档）

## 使用方法
- 解压压缩包并把所有文件复制到游戏根目录，安装字体"MSGothic_WenQuanYi_cnjp.ttf"后双击hoshiuta.exe运行(无需手动转区因为UniversalInjectorFramework会自动处理)
- 若游戏中字间距过窄可自行在uif_config.json修改`override_height`和`override_width`找到最合适的配置

# Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-3.5/GPT-4/Newbing/Sakura等大语言模型的Galgame自动化翻译解决方案
- [crskycode/GARbro](https://github.com/crskycode/GARbro) :Galgame解包和打包工具
- [amayra/arc_conv](https://github.com/amayra/arc_conv.git) :由 w8m 以纯 ASM 编写的命令行视觉小说工具包
- [satan53x/UniversalInjectorFramework](https://github.com/satan53x/UniversalInjectorFramework.git) :satan53x佬改版，实现自动转区和调整字距(QLIE引擎要修改fontdata.dat使其调用系统字体)
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本,并使用其jis替换字体
- [xupefei/Locale-Emulator](https://github.com/xupefei/Locale-Emulator.git) :转区软件,使用了其中的dll

# SExtractor提取正则(TXT引擎)
```
00_skip=^\s*[@^\/\\]
01_search=^,(?P<name>.+?),(?P<msg>.+?)$
02_search=^.+?,(?P<name>.+?),(?P<msg>.+?)$
03_search=^(.+?)$
sample=
,【和彦】,「……ふぁ」
足と手に力を入れ、大きく伸びをすると、徐々に目が冴えてくる。
com01_nan0002,【ななの】,「へいき……だもん……」
```

# QLIE引擎arc_conv打包命令(需保持目录结构)
```
.\arc_conv.exe --pack qlie .\data3 .\data3.pack
```
