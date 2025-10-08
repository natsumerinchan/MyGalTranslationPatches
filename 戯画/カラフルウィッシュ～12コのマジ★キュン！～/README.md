# カラフルウィッシュ～12コのマジ★キュン！～ gpt-4o-2024-11-20 翻译补丁

MD5: `62F99967C679EA13806ECDCFACD15792`

作者： natsumerinchan(Github) == 雨宮ゆうこ

已按照攻略全线ctrl。有bug请反馈（截图加私发存档）

## 使用方法
- 1、应用`12コの激萌えハーレムディスク`补丁以及免DVD补丁
- 2、解压压缩包并把所有文件复制到游戏根目录，双击运行ColorfulWish.exe

# Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-4/Claude/Deepseek/Sakura等大语言模型的Galgame自动化翻译解决方案
- [nanami5270/GARbro-Mod](https://github.com/nanami5270/GARbro-Mod.git) :Galgame解包和打包工具
- [ginyoushijin/GIGA_NeXAS](https://github.com/ginyoushijin/GIGA_NeXAS.git) :戏画引擎解封包 (仅用于无压缩封包，旧版nexas用它解包出来十六进制全是00，需配合转区工具使用，否则文件名会乱码)
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [AtomCrafty/UniversalInjectorFramework](https://github.com/AtomCrafty/UniversalInjectorFramework.git) :实现自动转区和更改字体，jis映射
- [xupefei/Locale-Emulator](https://github.com/xupefei/Locale-Emulator.git) :转区工具,使用了其中的dll

# SExtractor提取正则
1、初步提取(BIN引擎+自带NeXAS匹配规则+不开启截断，初步提取出人名后删掉pre_name分组再手动指定人名)

2、二次提取(JSON引擎)
- 先删除所有假名注释（详见我制作的bitter smile.补丁），再用此正则筛掉控制代码
```
10_search=(?P<unfinish>[^<>@a-zA-Z0-9－/\r\n]+)
```
