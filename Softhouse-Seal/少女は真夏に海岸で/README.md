# 少女は真夏に海岸で gemini-2.5-pro 翻译补丁

MD5: `DFFFBB9064CA2021EF1066D3F85F28F1`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 注

- 游玩时无需转区，但鉴赏模式需要

## 使用方法

- 1、将压缩包内所有文件解压至游戏根目录，双击运行`SMK_CHS.exe`

## Credits

- [julixian/GalTranslPP](https://github.com/julixian/GalTranslPP.git) :GalTransl的C++实现
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [nanami5270/GARbro](https://github.com/nanami5270/GARbro) :Galgame解包和打包工具
- [arcusmaximus/KirikiriTools](https://github.com/arcusmaximus/KirikiriTools.git) :Xp3Pack.exe 打包xp3

## krkr *.ks SExtractor提取正则(仅适用于本作)

(TXT引擎+UTF-16编码+不进行JIS替换)

```txt
00_search=^\[msg\s+name\=\"\s{0,}(?P<name>.+?)\s{0,}\"
01_skip=^\[msg\]$
02_skip=^\;
03_skip=^\s{0,}作成者
04_search=^\[linkitem\s+text\=\"(.+?)\"
05_search=^\s{0,}(?P<end_unfinish>.+?)\s{0,}\[mpc\]\s{0,}$
10_search=^\s{0,}(?P<start_unfinish>.+?)\s{0,}\[r\]\[l\]\s{0,}$
15_search=^\s{0,}(?P<start_unfinish>.+?)\s{0,}\[r\]\s{0,}$
20_search=^\s{0,}(.+?)\s{0,}$
postSkip=^[A-Za-z0-9\*\[\]\\\/\;\{\}_\(\)\t%&\"\|\+]
struct=paragraph
```
