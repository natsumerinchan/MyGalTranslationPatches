# フォルト!!SA（サービスエース） グランドスラムBOX V3版 gemini-2.5-pro 翻译补丁 

MD5：
- (フォルト!!A) `EE49BD51C2781711C527AD23173A80EC`
- (フォルト!!S) `686D10ACD43AC68FC05BBB61D1DED41C`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 注
- 1、本补丁仅支持フォルト!!SA版本，不支持单独的フォルト!!A和フォルト!!S
- 2、本作人名是图片形式，生成脚本已放在仓库，先用crass解包dat.arc获取name.csv得到人名行保存为txt(保持原顺序)，再运行对应游戏的人名生成脚本得到name.bmp回封到system.arc

## 更新日志
- 2025.08.20 23:30 首次提交
- 2025.08.24 15:43 补充フォルト!!A漏翻的内容

## 使用方法
- 1.解压压缩包并把所有文件复制到游戏根目录，双击运行FaultA_CHS.exe或FaultS_CHS.exe

# Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-3.5/GPT-4/Newbing/Sakura等大语言模型的Galgame自动化翻译解决方案
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [amayra/arc_conv](https://github.com/amayra/arc_conv.git) :由 w8m 以纯 ASM 编写的命令行视觉小说工具包
- [Crass-source](https://github.com/shangjiaxuan/Crass-source.git) :解包工具，作者：痴汉公贼@飞雪之城 (RPM ADV SYSTEM插件，特殊参数为code=FaultSA)
- [【工具】API HOOK和编码处理工具包](https://www.ai2.moe/topic/29225-【工具】api-hook和编码处理工具包)
- [xupefei/Locale-Emulator](https://github.com/xupefei/Locale-Emulator.git) :转区工具,使用了其中的dll
- [关于RPM引擎](https://www.bilibili.com/opus/862771454202085408)

## RPM引擎 *.txt SExtractor文本提取正则
(TXT引擎+932编码+JIS替换)
```
00_search=^\<SltAdd\s+\d+\,.+?\,(?P<predel_unfinish>.+?)\>$
01_search=^(?P<message>\<WinFontSize.+\>.+?)$
02_search=^(?P<end_unfinish>.+?\<KW\>\<WinClear\>)$
03_search=^(?P<end_unfinish>.+?\<KW\>)$
04_search=^(?P<unfinish>.+?)<CR>$
05_search=^\s+(?P<unfinish>.+?)$
06_search=^(?P<unfinish>.+?)$
postSkip=^[\$\/\<\[\]A-Za-z*【]
structure=paragraph
```

## JSON二次提取正则
(JSON引擎+UTF-8编码+不进行JIS替换)
```
10_search=(?P<unfinish>[^@A-Za-z0-9\<\>\\\/\r\n\,\. ]+)
```

## RPM引擎 arc_conv打包命令
```
arc_conv --pack ciel .\msg .\msg.arc {0|1|2|3|4|5} <key>

本作为:
arc_conv --pack ciel .\msg .\msg.arc 1 FaultSA
```
