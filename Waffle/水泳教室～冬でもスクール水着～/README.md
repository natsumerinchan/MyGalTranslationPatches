# 水泳教室～冬でもスクール水着～ Kimi-K2-Instruct翻译补丁 

MD5: `68F4B0B3A70174122208FB6C66E383AE`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 使用方法
- 1.压缩包内字体可以不安装
- 2.解压压缩包并把所有文件复制到游戏根目录，双击运行`水泳教室_CHS.exe`(无需手动转区)

# Credits

- [GalTransl/GalTransl](https://github.com/GalTransl/GalTransl.git) :支持GPT-4/Claude/Deepseek/Sakura等大语言模型的Galgame自动化翻译解决方案
- [Crass-source](https://github.com/shangjiaxuan/Crass-source.git) :作者：痴汉公贼@飞雪之城 (解包时指定NekoSDK插件)
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [【工具】API HOOK和编码处理工具包](https://www.ai2.moe/topic/29225-【工具】api-hook和编码处理工具包)
- [xupefei/Locale-Emulator](https://github.com/xupefei/Locale-Emulator.git) :转区工具,使用了其中的dll

## NekoSDK引擎 *.txt SExtractor提取正则(仅适用于本作)
(TXT引擎+cp932编码+生成JIS替换配置)
```
00_search=^10\s.+?\s(?P<name>.+?)\s(?P<message>.+?)\/n$
05_search=^10\s.+?\s(?P<name>.+?)\s(?P<message>.+?)$
10_search=^obj\\.+?\.bmp\s(?P<message>.+?)$
structure=paragraph
```
