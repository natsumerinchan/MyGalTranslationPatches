# Maple Colors 2 gemini-2.5-pro 翻译补丁

MD5: `FDA1C4423CAB06CA2C9C2C58BE531FBB`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 使用方法

- 1、解压压缩包并把所有文件复制到游戏根目录，双击运行`Maple2.exe`

## Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-4/Claude/Deepseek/Sakura等大语言模型的Galgame自动化翻译解决方案
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [asmodean-tools/exdaf2](https://github.com/hiroshil/asmodean-tools/tree/main/exdaf2) : 解包DenSDK引擎的DAF2文件头dat文件，原作者asmodean
- [【工具】API HOOK和编码处理工具包](https://www.ai2.moe/topic/29225-【工具】api-hook和编码处理工具包)
- [xupefei/Locale-Emulator](https://github.com/xupefei/Locale-Emulator.git) :转区工具,使用了其中的dll

## SExtractor提取正则

1、DenSDK引擎 *.txt 提取正则  
(TXT引擎+cp932编码+开启JIS替换配置)

```txt
00_search=^\s{0,}\<Name\s+(?P<name>.+?)\>\s{0,}$
01_search=^\s{0,}s\<Name\s+(?P<name>.+?)\>\s{0,}$
05_search=^\s{0,}\<Text\s+\d+\s+([^\>]+?)\>
10_search=^\s{0,}\<Text\s+([^\>]+?)\>
15_search=^\s{0,}(?P<end_unfinish>[^\>]+?)\>
20_search=^\s{0,}\<Text\s+\d+\s+(?P<start_unfinish>[^\>]+?)\s{0,}$
25_search=^\s{0,}\<Text\s+(?P<start_unfinish>[^\>]+?)\s{0,}$
30_search=^\s{0,}\<MenuAdd\s+\d+\s+([^\>]+?)\>
35_skip=^\<
40_search=^\s{0,}(.+?)\s{0,}$
postSkip=^[a-z0-9\/\<\:\;\t；\,]
struct=paragraph
```

2、json二次提取  
(JSON引擎+UTF-8编码+不开启JIS替换配置)

```txt
10_search=(?P<unfinish>[^@a-zA-Z0-9\\\/\r\n]+)
```
