# ピリオド claude-3-5-sonnet-20240620 翻译补丁

MD5: `234887433DACE34AC93D386DFBF16EAB`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 使用方法
- 1.应用ExtraUpdate特典追加补丁和修正补丁v1.1(要按顺序安装)
- 2.安装压缩包内VLゴシック_WenQuanYi_cnjp.ttf
- 3.解压压缩包并把所有文件复制到游戏根目录，转区运行ピリオド_CHS.exe

## 更新日志
- 2025.05.14 23:14 首次提交

# Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-3.5/GPT-4/Newbing/Sakura等大语言模型的Galgame自动化翻译解决方案
- [amayra/arc_conv](https://github.com/amayra/arc_conv.git) :由 w8m 以纯 ASM 编写的命令行视觉小说工具包
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [Enigma Virtual Box](https://enigmaprotector.com/assets/files/enigmavb.exe) :把脚本文件打包进exe

### FFDSystem *.txt SExtractor文本提取正则

(TXT引擎+932编码+不生成JIS替换配置因为这里已经用API HOOK生成了jis替换后的json)

```
00_skip=^\\
05_search=^(?P<predel_unfinish>「.+」)$
10_search=^@log_text\stext="(.+?)"$
15_search=^-case text="(.+?)"
20_search=^\s(?P<unfinish>.+)$
25_skip=^\s
30_search=^(?P<unfinish>.+)$
postSkip=^[*\)\{#@\-\/A-Za-z\}\t]
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
arc_conv --pack repipack .\Message .\Message.dat 5 8
封包版本和key_index请自行穷举摸索，我也没搜到如何获取,
只知2002年的《白詰草話番外編 『津名川さん家のクリスマス』》是版本2；2007年的本作，
2008年的《少女魔法学リトルウィッチロマネスク editio perfecta》，
2009年的《聖剣のフェアリース》，2010年的《シュガーコートフリークス》及2012年的《英雄＊戦姫》是版本5。

```

### png人名和png文本处理
本引擎的人名是以png格式图片存在的(位于Message.dat和Log.dat)，直接在脚本修改-message id会报错，<br>
开场部分的文本也以png图片的形式存在(位于Back.dat)，脚本中更改译文只在log中显示，须两处都修改。

仓库里(见シュガーコートフリークス)tools文件夹的msg2png用于生成png文本，name2png用于生成png人名(两者区别在于name2png限制了图高度为45)，<br>
可用以下powershell命令在当前文件夹生成png文件名列表input.txt
```
Get-ChildItem -Filter *.png | Select-Object -ExpandProperty BaseName | Out-File input.txt -Encoding UTF8
```

需安装`pillow`依赖
```
pip install pillow
```

### FFDSystem 改用系统字体
解包System.dat，用shift_jis编码打开并编辑font.def
