# オトメクライシス gemini-2.5-pro 翻译补丁

MD5: `EB78E128FC12BA02562C5C72A30E89B3`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 使用方法
- 1、解压压缩包并把所有文件复制到游戏根目录，双击运行`Otome_CHS.exe`

# Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-4/Claude/Deepseek/Sakura等大语言模型的Galgame自动化翻译解决方案
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [GalTools/GalArc](https://github.com/GalTools/GalArc.git) :Galgame解包和打包工具(NEXAS版本2，压缩方式none)
- [【工具】API HOOK和编码处理工具包](https://www.ai2.moe/topic/29225-【工具】api-hook和编码处理工具包)
- [xupefei/Locale-Emulator](https://github.com/xupefei/Locale-Emulator.git) :转区工具,使用了其中的dll
- [Duel Savior Justice Dev Kit](http://tenka.seiha.org/images2019/dsj/DuelSavior_SDK.rar) :英翻补丁作者[Tenka Seiha](https://tenka.seiha.org/)提供的翻译工具包，里面有NEXAS引擎脚本的反编译和重编译工具dstool.exe
- [FunkyFr3sh/cnc-ddraw](https://github.com/FunkyFr3sh/cnc-ddraw.git) :GDI, OpenGL and Direct3D 9 re-implementation of the DirectDraw API for classic 2D games for better compatibility with Windows ME, 2000, XP, Vista, 7, 8, 10, 11, Wine (Linux/macOS/Android) and Virtual Machines

# SExtractor提取正则
1、初步提取
(TXT引擎+cp932编码+不开启JIS替换配置)
```
00_skip=^PushB\s+<[A-Z]{1}[0-9]{0,1}_.+?>$
05_skip=^PushB\s+<.+?_.+?>$
06_skip=^PushB\s+<\d+>$
07_skip=^PushB\s+<\w{3,4}\d+>$
08_skip=^PushB\s+<.+?\d{2}[0-9\-]{0,3}[0-9～]{0,3}>$
09_skip=^PushB\s+<.+?\.(bin|mpg)>$
10_search=^PushB\s+<(?P<pre_nameANDmessage>@[@a-z0-9\s]+[（「]{1}+.+?)>$
15_search=^PushB\s+<(?P<pre_nameANDmessage>「.+?)>$
20_search=^PushB\s+<(.+?)>$
JisEncodeName=shift-jis
structure=paragraph
```

2、二次提取
(JSON引擎+UTF-8编码+开启JIS替换配置)
```
10_search=(?P<unfinish>[^@a-zA-Z0-9－/\r\n　_]+)
```
