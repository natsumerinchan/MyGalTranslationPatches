# ラブレプリカ gemini-2.5-pro 翻译补丁

MD5: `9027867DC17DEFCEA3A356028212E416`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 使用方法
- 1.将压缩包内所有文件解压至游戏根目录，双击运行SiglusEngine_CHS.exe

# Credits

- [GalTransl/GalTransl](https://github.com/GalTransl/GalTransl.git) :支持GPT-4/Claude/Deepseek/Sakura等大语言模型的Galgame自动化翻译解决方案
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [amayra/arc_conv](https://github.com/amayra/arc_conv.git) :由 w8m 以纯 ASM 编写的命令行视觉小说工具包
- [yanhua0518/GALgameScriptTools](https://github.com/yanhua0518/GALgameScriptTools.git) :SiglusEngine解包和打包工具
- [xmoezzz/SiglusExtract](https://github.com/xmoezzz/SiglusExtract.git) :使用了其中Universal Patch的功能，以解决修正中文显示间距，实现中日文版本共存
- [【工具】API HOOK和编码处理工具包](https://www.ai2.moe/topic/29225-【工具】api-hook和编码处理工具包)
- [[Gal汉化入门]#6 SiglusEngine汉化教程](https://www.bilibili.com/read/cv13305423)

### SiglusExtract *.txt SExtractor文本提取正则(仅适用于本作)
(TXT引擎+utf-8编码+不生成jis替换配置)
```
00_search=^●.+?●(?P<message>「.+?」)$
05_search=^●.+?●(?P<end_unfinish>.+?」)$
10_search=^●.+?●(?P<start_unfinish>「.+?)$
15_skip=^●.+?●(\<ruby\>.+?)$
20_search=^●.+?●(?P<name>沢人|みずほ|鈴|藍|咲子|怜|千佳|影士|鴻|女神|影幹|エリザベス|？？？＠藍|マリア|千佳＠千佳１ｓｔ|亜透父|？？？＠鈴|女の子Ｂ|？？？＠みずほ|女の子Ａ|女の子Ｃ|男の子Ａ|誠谷学園の教師|坊っちゃん９|文化祭司会|執事＠影幹|マジシャン|藍那|ご近所のおばさん|エリザベス＠影士|店員|坊っちゃま９|女子生徒２|？？？＠千佳|メイド|男子生徒１|先生|バッグ＠千佳|おっぱい＠怜|坊っちゃま８|ギターを持った女性|カフェ店員|ご近所のおばちゃん|女子生徒１|沢人にナンパされた女生徒|すると藍が|エリザベス＠影幹|左の藍|右の藍|？？？＠エリザベス|全員|千佳・沢人|？？？＠怜|坊っちゃま１|坊っちゃま５|女の子|お母さん|？？？＠影幹|？？？＠影士|おばさん|ファミレス店員|？？？＠藍那|？？？＠咲子|女子生徒３)$
25_search=^●.+?●(?P<end_unfinish>.+?[。|？|！])$
30_search=^●.+?●(?P<unfinish>.+?)$
postSkip=^[A-Za-z0-9＊]
skipIgnoreUnfinish=true
structure=paragraph
```
