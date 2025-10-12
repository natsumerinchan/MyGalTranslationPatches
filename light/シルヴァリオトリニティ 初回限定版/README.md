# シルヴァリオトリニティ 初回限定版 gemini-2.5-pro翻译补丁

MD5: `B15B969728F66D908D9A6653F9A9A6CF`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 使用方法
- 1.依次应用初回特典、演出强化补丁、修正补丁v1.2(每次应用补丁都要覆盖一次免DVD补丁(压缩包内的malie.exe和kDays.dll)运行一次游戏)
- 2.解压压缩包并把所有文件复制到游戏根目录，双击运行malie_chs.exe

## 更新日志
- 2025.08.12 20:44 首次提交

# Credits

- [GalTransl/GalTransl](https://github.com/GalTransl/GalTransl.git) :支持GPT-4/Claude/Deepseek/Sakura等大语言模型的Galgame自动化翻译解决方案
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本(malie引擎dat打包工具在tools\malie文件夹内)
- [nanami5270/Malie_Script_Tool](https://github.com/nanami5270/Malie_Script_Tool.git) :FreeMalie Engine Script Disassembler
- [【工具】API HOOK和编码处理工具包](https://www.ai2.moe/topic/29225-【工具】api-hook和编码处理工具包)

### malie引擎 SExtractor文本提取正则(仅适用于本作)
需提前删除符合正则`^◇.+?◇.+$`以及`^\n$`的行
(TXT引擎+utf-8编码+不生成JIS替换配置)
```
00_skip=^(\[9\]|\[6\]|\[n\]|\[4\])
05_skip=^(.[A-Za-z0-9]+|◆|\s+)$
10_search=^\s+\{v_.+?\}(?P<end_unfinish>.+?」)$
15_search=^\{v_.+?\}(?P<end_unfinish>.+?」)$
20_search=^\s+(?P<end_unfinish>.+?」)$
25_search=^(?P<end_unfinish>.+?」)$
30_search=^\s+(?P<end_unfinish>」)$
35_search=^(?P<end_unfinish>」)$
40_search=^\s+\{v_.+?\}(「.+?」)$
45_search=^\s+\{v_.+?\}(?P<start_unfinish>「.+?)$
50_search=^\s+\{v_.+?\}(.+?)$
55_search=^\{v_.+?\}(「.+?」)$
60_search=^\{v_.+?\}(?P<start_unfinish>「.+?)$
65_search=^\{v_.+?\}(.+?)$
70_search=^\s+(「.+?」)$
75_search=^\s+(?P<start_unfinish>「.+?)$
80_search=^\s+(.+?)$
85_search=^(「.+?」)$
90_search=^(?P<start_unfinish>「.+?)$
95_search=^(?P<name>アッシュ|アヤ|ミステル|レイン|アリス|グレイ|ケルベロス|ギルベルト|ムラサメ|ヘリオス|ヴァネッサ|シズル|ガラハッド|ティセ|ティナ|ダインスレイフ|リン|レイン？|アヤ？|ミステル？|ミステル？？|アッシュ＆レイン|ケルベロス？|グレイ？|ティナ＆ティセ|帝国兵|ダインスレイフ？|ガラハッド？|第十三小隊員|聖教国兵|アッシュたち|アッシュ達|ギルベルト？|聖教国兵士|レイン＆ミステル|アッシュ＆グレイ|三人|ガラハッド？？|アッシュ＆アヤ|客Ａ|客Ｂ|ヘリオス？|レイン？？|？|煌翼＆冥狼|傀儡兵|師弟|小悪魔たち|二人|天駆翔＆銀悠冥狼|レイン＆アヤ)$
100_search=^(.+?)$
skipIgnoreUnfinish=true
pureText=1
separate=(\x0D\x0A|◆|\[9\]\[6\]\[n\]\[n\]|\[9\]\[6\]\[n\]|\[9\]\[6\]|\[6\]\[n\]\[n\]|\[6\]\[n\]|\[4\]|\[6\]|\[9\])
structure=paragraph
```

