# 萌えろダウンヒルナイト -峠最速伝説- qwen-max-latest 翻译补丁 
(基于2009-10-21英文版制作，因为找不到2007-03-08的日文版资源，05版旧引擎咱不会弄)

MD5: `A65D16586907E4191547FC6DE29DC8F2`

作者： natsumerinchan(Github) == 雨宮ゆうこ

还未推完，有bug请反馈（截图加发送存档）

## 使用方法
1.解压压缩包并把所有文件复制到游戏根目录，双击运行Moero Downhill Night Type R_CHS.exe

# Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-3.5/GPT-4/Newbing/Sakura等大语言模型的Galgame自动化翻译解决方案
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [Enigma Virtual Box](https://enigmaprotector.com/assets/files/enigmavb.exe) :把脚本文件打包进exe
- [asmodean/expkd](http://asmodean.reverse.net/pages/expkd.html) :BladeEngine引擎*.pkd解包工具，我让DeepSeek-R1为其拓展了封包功能(pkdtool)，工具及源码放在第二部那里

BladeEngine引擎英文版*.scp SExtractor文本提取正则(TXT引擎+UTF-16编码)
```
00_skip=^[→;,*@0-9$#/\[{}]
01_skip=^(if\(|if \(|[A-Za-z]+[0-9]+|set|return|select|ongoto|dim@)
02_skip=^(gosub|:|　set|[A-Z]+:)
03_skip=^case\s[0-9],\s""$
04_search=^case\s[0-9],\s"(.+)"$
05_search=^(?P<unfinish>.+?),\*.+$
06_search=^(?P<unfinish>.+?),[a-z]+[0-9]+
07_search=^(?P<unfinish>.+)$
structure=paragraph
```
