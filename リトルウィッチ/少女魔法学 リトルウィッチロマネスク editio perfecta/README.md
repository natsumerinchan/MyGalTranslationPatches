# 少女魔法学 リトルウィッチロマネスク editio perfecta gpt-4.1-2025-04-14+DeepSeek-V3-0324 翻译补丁

MD5: `5BC93BF3BD134902F6E2259B13B52C46`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 使用方法
- 1.安装压缩包内字体VLゴシック_WenQuanYi_cnjp.ttf
- 2.解压压缩包并把所有文件复制到游戏根目录，转区运行ロマネスク ep_CHS.exe

# Credits

- [GalTransl/GalTransl](https://github.com/GalTransl/GalTransl.git) :支持GPT-4/Claude/Deepseek/Sakura等大语言模型的Galgame自动化翻译解决方案
- [amayra/arc_conv](https://github.com/amayra/arc_conv.git) :由 w8m 以纯 ASM 编写的命令行视觉小说工具包
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [Enigma Virtual Box](https://enigmaprotector.com/assets/files/enigmavb.exe) :把脚本文件打包进exe

### FFDSystem *.txt SExtractor文本提取正则

(TXT引擎+932编码+不生成JIS替换配置因为这里已经用API HOOK生成了jis替换后的json)

```
00_skip=^\\
05_search=^(?P<unfinish>.+)$
postSkip=^[*\{#\s@\-\/a-z\}]
structure=paragraph
```

### FFDSystem arc_conv 解包和封包命令

```
解包：
arc_conv --list .\repipack.txt
（repipack.txt在arc_conv文件夹根目录有）

封包：
arc_conv --pack repipack .\xx .\xx.dat [1|2a|2|3|4|5] {key|key_index}
本作为：
arc_conv --pack repipack .\Message .\Message.dat 5 9
封包版本和key_index请自行穷举摸索，我也没搜到如何获取,
只知2002年的《白詰草話番外編 『津名川さん家のクリスマス』》是版本2；2008年的本作，2009年的《聖剣のフェアリース》，
2010年的《シュガーコートフリークス》及2012年的《英雄＊戦姫》是版本5。
```

### FFDSystem 改用系统字体
解包System.dat，用shift_jis编码打开并编辑font.def

### 注
本作人名未作翻译
