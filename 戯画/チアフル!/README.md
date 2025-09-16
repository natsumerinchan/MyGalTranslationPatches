# チアフル! gemini-2.5-pro 翻译补丁

MD5: `E90144410883F998E60EACB889C53C1B`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 注
- 1、已整合修正补丁v1.01和免DVD补丁

## 使用方法
- 1、解压压缩包并把所有文件复制到游戏根目录，双击运行`Cheerfull_CHS.exe`

# Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-4/Claude/Deepseek/Sakura等大语言模型的Galgame自动化翻译解决方案
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [GalTools/GalArc](https://github.com/GalTools/GalArc.git) :Galgame解包和打包工具(NEXAS版本2，压缩方式none)
- [【工具】API HOOK和编码处理工具包](https://www.ai2.moe/topic/29225-【工具】api-hook和编码处理工具包)
- [xupefei/Locale-Emulator](https://github.com/xupefei/Locale-Emulator.git) :转区工具,使用了其中的dll

# SExtractor提取正则
1、初步提取
(BIN引擎+cp932编码+不开启JIS替换配置+免截断)
```
00_search=^(俊|梢|楓)$
01_skip=^[\S\s]{0,3}$
02_skip=^[^@\x81-\xFC]
10_search=^[0-~]*(?P<pre_name>「[ 0-\xFC]+?)$
20_search=^[0-~]*([\x81-\xFC][ 0-\xFC]+?)$
checkJIS=[ 0-~]
ignoreDecodeError=1
postSkip=_.*[^」a-zA-Z]$|[0-9]$
separate=\x00
struct=para
sample=
<暴力匹配，日文仅允许双字节，每行结尾限定字符>
```

2、二次提取
(JSON引擎+UTF-8编码+开启JIS替换配置)
```
10_search=(?P<unfinish>[^@a-zA-Z0-9－/\r\n　_]+)
```
