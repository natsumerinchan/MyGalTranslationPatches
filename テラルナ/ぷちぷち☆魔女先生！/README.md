# ぷちぷち☆魔女先生！ gemini-2.5-pro 翻译补丁

MD5: `4A169BB27F327FBEF3653ADC2C3BD665`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 使用方法
- 1.将压缩包内所有文件解压至游戏根目录，双击运行PUCHI_CHS.EXE(用了GBK编码请勿转区)

# Credits

- [GalTransl/GalTransl](https://github.com/GalTransl/GalTransl.git) :支持GPT-4/Claude/Deepseek/Sakura等大语言模型的Galgame自动化翻译解决方案
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [julixian/MyVisualNovelTransTools](https://github.com/julixian/MyVisualNovelTransTools) :使用了其中的MarbleMblArchiveTool用于解包和打包mbl(本作Index length为24，无加密)
- [【工具】API HOOK和编码处理工具包](https://www.ai2.moe/topic/29225-【工具】api-hook和编码处理工具包)

### Marble引擎 *.S SExtractor文本提取正则
(BIN引擎+cp932->gbk编码+BIN启用纯文本正则模式+不截断)
```
00_search=^\>(?P<name>【.+?】)$
05_search=^\@title\x20(.+?)$
10_search=^(?P<predel_unfinish>「.+?」)$
15_search=^(?P<name>[^\s].+?)(「.+?」)$
20_search=^\{\(\w\d.+?\)(?P<predel_unfinish>.+?)$
25_search=^\{(?P<predel_unfinish>.+?)$
30_search=^\s+(.+?)$
35_skip=^(\\|\:\d+|\s+|\[\d+\])$
40_search=^(?P<unfinish>.+?)$
separate=\x00
postSkip=^[(A-Za-z0-9#▼*\\!@=；;:\{\}>\x01\x1A]
structure=paragraph
```
