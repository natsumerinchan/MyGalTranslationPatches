# おとなり恋戦争！ gemini-2.5-pro 翻译补丁

MD5: `2F5E2DBA8DEBE5B316B93AD3FE8EBE6A`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 使用方法
- 1、安装压缩包内字体
- 2、删除savedata文件夹内的data_anchor.ksd、datasc.ksd、krenvprf.kep和savecheck否则字体不生效
- 3、将压缩包内所有文件解压至游戏根目录，转区运行おとなり恋戦争！.exe

## 注
- 1、为保证语音正常，本作人名没有翻译，需要转日区运行

# Credits

- [julixian/GalTranslPP](https://github.com/julixian/GalTranslPP.git) :GalTransl的C++实现
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [crskycode/GARbro](https://github.com/crskycode/GARbro) :Galgame解包和打包工具
- [arcusmaximus/KirikiriTools](https://github.com/arcusmaximus/KirikiriTools.git) :Xp3Pack.exe 打包xp3
- 测试人员： [伪恶君子333@御爱同萌](https://www.ai2.moe/profile/9569-伪恶君子333/)

## krkr *.ks SExtractor提取正则(仅适用于本作)
(TXT引擎+UTF-16编码+不进行JIS替换)
```
00_skip=^$
01_skip=^(?P<name>【.+?】)$
05_search=^\s+(?P<end_unfinish>「.+?」)\[.+?\]$
06_search=^\s+(?P<end_unfinish>「.+?」)$
10_search=^\s+(?P<end_unfinish>（.+?）)\[.+?\]$
11_search=^\s+(?P<end_unfinish>（.+?）)$
15_search=^\s+(?P<end_unfinish>『.+?』)\[.+?\]$
16_search=^\s+(?P<end_unfinish>『.+?』)$
20_search=^(?P<end_unfinish>「.+?」)\[.+?\]$
21_search=^(?P<end_unfinish>「.+?」)$
25_search=^(?P<end_unfinish>（.+?）)\[.+?\]$
26_search=^(?P<end_unfinish>（.+?）)$
30_search=^(?P<end_unfinish>『.+?』)\[.+?\]$
31_search=^(?P<end_unfinish>『.+?』)$
35_search=^\s+(?P<end_unfinish>「[^「].+?」)$
40_search=^\s+(?P<end_unfinish>「[^（].+?）)$
45_search=^\s+(?P<end_unfinish>「[^『].+?』)$
50_search=^(?P<end_unfinish>「[^「].+?」)$
55_search=^(?P<end_unfinish>「[^（].+?）)$
60_search=^(?P<end_unfinish>「[^『].+?』)$
65_search=^\s+(?P<start_unfinish>「[^」].+?)$
70_search=^\s+(?P<start_unfinish>（[^）].+?)$
75_search=^\s+(?P<start_unfinish>『[^』].+?)$
80_search=^(?P<start_unfinish>「[^」].+?)$
85_search=^(?P<start_unfinish>（[^）].+?)$
90_search=^(?P<start_unfinish>『[^』].+?)$
95_search=^\s+(?P<start_unfinish>.+?、)$
100_search=^(?P<start_unfinish>.+?)$
105_search=^\s+(.+?)\[.+?\]$
110_search=^\s+(.+?)$
115_search=^(.+?)\[.+?\]$
120_search=^(.+?)$
postSkip=^[@\[\]\*\;$%A-Za-z0-9#\^\s\/\\\:]
structure=paragraph
```

## json二次提取正则
(JSON引擎+UTF-8编码+不进行JIS替换)
```
10_search=(?P<unfinish>[^=@a-zA-Z0-9－\r\n\[\] ]+)
```
