# うそつき王子と悩めるお姫さま –Princess syndrome– gemini-2.5-pro翻译补丁 

MD5: `28B9BB02FC71FC5734E83AB9282DF515`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 使用方法
- 1.解压压缩包并把所有文件复制到游戏根目录，双击运行usomeru_chs.exe

# Credits

- [GalTransl/GalTransl](https://github.com/GalTransl/GalTransl.git) :支持GPT-4/Claude/Deepseek/Sakura等大语言模型的Galgame自动化翻译解决方案
- [detached64/GalArc](https://github.com/detached64/GalArc.git) :Galgame解包和打包工具(取消勾选解密ybn)
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [【工具】API HOOK和编码处理工具包](https://www.ai2.moe/topic/29225-【工具】api-hook和编码处理工具包)
- [xupefei/Locale-Emulator](https://github.com/xupefei/Locale-Emulator.git) :转区工具,使用了其中的dll


## YU-RIS引擎*.ybn SExtractor提取正则(改编默认的None规则)
(Yuris引擎+cp932编码+JIS替换)
```
00_skip=^M[\S\s]{2}"(?=[^\x81-\xEF]|■|◆)
01_skip=^[A-Za-z0-9]+$
05_search=^(?P<name>【.+?】)$
10_search=^M[\S\s]{2}"(.+?)"
15_skip=^[A-Z][\x00-\xFF][\x00-\x04]
20_search=^(?P<name>【.+?】)(?P<end_unfinish>「.+」)$
21_search=^(?P<end_unfinish>.+」)$
22_search=^(?P<name>【.+?】)(?P<start_unfinish>「.+)$
23_search=^(?P<name>【.+?】)(?P<end_unfinish>（.+）)$
24_search=^(?P<end_unfinish>.+）)$
25_search=^(?P<name>【.+?】)(?P<start_unfinish>（.+)$
26_search=^(?P<name>【.+?】)(?P<end_unfinish>『.+』)$
27_search=^(?P<end_unfinish>.+』)$
28_search=^(?P<name>【.+?】)(?P<start_unfinish>『.+)$
30_search=^(.+)$
decrypt=\xF2\x79\xB0\xE5
extraData=9
struct=paragraph
```
