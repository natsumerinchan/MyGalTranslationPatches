# しこたまスレイブ －あるじで姉妹な天使と悪魔－ claude-3.7-sonnet(openrouter) 翻译补丁

MD5: `ABEC90B74DE2130AB034963B02DA1199`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 使用方法

- 1.将压缩包内所有文件解压至游戏根目录，双击运行shikotama_CHS.exe(无需手动转区，字体可不安装)

# Credits

- [GalTransl/GalTransl](https://github.com/GalTransl/GalTransl.git) :支持GPT-4/Claude/Deepseek/Sakura等大语言模型的Galgame自动化翻译解决方案
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [arcusmaximus/VNTranslationTools](https://github.com/arcusmaximus/VNTranslationTools.git) :视觉小说翻译工具
- [CFF_Explorer 8.0 汉化版](https://bbs.kanxue.com/thread-158547-1.htm) :PE工具，可用于便捷修改dll导入表
- [【工具】API HOOK和编码处理工具包](https://www.ai2.moe/topic/29225-【工具】api-hook和编码处理工具包)

VNTranslationTools SoftPal引擎文本提取回封命令
(将SCRIPT.SRC TEXT.DAT POINT.DAT放在同一文件夹，POINT.DAT仅用于提取回封不要放进补丁)

```
提取：
vntextpatch extractlocal .\SCRIPT.SRC .\script.json

回封:
VNTextPatch insertlocal .\SCRIPT.SRC .\json\new\script.json .\out\SCRIPT.SRC
```

SExtractor script.json二次提取正则
(JSON引擎+UTF-8编码+生成JIS替换配置)

```
10_search=(?P<unfinish>[^%<>@a-zA-Z0-9－/\r\n]+)
JisEncodeName=shift-jis
```
