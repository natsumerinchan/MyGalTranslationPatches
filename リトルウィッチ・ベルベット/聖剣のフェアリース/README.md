# 聖剣のフェアリース claude-3.7-sonnet(openrouter) 翻译补丁

MD5: `B3DFF6B452F4B1846F42C096C397402C`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 使用方法
- 1.解压压缩包并把所有文件复制到游戏根目录，双击フェアリース_CHS.exe运行
- 2.字体无需安装

## 更新日志
- 2025.4.14 19:00 首次提交

# Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-3.5/GPT-4/Newbing/Sakura等大语言模型的Galgame自动化翻译解决方案
- [amayra/arc_conv](https://github.com/amayra/arc_conv.git) :由 w8m 以纯 ASM 编写的命令行视觉小说工具包
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [Enigma Virtual Box](https://enigmaprotector.com/assets/files/enigmavb.exe) :把脚本文件打包进exe
- [【工具】API HOOK和编码处理工具包](https://www.ai2.moe/topic/29225-【工具】api-hook和编码处理工具包) :士佬制作的jis映射、字体生成、hook工具包
- [xupefei/Locale-Emulator](https://github.com/xupefei/Locale-Emulator.git) :转区工具,使用了其中的dll

### FFDSystem *.txt SExtractor文本提取正则

(TXT引擎+932编码+不生成JIS替换配置因为这里已经用API HOOK生成了jis替换后的json)

```
00_skip=^[\/\\a-zA-Z\{\}\)@#*]
05_search=^\tLogText\( text="\s(.+?)"
10_search=^-case text=\"(.+?)\"
15_skip=^[-\t]
20_skip=^\s//$
25_search=^\s(.+?)//$
30_search=^\s(.+?)$
35_search=^(.+?)//$
40_search=^(.+?)$
structure=paragraph
```

### FFDSystem arc_conv 解包和封包命令

```
解包：
arc_conv --list .\repipack.txt
（repipack.txt在arc_conv文件夹根目录有）

封包：
arc_conv --pack repipack .\xx .\xx.dat [1|2a|2|3|4|5] {key|key_index}
本作为：
arc_conv --pack repipack .\Message .\Message.dat 5 12
封包版本和key_index请自行穷举摸索，我也没搜到如何获取,
只知2002年的《白詰草話番外編 『津名川さん家のクリスマス』》是版本2,
2009年的本作，2010年的《シュガーコートフリークス》及2012年的《英雄＊戦姫》是版本5。

```

### png人名和png文本处理
见我制作的《シュガーコートフリークス》补丁<br>
https://github.com/natsumerinchan/MyGalTranslationPatches/tree/main/リトルウィッチ/シュガーコートフリークス

### FFDSystem 改用系统字体
解包System.dat，用shift_jis编码打开并编辑font.def
