# まじかる☆萌えりん♪ DeepSeek-V3 翻译补丁 v1.0.0

MD5: `9B7ECE6BCF1AEC14E7C0CD31836E26A5`

作者： natsumerinchan(Github) == 雨宮ゆうこ

未作完整测试，有bug请反馈（截图加私发存档）。

## 使用方法
- 1.解压压缩包并把所有文件复制到游戏根目录，安装压缩包内字体后转区运行moerin_dsv3.exe

# Credits

- [GalTransl/GalTransl](https://github.com/GalTransl/GalTransl.git) :支持GPT-4/Claude/Deepseek/Sakura等大语言模型的Galgame自动化翻译解决方案
- [arcusmaximus/VNTranslationTools](https://github.com/arcusmaximus/VNTranslationTools.git) :视觉小说翻译工具(SYSTEMNNN引擎.spt脚本)
- [amayra/arc_conv](https://github.com/amayra/arc_conv.git) :由 w8m 使用纯 ASM 编写的命令行视觉小说工具包
- [Enigma Virtual Box](https://enigmaprotector.com/assets/files/enigmavb.exe) :把脚本文件打包进exe
- [wxMEdit/wxMEdit](https://github.com/wxMEdit/wxMEdit.git) :wxMEdit，跨平台文本/十六进制编辑器，MadEdit 的改进版

### arc_conv *.spt 异或处理命令(非必须，仅用于检查回封的译文，用十六进制编辑器打开)
```
解密：
arc_conv --mod xor ff .\xxx.spt .\xxx.dec
加密：
arc_conv --mod xor ff .\xxx.dec .\xxx.spt
```

