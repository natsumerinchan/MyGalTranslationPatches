# そらをみあげて想うこと gemini-2.5-pro 翻译补丁

MD5: `534C8938E5A74FE22A42B148251E6D28`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 使用方法
- 1.将压缩包内所有文件解压至游戏根目录，双击运行SORAMIA_CHS.EXE

# Credits

- [GalTransl/GalTransl](https://github.com/GalTransl/GalTransl.git) :支持GPT-4/Claude/Deepseek/Sakura等大语言模型的Galgame自动化翻译解决方案
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [julixian/MyVisualNovelTransTools](https://github.com/julixian/MyVisualNovelTransTools) :使用了其中的MarbleMblArchiveTool用于解包和打包mbl(本作Index length为24，无加密)
- [【工具】API HOOK和编码处理工具包](https://www.ai2.moe/topic/29225-【工具】api-hook和编码处理工具包)
- [xupefei/Locale-Emulator](https://github.com/xupefei/Locale-Emulator.git) :转区工具,使用了其中的dll

### Marble引擎 *.S SExtractor文本提取正则
(BIN引擎+cp932编码+生成JIS替换配置+BIN启用纯文本正则模式+不截断)
```
00_search=^\>【(?P<name>.+?)】$
05_search=^(「.+?」)$
10_search=^(?P<name>[^\s].+?)(「.+?」)$
15_search=^\{\(F\d+=\d+\)(.+?)$
20_search=^\{(.+?)$
25_search=^\s+(.+?)$
30_skip=^(\\|\:\d+|\s+|\[\d+\])$
35_search=^(?P<unfinish>.+?)$
separate=\x00
JisEncodeName=shift-jis
postSkip=^[(A-Za-z0-9#▼*\\!@=；;:\{\}>\x01]
structure=paragraph
```
