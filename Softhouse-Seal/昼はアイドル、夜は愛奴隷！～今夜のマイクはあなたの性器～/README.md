# 昼はアイドル、夜は愛奴隷！～今夜のマイクはあなたの性器～ claude-3-7-sonnet 翻译补丁

MD5: `B92934EB6927FB42F94DB00305E35CBF`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 使用方法
- 1.将压缩包内所有文件解压至游戏根目录，安装压缩包内字体后转区运行昼はアイドル、夜は愛奴隷.exe

# Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-3.5/GPT-4/Newbing/Sakura等大语言模型的Galgame自动化翻译解决方案
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [amayra/arc_conv](https://github.com/amayra/arc_conv.git) :由 w8m 以纯 ASM 编写的命令行视觉小说工具包

### Nscripter引擎 nscript.dat转txt明文
对nscript.dat异或0x84即可，如：
```
arc_conv --mod xor 84 .\nscript.dat .\0.txt
```

### Nscripter引擎 *.txt SExtractor文本提取正则(仅适用于本作)
(TXT引擎+932编码+生成JIS替换配置)
```
00_search=^\[(?P<name>.+?)\/.+?\](.+?)$
05_search=^\[(?P<name>.+?)\](.+?)$
10_search=^(.+?)$
postSkip=^[A-Za-z;*_\"\t\s\-]
structure=paragraph
```
