# 最高に都合のいいパイズリ上手のマリーさん MOTION EDITION gemini-2.5-pro翻译补丁 

MD5: `24FE3DB0290EF2C653F9FB3FBF8AD1E3`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 使用方法
- 1.解压压缩包并把所有文件复制到游戏根目录，双击运行paizuri_me.exe(无需转区)
- 2.进设置改用支持中文的字体如黑体、微软雅黑等

## 注
由于我不会脱enigma壳所以没法像第二部那样在设置添加多语言选项，且为了方便书写提取正则我用python把英文和简繁体的译文批量删干净了

# Credits

- [GalTransl/GalTransl](https://github.com/GalTransl/GalTransl.git) :支持GPT-4/Claude/Deepseek/Sakura等大语言模型的Galgame自动化翻译解决方案
- [detached64/GalArc](https://github.com/detached64/GalArc.git) :Galgame解包和打包工具(kirikiri引擎，xp3打包时选版本2)
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本

## krkrz引擎*.wks SExtractor提取正则
(TXT引擎+utf-8编码+不进行JIS替换)
```
00_search=^\[Talk\s+name\=(?P<name>.+?)\]$
05_skip=^\s+$
10_search=^(?P<unfinish>.+?)／$
15_search=^\s+\[macCmd\s+num\=.+?text\=(.+?)\]$
20_search=^(.+?)$
postSkip=^[;\[\]*\t\/\\]
structure=paragraph
```
