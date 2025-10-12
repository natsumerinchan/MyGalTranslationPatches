# 真夏の小さな恋物語 gemini-2.5-pro 翻译补丁

MD5: `F414C9A8711BAD2009FA3E8CFAFCF6E9`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 使用方法

- 1.解压压缩包并把所有文件复制到游戏根目录，双击运行cs2.exe

## Credits

- [julixian/GalTranslPP](https://github.com/julixian/GalTranslPP.git) :GalTransl的C++实现
- [crskycode/GARbro](https://github.com/crskycode/GARbro) :Galgame解包和打包工具
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [regomne/chinesize](https://github.com/regomne/chinesize.git) :galgame破解工具集，使用其中CatSystem2引擎的exthg3(hg3图片解包和封包)
- [lifegpc/msg-tool](https://github.com/lifegpc/msg-tool.git) :多引擎文本提取和导入工具
- [xd2333/GalTransl_DumpInjector](https://github.com/xd2333/GalTransl_DumpInjector.git) :VNTranslationTools和msg-tool的GUI界面
- [【工具】API HOOK和编码处理工具包](https://www.ai2.moe/topic/29225-【工具】api-hook和编码处理工具包)
- [xupefei/Locale-Emulator](https://github.com/xupefei/Locale-Emulator.git) :转区工具,使用了其中的dll

## exthg3编译方法

安装go工具链并设置好环境变量后,在exthg3目录执行

```pwsh
go mod init exthg3
go mod tidy
go get github.com/regomne/bstream
go build -buildvcs=false -o .\hg3tool.exe .
```

## msg-tool导出json SExtractor二次提取正则

(JSON引擎+UTF-8编码+JIS替换)

```txt
10_search=(?P<unfinish>[^@a-zA-Z0-9\;\\\/\r\n ]+)
```

## 本作人名处理

参见[真夏の夜の雪物語 -MIDSUMMER SNOW NIGHT- gemini-2.5-pro 翻译补丁](https://github.com/natsumerinchan/MyGalTranslationPatches/tree/main/エックスワン/真夏の夜の雪物語%20-MIDSUMMER%20SNOW%20NIGHT-)
