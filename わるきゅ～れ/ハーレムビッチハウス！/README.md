# ハーレムビッチハウス！ gemini-2.5-pro 翻译补丁

MD5: `10525154115CF80E12455793C962F783`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 使用方法

- 1、解压压缩包并把所有文件复制到游戏根目录，双击运行`VAL-0061(DL)_CHS.exe`

## Credits

- [julixian/GalTranslPP](https://github.com/julixian/GalTranslPP.git) :GalTransl的C++实现
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [Dir-A/ReVN](https://github.com/Dir-A/ReVN/releases) : Valkyria-Tools用于Valkyria引擎*.dat解包封包和*.sdt脚本提取回封
- [【工具】API HOOK和编码处理工具包](https://www.ai2.moe/topic/29225-【工具】api-hook和编码处理工具包)
- [xupefei/Locale-Emulator](https://github.com/xupefei/Locale-Emulator.git) :转区工具,使用了其中的dll

## SExtractor提取正则

1、Valkyria_SDT_TextEditor *.json 提取正则  
(TXT引擎+UTF-8编码+开启JIS替换配置)

```txt
00_search=^\s+\"tra\"\:\s+\"\s{0,}(?P<name>【.+?】)\"$
05_search=^\s+\"tra\"\:\s+\"\s{0,}(?P<end_unfinish>「.+?」)\"$
10_search=^\s+\"tra\"\:\s+\"\s{0,}(?P<end_unfinish>『.+?』)\"$
15_search=^\s+\"tra\"\:\s+\"\s{0,}(?P<end_unfinish>（.+?）)\"$
20_search=^\s+\"tra\"\:\s+\"\s{0,}(?P<end_unfinish>.+?」)\"$
25_search=^\s+\"tra\"\:\s+\"\s{0,}(?P<end_unfinish>」)\"$
30_search=^\s+\"tra\"\:\s+\"\s{0,}(?P<end_unfinish>.+?』)\"$
35_search=^\s+\"tra\"\:\s+\"\s{0,}(?P<end_unfinish>』)\"$
40_search=^\s+\"tra\"\:\s+\"\s{0,}(?P<end_unfinish>.+?）)\"$
45_search=^\s+\"tra\"\:\s+\"\s{0,}(?P<end_unfinish>）)\"$
50_search=^\s+\"tra\"\:\s+\"\s{0,}(?P<start_unfinish>「.+?)\"$
55_search=^\s+\"tra\"\:\s+\"\s{0,}(?P<start_unfinish>『.+?)\"$
60_search=^\s+\"tra\"\:\s+\"\s{0,}(?P<start_unfinish>（.+?)\"$
65_search=^\s+\"tra\"\:\s+\"\s{0,}\\\\r\s+(.+?)\"$
70_search=^\s+\"tra\"\:\s+\"\s{0,}(.+?)\"$
structure=paragraph
```

2、json二次提取  
(JSON引擎+UTF-8编码+不开启JIS替换配置)

```txt
10_search=(?P<unfinish>[^A-Za-z0-9\r\n\\\/]+)
```
