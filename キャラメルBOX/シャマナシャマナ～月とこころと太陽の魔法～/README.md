# シャマナシャマナ～月とこころと太陽の魔法～ gemini-2.5-pro-exp-03-25 翻译补丁

MD5: `05B98C6E8C3AE8F4C9F3B29DCF40F936`

作者： natsumerinchan(Github) == 雨宮ゆうこ

未作完整测试，有bug请反馈（截图加私发存档）。

## 使用方法
- 1.解压压缩包并把所有文件复制到游戏根目录，安装字体后转区运行shamana_chs.exe

# Credits

- [GalTransl/GalTransl](https://github.com/GalTransl/GalTransl.git) :支持GPT-4/Claude/Deepseek/Sakura等大语言模型的Galgame自动化翻译解决方案
- [nanami5270/GARbro-Mod](https://github.com/nanami5270/GARbro-Mod.git) :Galgame解包和打包工具(打包时选yks格式)
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [Inori/FuckGalEngine](https://github.com/Inori/FuckGalEngine.git) :galgame破解工具集，使用其中YukaScript引擎的text_export.py和text_import.py(脚本处理)

### SExtractor text_export.py文本提取正则(TXT引擎+UTF-16编码+JIS替换)
```
00_search=^★.+?★(?P<name>ミルディン|ラビ|リース|スノゥ|サラ|パティ|エーファ)$
01_search=^★.+?★(?P<name>ミリア|クム|フレイ|ツバキ|ダウィッズ|帽子|テギッド)$
02_search=^★.+?★(?P<name>声|ボゥロゥ|キネザ|ローエングリン|男|女性の声)$
03_search=^★.+?★(?P<name>ジャスパー|ユウセイ|月|地|女性|男の子|ふたり)$
04_search=^★.+?★(?P<name>初老の男|ケリ|先生|ラウェリン|青年|女の子|女子生徒|一同)$
05_search=^★.+?★(?P<name>男子生徒|少女|ミル|男性|生徒達|少年|女生徒|子犬|僕)$
06_skip=^★.+?★\s+$
10_search=^★.+?★\s+(.+?)$
15_search=^★.+?★(.+?)$
postSkip=^[A-Za-z\[\]【】\%]
structure=paragraph
JisEncodeName=shift-jis
```

### exe中ykc读取顺序修改
用十六进制编辑器(如wxmedit)打开exe,搜索data0,可见一堆data0*.ykc,越往后读取优先级越高
