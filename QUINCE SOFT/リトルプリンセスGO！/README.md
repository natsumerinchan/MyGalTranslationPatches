# リトルプリンセスGO！ claude-3-5-sonnet-20240620 翻译补丁

MD5: `D76BAB45C5EECB002FC7943D6A65A0E0`

作者： natsumerinchan(Github) == 雨宮ゆうこ(2dfan)

用claude翻个新

## 使用方法
1.安装修正补丁v1.01
2.解压压缩包并把所有文件复制到游戏根目录，双击lingo_claude3.5s.exe运行

# Credits

- [GalTransl/GalTransl](https://github.com/GalTransl/GalTransl.git) :支持GPT-4/Claude/Deepseek/Sakura等大语言模型的Galgame自动化翻译解决方案
- [nanami5270/GARbro-Mod](https://github.com/nanami5270/GARbro-Mod.git) :Galgame解包和打包工具
- [nanami5270/BGI_Script_Tool](https://github.com/nanami5270/BGI_Script_Tool.git) :BGI引擎脚本提取和打包工具(要改源码把写入时的编码从utf-8改为shift-jis)
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [Enigma Virtual Box](https://enigmaprotector.com/assets/files/enigmavb.exe) :把脚本文件打包进exe
- [AtomCrafty/UniversalInjectorFramework](https://github.com/AtomCrafty/UniversalInjectorFramework.git) :实现更改字体，jis映射
- [リトルプリンセスＧＯ！免DVD补丁](https://2dfan.com/downloads/18230)

### SExtractor文本提取正则

先用两条正则删除所有◇行`^◇.+?◇.+`和空行`^(\t)*$\n`

再用SExtractor提取文本:
```
00_skip=^◆.+?◆[　#_A-Za-z0-9]
01_search=^◆.+?◆(?P<name>ギフト)$
10_search=^◆.+?◆(?P<pre_nameANDmsg>「.+)$
20_search=^◆.+?◆(?P<msg>.+)$
structure=paragraph
```