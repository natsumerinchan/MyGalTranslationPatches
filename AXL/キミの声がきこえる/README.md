# キミの声がきこえる gpt-4o-2024-11-20 翻译补丁 

MD5: `4AF52800D580388EF375B41182558BC3`

作者： natsumerinchan(Github) == 雨宮ゆうこ

未作完整测试，有bug请反馈（截图加发送存档）

## 使用方法
- 1.应用修正补丁Ver.11
- 2.解压压缩包并把所有文件复制到游戏根目录，安装压缩包内字体后转区运行KIMIKOE_CHS.exe

# Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-3.5/GPT-4/Newbing/Sakura等大语言模型的Galgame自动化翻译解决方案
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [Enigma Virtual Box](https://enigmaprotector.com/assets/files/enigmavb.exe) :把脚本文件打包进exe
- [amayra/arc_conv](https://github.com/amayra/arc_conv.git) :由 w8m 以纯 ASM 编写的命令行视觉小说工具包
- [nanami5270/GARbro-Mod](https://github.com/nanami5270/GARbro-Mod.git) :Galgame解包和打包工具
- [AtomCrafty/UniversalInjectorFramework](https://github.com/AtomCrafty/UniversalInjectorFramework.git) :实现更改字体，jis映射
- [关于RPM引擎](https://www.bilibili.com/opus/862771454202085408)

RPM引擎 *.txt SExtractor文本提取正则(TXT引擎+932编码)

```
00_search=^(?P<name>【.+】)
01_search=^<WinFontSize.+>(?P<msg>[^<>]+)<.+>$
02_skip=^[$/<\[a-zA-Z]
03_search=^(?P<end_unfinish>[^<>@debug]+)<.+>.+$
04_search=^(?P<unfinish>.+)<CR>$
05_search=^(?P<unfinish>.+)$
structure=paragraph
```

RPM引擎 arc_conv打包命令
```
arc_conv --pack ciel .\script .\script.arc {0|1|2|3|4|5} <key>

本作为:
arc_conv --pack ciel .\script .\script.arc 1 KIMIKOE
```
