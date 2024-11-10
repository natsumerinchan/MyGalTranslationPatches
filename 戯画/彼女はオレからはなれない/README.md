# 彼女はオレからはなれない claude-3-5-sonnet-20240620 翻译补丁 

MD5: `FDC66575939C0A261CE5208E81B8C8C5`

作者： natsumerinchan(Github) == 雨宮ゆうこ(2dfan)

已按攻略把所有路线Ctrl了一遍，未出现闪退，但发现有零星漏翻

## 使用方法
1、安装升级补丁v1.02
2、应用站内免DVD补丁
3、解压压缩包并把所有文件复制到游戏根目录，双击Anoore.exe运行(无需手动转区因为UniversalInjectorFramework会自动处理)

# Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-3.5/GPT-4/Newbing/Sakura等大语言模型的Galgame自动化翻译解决方案
- [ginyoushijin/GIGA_NeXAS](https://github.com/ginyoushijin/GIGA_NeXAS.git) :戏画引擎解/封包 (需配合转区软件使用，否则解包出来的bin文件名会乱码)
- [AtomCrafty/UniversalInjectorFramework](https://github.com/AtomCrafty/UniversalInjectorFramework.git) :实现自动转区和更改字体
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本，使用了其jis替换字体
- [xupefei/Locale-Emulator](https://github.com/xupefei/Locale-Emulator.git) :转区软件,使用了其中的dll

# SExtractor提取正则
1、初步提取(BIN引擎)
```
01_skip=^[\S\s]{0,3}$
02_skip=^[^@\x81-\xFC]
10_search=^[0-~]*「(?P<msg>[\x81-\xFC][ 0-\xFC]+?)」
20_search=^[0-~]*「(?P<unfinish>[\x81-\xFC][ 0-\xFC]+?)@e
30_search=^[0-~]*([\x81-\xFC][ 0-\xFC]+?)」
40_search=^[0-~]*(?P<unfinish>[\x81-\xFC][ 0-\xFC]+?)@e
50_search=^[0-~]*([\x81-\xFC][ 0-\xFC]+?)@k
60_search=^[0-~]*([\x81-\xFC][ 0-\xFC]+?)$
checkJIS=[ 0-~]
ignoreDecodeError=1
postSkip=_.*[^」a-zA-Z]$|[0-9]$
separate=\x00
struct=para
sample=
<暴力匹配，日文仅允许双字节，每行结尾限定字符>
```
2、二次提取(JSON引擎)
先删除所有假名注释（详见我制作的bitter smile.补丁），再用此正则筛掉控制代码
```
10_search=(?P<unfinish>[^@a-zA-Z0-9－/\r\n]+)
```