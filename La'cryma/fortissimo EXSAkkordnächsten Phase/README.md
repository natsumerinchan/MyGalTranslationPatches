# fortissimo//Akkord:Bsusvier claude-3.7-sonnet(openrouter) 翻译补丁

MD5: `BF94B9B8ED18C0CE92165A280C1A73B3`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 使用方法
- 1.解压压缩包并把所有文件复制到游戏根目录，双击fortissimo_exs_cn.exe运行(GBK编码无需转区)
- 2.标题栏右键菜单可以修改字体(默认字体为WenQuanYi Micro Hei)

# Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-3.5/GPT-4/Newbing/Sakura等大语言模型的Galgame自动化翻译解决方案
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [cokkeijigen/MesTextTool](https://github.com/cokkeijigen/MesTextTool.git) :CIRCUS引擎*.mes脚本处理工具
- [cokkeijigen/DC_CN_PATCH](https://github.com/cokkeijigen/DC_CN_PATCH/tree/test) :CIRCUS引擎汉化hook补丁
- [CFF_Explorer 8.0 汉化版](https://bbs.kanxue.com/thread-158547-1.htm) :PE工具，可用于便捷修改dll导入表

# 特别鸣谢
感谢github@cokkeijigen佬对MesTextTool旧版本引擎bug的修复及其制作的汉化hook补丁

### MesTextTool *.txt SExtractor文本提取正则
(TXT引擎+UTF-8编码+不生成JIS替换配置)
```
00_search=^★◎.+?◎★@l(?P<pre_nameANDmsg>「.+」)$
01_search=^★◎.+?◎★(?P<pre_nameANDmsg>「.+」)$
02_search=^★◎.+?◎★　\\n　\\n　\\n　\\n　\\n　\\n　\\n(?P<name>[^\\n].+?)\\n(「.+」)$
03_search=^★◎.+?◎★　\\n　\\n　\\n　\\n　\\n　\\n　\\n(.+)$
04_search=^★◎.+?◎★　\\n　(?P<name>.+?)\\n(「.+」)$
05_search=^★◎.+?◎★　(?P<name>.+?)\\n(「.+」)$
06_search=^★◎.+?◎★(?P<name>[^\\n].+?)\\n(「.+」)$
07_search=^★◎.+?◎★　\\n(.+)$
08_search=^★◎.+?◎★@s(.+)$
09_search=^★◎.+?◎★(.+)$
structure=paragraph
```
