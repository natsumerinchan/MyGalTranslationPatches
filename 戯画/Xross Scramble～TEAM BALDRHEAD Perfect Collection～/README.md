# Xross Scramble～TEAM BALDRHEAD Perfect Collection～ gemini-2.5-pro 翻译补丁

MD5: `FE5B1B5BB6EEB2A9026068869E35982B`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 注

- 1、已整合免DVD补丁、修正补丁v1.03、Savior特典和BFR的リリィ特典
- 2、BFR只翻译了剧情对话部分

## 更新日志

- 2025.09.16 23:09 首次提交
- 2025.09.24 12:29 添加Savior特典内容（无尽模式和生存模式的时候可以选择变大或者变小）

## 使用方法

- 1、解压压缩包并把所有文件复制到游戏根目录，安装字体后转区运行`XrossScramble.exe`
- 2、游戏内设置字体为`VL ゴシック`

## Credits

- [GalTransl/GalTransl](https://github.com/GalTransl/GalTransl.git) :支持GPT-4/Claude/Deepseek/Sakura等大语言模型的Galgame自动化翻译解决方案
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [GalTools/GalArc](https://github.com/GalTools/GalArc.git) :Galgame解包和打包工具(NEXAS版本2，压缩方式none)
- [Duel Savior Justice Dev Kit](http://tenka.seiha.org/images2019/dsj/DuelSavior_SDK.rar) :英翻补丁作者[Tenka Seiha](https://tenka.seiha.org/)提供的翻译工具包，里面有NEXAS引擎脚本的反编译和重编译工具dstool.exe
- [FunkyFr3sh/cnc-ddraw](https://github.com/FunkyFr3sh/cnc-ddraw.git) :GDI, OpenGL and Direct3D 9 re-implementation of the DirectDraw API for classic 2D games for better compatibility with Windows ME, 2000, XP, Vista, 7, 8, 10, 11, Wine (Linux/macOS/Android) and Virtual Machines
- [补丁测试人员名单](https://github.com/natsumerinchan/MyGalTranslationPatches/issues/5) : [Kanadeforever@Github](https://github.com/Kanadeforever) [Whereis-Alice@Github](https://github.com/Whereis-Alice)

## SExtractor提取正则

### 1、初步提取

#### 1.1、Savior部分

(TXT引擎+cp932编码+不开启JIS替换配置)

```txt
00_skip=^PushB\s+<[A-Z]{1}[0-9]{0,1}_.+?>$
05_skip=^PushB\s+<.+?_.+?>$
06_skip=^PushB\s+<\d+>$
07_skip=^PushB\s+<\w{3,4}\d+>$
08_skip=^PushB\s+<.+?\d{2}[0-9\-]{0,3}[0-9～]{0,3}>$
09_skip=^PushB\s+<.+?\.(bin|mpg)>$
10_search=^PushB\s+<(?P<pre_nameANDmessage>@[@a-z0-9\s]+[（「]{1}+.+?)>$
15_search=^PushB\s+<(?P<pre_nameANDmessage>「.+?)>$
20_search=^PushB\s+<(.+?)>$
JisEncodeName=shift-jis
structure=paragraph
```

#### 1.2、 BFR(BALDR FORCE Re-Action)部分

(BIN引擎+cp932编码+不开启JIS替换配置+免截断)

```txt
01_skip=^[\S\s]{0,3}$
02_skip=^[^@\x81-\xFC]
10_search=^[0-~]*(?P<pre_name>「[ 0-\xFC]+?)$
20_search=^[0-~]*([\x81-\xFC][ 0-\xFC]+?)$
checkJIS=[ 0-~]
ignoreDecodeError=1
postSkip=_.*[^」a-zA-Z]$|[0-9]$
separate=\x00
JisEncodeName=shift-jis
struct=para
sample=
<暴力匹配，日文仅允许双字节，每行结尾限定字符>
```

## 2、二次提取

(JSON引擎+UTF-8编码+开启JIS替换配置)

```txt
10_search=(?P<unfinish>[^@a-zA-Z0-9－/\r\n　_]+)
```
