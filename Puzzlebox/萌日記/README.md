# 萌日記 qwen-max-latest 翻译补丁 

MD5: `2358C7A0BD5318F81624311ABED5D83C`

作者： natsumerinchan(Github) == 雨宮ゆうこ

未作完整测试，有bug请反馈（截图加发送存档）

## 使用方法
1.解压压缩包并把所有文件复制到游戏根目录，安装压缩包内字体后转区运行MoeDiary_CHS.exe

# Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-3.5/GPT-4/Newbing/Sakura等大语言模型的Galgame自动化翻译解决方案
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [Enigma Virtual Box](https://enigmaprotector.com/assets/files/enigmavb.exe) :把脚本文件打包进exe
- [amayra/arc_conv](https://github.com/amayra/arc_conv.git) :由 w8m 以纯 ASM 编写的命令行视觉小说工具包
- [crskycode/GARbro](https://github.com/crskycode/GARbro) :Galgame解包和打包工具

RPM引擎 *.txt SExtractor文本提取正则(TXT引擎+932编码)

```
01_search=^(?P<name>【.+】)
02_search=^<WinFontSize.+>(?P<msg>[^<>]+)<.+>$
03_skip=^[/<\[]
04_search=^(?P<end_unfinish>[^<>@debug]+)<.+>.+$
05_search=^(?P<unfinish>.+)$
structure=paragraph
```

RPM引擎 arc_conv打包命令
```
arc_conv --pack ciel .\msg .\msg.arc {0|1|2|3|4|5} <key>

本作为:
arc_conv --pack ciel .\msg .\msg.arc 1 moe
```
