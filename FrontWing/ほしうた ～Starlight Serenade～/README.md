# ほしうた ～Starlight Serenade～ gpt-4o-2024-11-20翻译补丁 v1.0.1

MD5: `D7F2EA67A803B319DEAA75D11F33FA0B`

作者： natsumerinchan(Github) == 雨宮ゆうこ(2dfan)

未完整测试，有bug请反馈（截图加私发存档）

## 使用方法
- 解压压缩包并把所有文件复制到游戏根目录，安装字体"MSGothic_WenQuanYi_cnjp.ttf"后双击hoshiutaSS.exe运行(无需手动转区因为UniversalInjectorFramework会自动处理)

## 已知问题
- 由于个人水平有限，目前简体字与正常字距两者不可兼得，默认简体窄距，如需改为日繁正常字距则把GameData/System/config.txt_bak重命名为config.txt，<br>uif_config.json中`spoof_creation`的`enable`设为`false`。

# Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-3.5/GPT-4/Newbing/Sakura等大语言模型的Galgame自动化翻译解决方案
- [crskycode/GARbro](https://github.com/crskycode/GARbro) :Galgame解包和打包工具
- [amayra/arc_conv](https://github.com/amayra/arc_conv.git) :由 w8m 以纯 ASM 编写的命令行视觉小说工具包
- [AtomCrafty/UniversalInjectorFramework](https://github.com/AtomCrafty/UniversalInjectorFramework.git) :实现自动转区和更改字体(QLIE引擎要修改fontdata.dat使其调用系统字体)
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
.\arc_conv.exe --pack qlie .\data4 .\data4.pack
```
