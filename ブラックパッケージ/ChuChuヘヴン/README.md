# ChuChuヘヴン gemini-2.5-pro 翻译补丁

MD5: `D6D90B186C0038905AD7195D03193C16`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 使用方法

1.解压压缩包并把`X2WIN`文件夹所有内容复制到游戏根目录，双击运行CHS_X2WIN.EXE

## Credits

- [julixian/GalTranslPP](https://github.com/julixian/GalTranslPP.git) :GalTransl的C++实现
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [FFA System引擎翻译演示](https://www.ai2.moe/topic/31711-ffa-system引擎翻译演示)
- [【工具】API HOOK和编码处理工具包](https://www.ai2.moe/topic/29225-【工具】api-hook和编码处理工具包)
- [xupefei/Locale-Emulator](https://github.com/xupefei/Locale-Emulator.git) :转区工具,使用了其中的dll

## FFA System引擎 *.txt SExtractor提取正则

(TXT引擎+UTF-8编码+JIS替换)

```txt
00_skip=^●.+?●\s+$
05_search=^●.+?●\s{0,}(?P<name>[^\/\\\s]+?)\/(.+?)\s{0,}$
10_search=^●.+?●\s{0,}\/(.+?)\s{0,}$
15_search=●.+?●\s{0,}(.+?)\s{0,}$
postSkip=^[A-Za-z0-9\$]
JisEncodeName=shift-jis
struct=paragraph
```

## JSON二次提取正则

(JSON引擎+UTF-8编码+不进行JIS替换)

```txt
10_search=(?P<unfinish>[^\$A-Za-z0-9\=\\\/\r\n]+)
```
