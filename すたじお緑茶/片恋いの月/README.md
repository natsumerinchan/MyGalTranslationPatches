# 片恋いの月 claude-3-5-sonnet-20240620 翻译补丁

MD5: `49BDF17E156E7205220C230A92364F3F`

作者： natsumerinchan(Github) == 雨宮ゆうこ(2dfan)

## 已知问题
由于SAS5Tool暂不支持低于109000的引擎版本，本作暂时只能用SExtractor暴提+截断，<br>导致有部分文本未能翻译，尤其是有特效的文本（防止截断时控制符丢失）

## 使用方法
1.解压压缩包并把所有文件复制到游戏根目录，双击katakoi.exe运行

# Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-3.5/GPT-4/Newbing/Sakura等大语言模型的Galgame自动化翻译解决方案
- [Yggdrasill-Moe/Niflheim](https://github.com/Yggdrasill-Moe/Niflheim.git) :StudioSeldomAdventureSystem的sec5_pack和sec5_unpack工具
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本

### 注：

SExtractor暴力提取正则(BIN引擎+截断，仅适用于本作，未匹配人名和带特效文本)：
```
00_skip=^[\S\s]{0,2}$
10_search=^([\x20\x81-\xFE][\x00-\xFF][\x1B-\xFF]+?)$
ignoreDecodeError=1
separate=(\xFF\xFF\x1B\x1C\x00\x00\x03\x00\xFF\xFF\x1B\x03\x00\x01\x01\x25\x67\x00\x00\xFF\xFF|\x1b\x1c\x00\x00\x03\x00\xff\xff\x1b\x03\x00\x01\x01\x2b\x6d\x00\x00\xff\xff\x1b\x31|\xFF\xFF\x1B\x03\x00\x01\x01\x25\x67\x00\x00\xFF\xFF|\x1B\x03\x00\x01\x01\x32\x7B\x00\x00\xFF\xFF)
sample=
<暴力匹配，日文仅允许双字节，单字节符号按正则匹配[\r\n]>
```