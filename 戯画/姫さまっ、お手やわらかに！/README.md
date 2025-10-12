# 姫さまっ、お手やわらかに！ gemini-2.5-pro 翻译补丁

MD5: `F3E0F20B69FC9F502EAA51EA03DF9E8E`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 注
- 1、已整合修正补丁v1.03和免DVD补丁

## 使用方法
- 1、解压压缩包并把所有文件复制到游戏根目录，双击运行`HIME_CHS.exe`

# Credits

- [GalTransl/GalTransl](https://github.com/GalTransl/GalTransl.git) :支持GPT-4/Claude/Deepseek/Sakura等大语言模型的Galgame自动化翻译解决方案
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [GalTools/GalArc](https://github.com/GalTools/GalArc.git) :Galgame解包和打包工具(NEXAS版本2，压缩方式none)
- [【工具】API HOOK和编码处理工具包](https://www.ai2.moe/topic/29225-【工具】api-hook和编码处理工具包)
- [xupefei/Locale-Emulator](https://github.com/xupefei/Locale-Emulator.git) :转区工具,使用了其中的dll

# SExtractor提取正则
1、初步提取
(BIN引擎+cp932编码+JIS不开启替换配置+免截断+SE自带NeXAS引擎规则)

2、二次提取
(JSON引擎+UTF-8编码+开启JIS替换配置)
```
10_search=(?P<unfinish>[^@a-zA-Z0-9－/\r\n　_]+)
```
