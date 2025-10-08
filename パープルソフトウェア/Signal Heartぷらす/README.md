# Signal Heartぷらす claude-3-5-sonnet-20241022翻译补丁 

MD5: `177915168F7E3CE671F18C2B663215E1`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 使用方法
- 1.依次应用修正补丁v12和v12s
- 2.解压压缩包并把`所有文件`复制到游戏根目录，双击运行`シグナルハート_ぷらす_CHS.exe`(无需手动转区)

# Credits

- [nanami5270/GARbro-Mod](https://github.com/nanami5270/GARbro-Mod.git) :Galgame解包和打包工具
- [amayra/arc_conv](https://github.com/amayra/arc_conv.git) :由 w8m 以纯 ASM 编写的命令行视觉小说工具包
- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-3.5/GPT-4/Newbing/Sakura等大语言模型的Galgame自动化翻译解决方案
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [【工具】API HOOK和编码处理工具包](https://www.ai2.moe/topic/29225-【工具】api-hook和编码处理工具包)
- [xupefei/Locale-Emulator](https://github.com/xupefei/Locale-Emulator.git) :转区工具,使用了其中的dll
- 补丁测试人员: [伪恶君子333@御爱同萌](https://www.ai2.moe/profile/9569-伪恶君子333/)

# QLIE引擎 *.s SExtractor提取正则(仅适用于本作)
(TXT引擎+cp932编码+生成JIS替换配置)
```
00_skip=^[@^\\\/\s]
01_search=^(\[rb.+?)$
02_search=^.[^\[]+?,(?P<name>.+?),(?P<msg>.+?)$
03_search=^(.+?)$
structure=paragraph
```

# QLIE引擎arc_conv打包命令(需保持目录结构)
```
.\arc_conv.exe --pack qlie .\data12 .\data12.pack
```
