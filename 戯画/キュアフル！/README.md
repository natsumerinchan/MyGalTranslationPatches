# キュアフル！ gemini-2.5-pro 翻译补丁

MD5: `3479FE13C71BF36145AADC68882FB235`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 使用方法
- 1、解压压缩包并把所有文件复制到游戏根目录，双击运行`Curefull_CHS.exe`

# Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-4/Claude/Deepseek/Sakura等大语言模型的Galgame自动化翻译解决方案
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [GalTools/GalArc](https://github.com/GalTools/GalArc.git) :Galgame解包和打包工具(NEXAS版本2，压缩方式none)
- [【工具】API HOOK和编码处理工具包](https://www.ai2.moe/topic/29225-【工具】api-hook和编码处理工具包)
- [xupefei/Locale-Emulator](https://github.com/xupefei/Locale-Emulator.git) :转区工具,使用了其中的dll

# SExtractor提取正则
1、初步提取
(BIN引擎+cp932编码+开启JIS替换配置+免截断)
```
00_search=^(?P<name>悠也|瑞貴|彩香|遥菜|涼音|都|樋口|綾瀬|三杉|？？？|全員|女の子|キャプテン)$
01_search=^(?P<name>野球部員|黒猫|先輩バスケ部員２|学年主任|先輩バスケ部員１|神山|チンピラ)$
02_search=^(?P<name>\x83\x5C\x83\x74\x83\x67\x83\x7B\x81\x5B\x83\x8B\x95\x94\x88\xF5)$
03_search=^(?P<name>母さん|男子|後輩部員１|先生|女子学生１|女子部員１|女子部員２|後輩部員２)$
04_search=^(?P<name>テニス部員|遥菜・涼音・彩香|元チア部員|遥菜以外|悠也・遥菜|店員|アナウンス)$
05_search=^(?P<name>バトミントン部員|元チア部員２|審査員|悠也・涼音|司会|保健委員|涼音父)$
06_search=^(?P<name>悠也＆遥菜|遥菜＆涼音|悠也＆涼音＆遥菜|女子学生２|彩香＆涼音|遥菜＆彩香＆涼音)$
07_search=^(?P<name>男子学生|みんな|悠也＆都|彩香＆都|瑞貴＆樋口|女性|遥菜・瑞貴・涼音・都)$
08_search=^(?P<name>先輩女子|悠也・彩香|テレビ|自分以外|ＴＶ|涼音母)$
09_skip=^[\S\s]{0,3}$
10_skip=^[^@\x81-\xFC]
15_search=^[0-~]*(「[ 0-\xFC]+?)$
20_search=^[0-~]*([\x81-\xFC][ 0-\xFC]+?)$
checkJIS=[ 0-~]
ignoreDecodeError=1
postSkip=_.*[^」a-zA-Z]$|[0-9]$
separate=\x00
struct=para
sample=
<暴力匹配，日文仅允许双字节，每行结尾限定字符>
```

2、二次提取
(JSON引擎+UTF-8编码+不开启JIS替换配置)
```
10_search=(?P<unfinish>[^@a-zA-Z0-9－/\r\n　_]+)
```
