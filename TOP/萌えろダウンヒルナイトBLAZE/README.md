# 萌えろダウンヒルナイトBLAZE qwen-max-latest 翻译补丁 

MD5: `A5501BE00A15D21E119460A99F9C6E62`

作者： natsumerinchan(Github) == 雨宮ゆうこ

还未推完，有bug请反馈（截图加发送存档）

## 使用方法
1.解压压缩包并把所有文件复制到游戏根目录，安装压缩包内字体后转区运行萌えろダウンヒルナイトBLAZE_CHS.exe

# Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-3.5/GPT-4/Newbing/Sakura等大语言模型的Galgame自动化翻译解决方案
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [Enigma Virtual Box](https://enigmaprotector.com/assets/files/enigmavb.exe) :把脚本文件打包进exe
- [asmodean/expkd](http://asmodean.reverse.net/pages/expkd.html) :BladeEngine引擎*.pkd解包工具，我让DeepSeek-R1为其拓展了封包功能(pkdtool)

BladeEngine引擎 *.scp SExtractor文本提取正则(TXT引擎+932编码)

(BladeEngine引擎每29字必须换一次行)
```
00_skip=^[→a-zA-Z0-9;,*@$#/\[{}]
01_search=^\s(?P<unfinish>.+?)\,\*.+$
02_search=^(?P<unfinish>.+?)\,\*.+$
03_search=^\s(?P<unfinish>.+?)\,[0-9].+$
04_search=^(?P<unfinish>.+?)\,[0-9].+$
05_search=^\s(?P<unfinish>.+)$
06_search=^(?P<unfinish>.+)$
struct=para
```
