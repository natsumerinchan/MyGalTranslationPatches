# メイでぃ！～ご主人様は同級生～ gemini-2.5-pro 翻译补丁

MD5: `8F7455C8C3FD79237EA98496B98C8D72`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 已知问题
- 1、人名是图片形式故没有翻译

## 使用方法
- 1.解压压缩包并把所有文件复制到游戏根目录，双击运行メイでぃ！_CHS.exe

# Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-3.5/GPT-4/Newbing/Sakura等大语言模型的Galgame自动化翻译解决方案
- [Crass-source](https://github.com/shangjiaxuan/Crass-source.git) :作者：痴汉公贼@飞雪之城，解包时指定AST插件
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本(tools/AST有打包工具)
- [【工具】API HOOK和编码处理工具包](https://www.ai2.moe/topic/29225-【工具】api-hook和编码处理工具包)
- [xupefei/Locale-Emulator](https://github.com/xupefei/Locale-Emulator.git) :转区工具,使用了其中的dll

## AST引擎 *.adv SExtractor提取正则(改编自SExtractor自带AST引擎正则)
(TXT引擎+cp932编码+JIS替换)
```
00_skip=^$
01_skip=^[;*]
10_search=<WINDOW .*?NAME="(?P<name>.+?)"
11_search=<SELECT TEXT="(.+?)"
12_search=^NAME\s+\"(.+?)\"$
15_skip=^(?:<[^<>]+>)+$
20_search=^【(?P<name>.+?)】([^<>].+?)$
25_search=(?P<unfinish>[^<>]+)
postSkip=^[A-Z0-9=\s;]
structure=paragraph
sample=<WINDOW NAME="春臣" IMAGE="name01.png">
「ちょっ……待って…………！」
```
