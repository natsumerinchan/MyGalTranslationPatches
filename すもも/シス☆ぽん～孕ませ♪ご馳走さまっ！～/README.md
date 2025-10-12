# シス☆ぽん～孕ませ♪ご馳走さまっ！～ DeepSeek-V3-0324 翻译补丁

MD5: `299A78BEA5372ABA6864C3F351000C21`

作者： natsumerinchan(Github) == 雨宮ゆうこ

已全程ctrl无闪退，有其他bug请反馈

## 使用方法
- 1、解压压缩包并把所有文件复制到游戏根目录，双击运行SISPON_CHS.exe

# Credits

- [GalTransl/GalTransl](https://github.com/GalTransl/GalTransl.git) :支持GPT-4/Claude/Deepseek/Sakura等大语言模型的Galgame自动化翻译解决方案
- [amayra/arc_conv](https://github.com/amayra/arc_conv.git) :由 w8m 以纯 ASM 编写的命令行视觉小说工具包
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [AtomCrafty/UniversalInjectorFramework](https://github.com/AtomCrafty/UniversalInjectorFramework.git) :实现自动转区和更改字体，jis映射
- [xupefei/Locale-Emulator](https://github.com/xupefei/Locale-Emulator.git) :转区工具,使用了其中的dll

# 椎名里緒 *.txt提取正则(TXT引擎+932编码)
```
00_skip=^[$;]
05_search=^【(?P<name>.+)】$
10_search=^(.+)$
```

# 椎名里緒v2.40 *。WAR解包和封包
- 解包:
将arc_conv的examples文件夹中的warcscan.bat复制到arc_conv.exe所在目录，<br>
在arc_conv.exe的`属性`-`兼容性`勾选`以管理员身份运行此程序`并保存。<br>
转区启动游戏后运行warcscan.bat以获得*.WAR的解包密钥。
```
.\arc_conv.exe -o dir --dest <输出路径> --warc <解包密钥> <目标*.WAR>
```

- 封包:
(v2.40版本的椎名里緒不用修bug可无脑使用arc_conv封包，高版本可用士佬做的hook工具SBRioshiina实现免封包)
```
arc_conv --pack warc <目标目录> <输出*.WAR的路径>
```
