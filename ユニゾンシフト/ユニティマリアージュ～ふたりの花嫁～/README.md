# ユニティマリアージュ～ふたりの花嫁～ claude-3.7-sonnet(openrouter) 翻译补丁

MD5: `3918D6454842213A413B59C6B8482910`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 使用方法

- 1.应用修正补丁v1.1
- 2.将压缩包内所有文件解压至游戏根目录，双击运行unity_CHS.exe(GBK编码无需转区)

## 更新日志

- 2025.05.03 17:54 初始提交
- 2025.05.03 23:04 整合免DVD补丁
- 2025.05.04 10:02 修复空格导致的闪退或乱码
- 2025.05.04 16:24 修复空格导致的闪退或乱码(2)

# Credits

- [nanami5270/GARbro-Mod](https://github.com/nanami5270/GARbro-Mod.git) :Galgame解包和打包工具
- [GalTransl/GalTransl](https://github.com/GalTransl/GalTransl.git) :支持GPT-4/Claude/Deepseek/Sakura等大语言模型的Galgame自动化翻译解决方案
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [YIWANG-sketch/Galgame_automation_processing_tool](https://github.com/YIWANG-sketch/Galgame_automation_processing_tool.git) :使用了其中Softpal引擎的功能
- [CFF_Explorer 8.0 汉化版](https://bbs.kanxue.com/thread-158547-1.htm) :PE工具，可用于便捷修改dll导入表

SExtractor Galgame_automation_processing_tool text.txt二次提取正则
(TXT引擎+UTF-16编码+不生成JIS替换配置)

```
00_search=^●.+?●<.+?>(?P<pre_nameANDmessage>「.+」)$
05_search=^●.+?●(?P<pre_nameANDmessage>「.+」)$
10_search=^●.+?●(?P<name>あらた)$
15_search=^●.+?●(?P<pre_nameANDmessage>（.+）)$
20_search=^●.+?●<.+?>(.+)$
25_search=^●.+?●(.+)-.+?-$
30_search=^●.+?●(.+)$
structure=paragraph
```

SExtractor text.txt.json 二次提取正则
(JSON引擎+UTF-8编码+不生成JIS替换配置)
```
10_search=(?P<unfinish>[^%<>@a-zA-Z0-9－/\r\n]+)
```

## 翻译过程
- 1、Galgame_automation_processing_tool(简称GAPT)可以自动导出[{name,msgRN}]格式的json，但我发现有不少内容被漏提，<br>
故我还是自己用SExtractor写正则提取文本(回封TEXT.DAT时一路回车直到让你选择编码时把翻译好的text.txt扔进文件夹再选编码)
- 2、GAPT还可以自动对exe和PAL.dll进行修改使其支持GBK及其编码范围，但它不支持本游戏的exe，<br>
故本游戏需要手动用x32dbg搜CreateFontIndirectA把两处的icharset从0x80改为0x86，不过好在本游戏的exe中<br>
没有字符边界检查范围，改起来比较方便。之后用CFF_Explorer在导入目录中重命名PAL.DLL为PAL_CHS(总之改为新dll的名字)
- 3、本游戏的引擎免封包但不免加密，需要用GAPT的1-4功能对TEXT.DAT重新加密(解包data.pac时GARbro会自动进行解密)
