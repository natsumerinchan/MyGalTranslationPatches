# マキフェス！ DeepSeek-V3-0324 翻译补丁

MD5: `2302386994AC9DD47A5A085C3A20BD94`

作者： natsumerinchan(Github) == 雨宮ゆうこ

已全程ctrl无闪退，有其他bug请反馈

## 使用方法
- 1、解压压缩包并把所有文件复制到游戏根目录，双击运行MAKIFES_CHS.exe

# Credits

- [GalTransl/GalTransl](https://github.com/GalTransl/GalTransl.git) :支持GPT-4/Claude/Deepseek/Sakura等大语言模型的Galgame自动化翻译解决方案
- [amayra/arc_conv](https://github.com/amayra/arc_conv.git) :由 w8m 以纯 ASM 编写的命令行视觉小说工具包
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [AtomCrafty/UniversalInjectorFramework](https://github.com/AtomCrafty/UniversalInjectorFramework.git) :实现自动转区和更改字体，jis映射
- [xupefei/Locale-Emulator](https://github.com/xupefei/Locale-Emulator.git) :转区工具,使用了其中的dll
- [SBRioshiina——椎名理绪2.47-2.50通用免封包工具](https://www.ai2.moe/topic/29468-sbrioshiina%E2%80%94%E2%80%94%E6%A4%8E%E5%90%8D%E7%90%86%E7%BB%AA247-250%E9%80%9A%E7%94%A8%E5%85%8D%E5%B0%81%E5%8C%85%E5%B7%A5%E5%85%B7)

# 椎名里緒 *.txt提取正则(TXT引擎+932编码)
```
00_skip=^[$;]
05_search=^【(?P<name>.+)】$
10_search=^(.+)$
```
