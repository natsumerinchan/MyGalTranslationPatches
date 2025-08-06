# DUEL SAVIOR JUSTICE gemini-2.5-pro 翻译补丁

MD5: `96B18C4100C613E01AEBB764049EEDE5`

作者： natsumerinchan(Github) == 雨宮ゆうこ

目前仅通关了未亚线和后宫真结局，有bug请反馈（截图加私发存档）

## 使用方法
- 1、应用修正补丁v1.13和官方免DRM验证更新
- 2、解压压缩包并把所有文件复制到游戏根目录，双击运行DuelSavior_CHS.exe

# Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-4/Claude/Deepseek/Sakura等大语言模型的Galgame自动化翻译解决方案
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [GalTools/GalArc](https://github.com/GalTools/GalArc.git) :Galgame解包和打包工具(NEXAS版本2，压缩方式3-Zlib)
- [【工具】API HOOK和编码处理工具包](https://www.ai2.moe/topic/29225-【工具】api-hook和编码处理工具包)
- [xupefei/Locale-Emulator](https://github.com/xupefei/Locale-Emulator.git) :转区工具,使用了其中的dll

# SExtractor提取正则
1、初步提取
(BIN引擎+cp932编码+JIS替换配置，旧版NEXAS需开启截断)
```
00_skip=^[\S\s]{0,3}$
01_skip=^[^@\x81-\xFC]
02_search=^(?P<name>大河|リリィ|未亜|ベリオ|カエデ|リコ|学園長|ナナシ|ダウニ\x81\x5B|セル|ダリア)$
03_search=^(?P<name>クレア|ブラックパピヨン|イムニティ|ルビナス|ロベリア|？？？|シェザル|ムドウ)$
04_search=^(?P<name>ゾンビ娘|村長|女の子|露店の男|市民１|指揮官|市民２|議員１|議長|一同|アンデッド１)$
05_search=^(?P<name>侍従長|薬局の男|副官|トレイタ\x81\x5B|アンデッド２|議員２|料理長|アンデッド３|兵士)$
06_search=^(?P<name>少女|影３|チンピラ３|ガ\x81\x5Bゴイル|老女|死体の少女|女の子１|モンスタ\x81\x5B|モンスタ\x81\x5B１|大河＆ベリオ|リリィ＆ベリオ|大河＆未亜|生徒|議員４|議員５|リコ＆イムニティ|アンデッドたち)$
07_search=^(?P<name>部隊長１|女の子２|影４|男子学生|部下|学生１|チンピラ１|モンスタ\x81\x5B２|議員３)$
08_search=^(?P<name>市民|チンピラ２|触手モンスタ\x81\x5B|リア|影１|民衆１|職員|隊員１|クレアの部下)$
09_search=^(?P<name>学生２|学生３|全員|民衆男Ａ|民衆男Ｃ|上級生２|青年|大地|部隊長２|民衆男Ｂ|上級生１)$
10_search=^(?P<name>上級生５|難民１|リアの母|モンスタ\x81\x5B３|学生４|ゴ\x81\x5Bレム|上級生３)$
11_search=^(?P<name>上級生４|子供|民衆２|民衆３|母親|大輝|敗残兵|カエデ・リコ|影２|難民２|農民１)$
12_search=^(?P<name>農民２|警備兵１|民衆男Ｄ|民衆女Ａ|老人|兵士２|民衆４|ウェイトレス|雄大|大聖|生徒３)$
13_search=^(?P<name>市民３|市民４|子供１|子供２|副官２|大河＆リリィ|近衛兵１|先生|民衆女Ｂ|生徒２)$
14_search=^(?P<name>ベリオ・ナナシ・カエデ|カエデ・ベリオ・リコ|難民３|農民３|店長|看護婦|警備兵２)$
15_search=^(?P<name>屋台のおばさん|民衆５|おさげの女の子|市民５|学生たち|リリィ＆大河|キマイラ|女学生１)$
16_search=^(?P<name>医者|兵士１|観衆１|観衆２|軍勢|魔物|リアの父|オペレ\x81\x5Bタ\x81\x5B|大雅|街の住人１|セル＆大河|トイレの住人|ゾンビ)$
17_search=^(?P<name>街の住人２|ベリオ＆カエデ|女の子Ａ|女の子Ｂ|民衆|部隊長３|部隊長４|学生５|学生６)$
18_search=^(?P<name>学生７|学生８|学生９|近衛兵２|近衛兵３|住民１|住民２|住民３|住民４|売り子|生徒１)$
19_search=^(?P<name>観衆１（民衆男Ａ）|観衆２（民衆男Ｂ）|ベリオ＆セル|ベリオ＆大河|大河＆セル)$
20_search=^[0-~]*\s+([ 0-\xFC]+?)$
25_search=^[0-~]*([ 0-\xFC]+?)$
30_search=^[0-~]*\s+([\x81-\xFC][ 0-\xFC]+?)$
35_search=^[0-~]*([\x81-\xFC][ 0-\xFC]+?)$
checkJIS=[ 0-~]
ignoreDecodeError=1
postSkip=_.*[^」a-zA-Z]$|[0-9]$
separate=\x00
structure=paragraph
sample=
<暴力匹配，日文仅允许双字节，每行结尾限定字符>
```

2、二次提取(JSON引擎)
```
10_search=(?P<unfinish>[^<>@a-zA-Z0-9－/\r\n]+)
```
