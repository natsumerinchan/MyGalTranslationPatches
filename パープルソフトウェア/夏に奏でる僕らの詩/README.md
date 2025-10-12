# 夏に奏でる僕らの詩 gpt-4o-2024-11-20 翻译补丁 v1.0.0

MD5: 06A5681CAABC24796E5F1F345EC4AB02`

作者： natsumerinchan(Github) == 雨宮ゆうこ

未作完整测试，有bug请反馈（截图加私发存档）

## 使用方法
- 1.安装修正补丁v1.02
- 2.解压压缩包并把所有文件复制到游戏根目录，安装字体后转区运行cmvs32_gpt4o.exe

# Credits

- [GalTransl/GalTransl](https://github.com/GalTransl/GalTransl.git) :支持GPT-4/Claude/Deepseek/Sakura等大语言模型的Galgame自动化翻译解决方案
- [amayra/arc_conv](https://github.com/amayra/arc_conv.git) :由 w8m 使用纯 ASM 编写的命令行视觉小说工具包
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [ZQF-ReVN/RxCMVS](https://github.com/ZQF-ReVN/RxCMVS.git) :CMVS引擎脚本处理(用最新版)、hook工具(git reset --hard到4c9f2874c65c702e47e109e38ea91a060c953c3c并编辑CMVSVersion.h改为使用对应游戏的配置)

### PS3_TextEditor json SExtractor文本提取正则(TXT引擎+UTF-8-SIG编码+JIS替换)
(由于CMVS引擎的人名在对话的后面，不得已手动指定人名)
```
05_search=^\s\s*"tra":\s*"(?P<name>歌音|声|真夏|ほのか|果歩|優佳|なるみ|佐竹|大吾|女の子|はるか|英語教師)"$
06_search=^\s\s*"tra":\s*"(?P<name>女子|遥|人魚|少女|遥＆なるみ|女子２|男子１|女子３|男子２|男子３|女子１)"$
07_search=^\s\s*"tra":\s*"(?P<name>女子４|二人|四人|みんな|遥＆歌音|遥＆優佳|全員|三人|男１|男２|男３|男４)"$
08_search=^\s\s*"tra":\s*"(?P<name>遥＆真夏|老人１|老人２|老人３|老人４|男たち|遥＆佐竹|老女１|老女２)"$
09_search=^\s\s*"tra":\s*"(?P<name>老人たち|係員|遥＆果歩|男|実行委員|観客１|観客２|観客３|警備員|看護師)"$
10_search=^\s\s*"tra":\s*"(?P<name>草葉の陰|希紗|結城|司会者|子供|見張り１|見張り２|見張り３|見張り４)"$
11_search=^\s\s*"tra":\s*"(?P<name>狂犬達|女の子１|女の子２|九重遥様|歌音＆遥|上月|遥＆ほのか|たえちゃん)"$
12_search=^\s\s*"tra":\s*"(?P<name>女子５|女子６|女子二人)"$
13_search=^\s\s*"tra":\s*"(?P<msg>.+)"$

structure=paragraph
```

### arc_conv .cpz(cpz5) 解包命令（其它版本用garbro解包）
```
.\arc_conv.exe --dest .\script --unpack cpz5 .\script.cpz
.\arc_conv.exe --dest .\update --unpack cpz5 .\update.cpz
```