# Kadenz fermata//Akkord:fortissimo gpt-4.1-2025-04-14 翻译补丁

MD5: `D4E4D93739380FF6096EEF427BA24B0C`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 使用方法
- 1.应用修正补丁v1.04和append
- 2.将压缩包内所有文件解压至游戏根目录，安装压缩包内的VLゴシック_WenQuanYi_cnjp.ttf字体，双击运行KADENZF_CHS.EXE(无需转区)

## DLL源码
https://github.com/natsumerinchan/kadenzf_hook.git

# Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-3.5/GPT-4/Newbing/Sakura等大语言模型的Galgame自动化翻译解决方案
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [cokkeijigen/MesTextTool](https://github.com/cokkeijigen/MesTextTool.git) :CIRCUS引擎*.mes脚本处理工具
- [CFF_Explorer 8.0 汉化版](https://bbs.kanxue.com/thread-158547-1.htm) :PE工具，可用于便捷修改dll导入表

### MesTextTool *.txt SExtractor文本提取正则
(TXT引擎+UTF-8编码+生成JIS替换配置)
```
00_search=^★.+?★@[a-z]\d+(?P<pre_nameANDmessage>「.+?」)$
05_search=^★.+?★@[a-z]\d+(.+?)$
10_search=^★.+?★@l(.+?)\\n@r.+?\\n@s(.+?)\\n(.+)$
15_search=^★.+?★@[a-z](?P<pre_nameANDmessage>「.+?」)$
20_search=^★.+?★@[a-z](.+?)$
25_search=^★.+?★(?P<pre_nameANDmessage>「.+?」)$
30_search=^★.+?★(.+?)$
structure=paragraph
JisEncodeName=shift-jis
```
