# はめ☆ドリ～Happy Mellowly Dreams!～ gemini-2.5-pro 翻译补丁

MD5: `6928F78351A8CF0B1A1B05E319A91995`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 使用方法
- 1.将压缩包内所有文件解压至游戏根目录，双击运行hame_chs.exe(用了GBK编码请勿转区)

# Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-3.5/GPT-4/Newbing/Sakura等大语言模型的Galgame自动化翻译解决方案
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [amayra/arc_conv](https://github.com/amayra/arc_conv.git) :由 w8m 以纯 ASM 编写的命令行视觉小说工具包
- [【工具】API HOOK和编码处理工具包](https://www.ai2.moe/topic/29225-【工具】api-hook和编码处理工具包)

### Nscripter引擎 nscript.dat转txt明文
对nscript.dat异或0x84即可，如：
```
arc_conv --mod xor 84 .\nscript.dat .\0.txt
```

### Nscripter引擎 0.txt SExtractor文本提取正则(仅适用于本作)
(TXT引擎+cp932->gbk编码+不生成jis替换配置)
```
01_skip=^@$
02_search=^csel "(.+?)",\*.+?,"(.+?)",\*.+?$
03_search=^csel "(.+?)",\*.+?,$
04_search=^\s+"(.+?)",\*.+?$
05_search=^\[(?P<name>.+?)\/.+?\]$
10_search=^\[(?P<name>.+?)\/\]$
15_search=^\[(?P<name>.+?)\/.+?\](?P<message>.+?)\\$
20_search=^\[(?P<name>.+?)\/\](?P<message>.+?)\\$
25_search=^(?P<end_unfinish>.+?)\\$
30_search=^(?P<unfinish>.+?)@$
35_search=^(.+?)$
postSkip=^[A-Za-z0-9*;\s]
structure=paragraph
```
