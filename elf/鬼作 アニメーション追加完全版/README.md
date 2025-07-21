# 鬼作 アニメーション追加完全版 claude-3-5-sonnet-20241022 翻译补丁

MD5: `AA877A0467E192B8E1BF8D9F979BB72E`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 使用方法
- 1.解压压缩包并把所有文件复制到游戏根目录，双击运行AI6WIN_CHS.exe

# Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-3.5/GPT-4/Newbing/Sakura等大语言模型的Galgame自动化翻译解决方案
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [TesterTesterov/AI6WINScriptTool](https://github.com/TesterTesterov/AI6WINScriptTool.git) :AI6WIN引擎脚本工具(需让AI给ai6wincmd.py添加批处理功能，已放仓库内)
- [TesterTesterov/AI6WINArcTool](https://github.com/TesterTesterov/AI6WINArcTool.git) :AI6WIN引擎解包和打包工具
- [【工具】API HOOK和编码处理工具包](https://www.ai2.moe/topic/29225-【工具】api-hook和编码处理工具包)
- [xupefei/Locale-Emulator](https://github.com/xupefei/Locale-Emulator.git) :转区工具,使用了其中的dll

### AI6WINScriptTool *.txt SExtractor文本提取正则
(TXT引擎+cp932编码+JIS替换)
```
00_search=^\["［(?P<name>.+?)］：(.+?)"\]$
05_search=^\["［(?P<name>.+?)］："\]$
10_search=^\["］：(.+?)"\]$
15_search=^\["\s+(.+?)\r"\]$
20_search=^\["(.+?)\r"\]$
25_search=^\["\s+(.+?)"\]$
30_search=^\["(.+?)"\]$
postSkip=^[A-Za-z*\-［］0-9]
structure=paragraph
```
