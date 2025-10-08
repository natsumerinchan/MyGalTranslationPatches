# ソルティアンジュ魔法倶楽部 gemini-2.5-pro翻译补丁

MD5: `CF1BDF72548042CEC5506B275B4279BE`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 使用方法
- 1.应用修正补丁V1.01并安装压缩包内字体(以前安装过我字体的也要重新安装因为我改了替换表)
- 2.解压压缩包并把`所有文件`复制到游戏根目录，转区运行`ソルティアンジュ魔法倶楽部.exe`

# Credits

- [nanami5270/GARbro-Mod](https://github.com/nanami5270/GARbro-Mod.git) :Galgame解包和打包工具
- [amayra/arc_conv](https://github.com/amayra/arc_conv.git) :由 w8m 以纯 ASM 编写的命令行视觉小说工具包
- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-3.5/GPT-4/Newbing/Sakura等大语言模型的Galgame自动化翻译解决方案
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本

# QLIE引擎 *.s SExtractor提取正则(仅适用于本作)
(TXT引擎+cp932编码+生成JIS替换配置)
```
00_search=^\^select\,\d+\,\,(.+?)\,(.+?)$
05_skip=^[@^\\\/\s]
10_search=^(\[rb.+?)$
15_search=^.[^\[]+?,(?P<name>.+?),(?P<msg>.+?)$
20_search=^(.+?)$
structure=paragraph
```

# QLIE引擎arc_conv打包命令(需保持目录结构)
```
.\arc_conv.exe --pack qlie .\data5 .\data5.pack
```
