# ホワイトループ ～君に会うために僕はイクッ！～ gemini-2.5-pro 翻译补丁

MD5: `C70966A2C0EBA6AFB929336014AF6E69`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 使用方法

- 1、将压缩包内所有文件解压至游戏根目录，双击运行`loop.exe`

## Credits

- [julixian/GalTranslPP](https://github.com/julixian/GalTranslPP.git) :GalTransl的C++实现
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本(tools\unity里的encrypt_dsm.py可用于加解密data.dsm)

## Unity引擎 (data.dsm->)data.txt SExtractor提取正则(仅适用于本作)

(TXT引擎+UTF-8-SIG编码+不进行JIS替换)

```txt
00_search=^\s{0,}\[OnName num=\"(?P<name>.+?)\"\]\s{0,}$
05_search=^\s{0,}(.+?)\s{0,}$
postSkip=^[@\*\[\]\;]
struct=paragraph
```
