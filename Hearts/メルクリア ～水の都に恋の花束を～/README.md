# メルクリア ～水の都に恋の花束を～ gpt-4o-2024-11-20 + DeepSeek-V3-0324 翻译补丁

MD5: `2A5B93300FE6DF811CE230D440E7DAF3`

作者： natsumerinchan(Github) == 雨宮ゆうこ

还未推完，有bug请反馈（截图加发送存档）

## 使用方法
- 1.应用官方免DVD补丁mer_license.zip和win8兼容补丁MercuriaFirstVerPatchForWin8x64.exe(顺序不能乱)
- 2.安装压缩包里的`unifont-all.ttf`字体(该字体是普通字体并非jis替换字体)
- 3.解压压缩包并把所有文件复制到游戏根目录下，然后转区运行あやかしコントラクト.exe(否则会弹窗报错)
- 4.进入游戏后在`文字表示`-`フォント`中将字体改为`Unifont Smooth`

# Credits

- [GalTransl/GalTransl](https://github.com/GalTransl/GalTransl.git) :支持GPT-4/Claude/Deepseek/Sakura等大语言模型的Galgame自动化翻译解决方案
- [arcusmaximus/VNTranslationTools](https://github.com/arcusmaximus/VNTranslationTools.git) :视觉小说翻译工具
- [GalTransl/GalTransl_DumpInjector](https://github.com/GalTransl/GalTransl_DumpInjector.git) :VNTranslationTools及msg-tool的GUI界面
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [XP3Viewer](https://github.com/Inori/FuckGalEngine/blob/master/Krkr/XP3Viewer.rar) :可用于解包或封包被加密以及exe被保护的krkr2引擎游戏

## VNTranslationTools *.ks->*.json SExtractor二次提取正则
(JSON引擎+utf-8编码)
```
05_search=^(?P<name>【.+?】)(?P<msg>.+?)$
10_search=^(?P<msg>.+?)$
structure=paragraph
```

## VNTranslationTools krkr2 漏提内容SExtractor提取正则
(TXT引擎+UTF-16编码)
```
05_search=text="(.+?)"
structure=paragraph
```
