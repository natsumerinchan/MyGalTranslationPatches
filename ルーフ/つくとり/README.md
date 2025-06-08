# つくとり gemini-2.5-pro-exp-03-25 翻译补丁

MD5: `503779385BB8C94A89969906D5FC6A49`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 使用方法
- 1、解压压缩包并把所有文件复制到游戏根目录，双击运行TUKU_CHS.EXE（字体可以不安装）

# Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-4/Claude/Deepseek/Sakura等大语言模型的Galgame自动化翻译解决方案
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [【工具】API HOOK和编码处理工具包](https://www.ai2.moe/topic/29225-【工具】api-hook和编码处理工具包)
- [xupefei/Locale-Emulator](https://github.com/xupefei/Locale-Emulator.git) :转区工具,使用了其中的dll
- 测试人员： [伪恶君子333@御爱同萌](https://www.ai2.moe/profile/9569-伪恶君子333/)

# 椎名里緒 *.txt提取正则(TXT引擎+932编码)
```
00_skip=^[$;]
05_search=^【(?P<name>.+)】$
10_search=^(.+)$
structure=paragraph
JisEncodeName=shift-jis
```

# 椎名里緒v2.37 *.WAR解包和免封包
- 解包用garbro，翻译好的脚本扔进游戏根目录script文件夹即可实现免封包读取
