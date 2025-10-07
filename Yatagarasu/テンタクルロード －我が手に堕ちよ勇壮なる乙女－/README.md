# テンタクルロード －我が手に堕ちよ勇壮なる乙女－ gemini-2.5-pro 翻译补丁

MD5: `6069383309E209B39B89DFD8C69197D7`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 使用方法

- 1.应用修正补丁v1.0.3
- 2.解压压缩包并把所有内容复制到游戏根目录，双击运行`テンタクルロード_CHS.EXE`

## Credits

- [julixian/GalTranslPP](https://github.com/julixian/GalTranslPP.git) :GalTransl的C++实现
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [nanami5270/GARbro-Mod](https://github.com/nanami5270/GARbro-Mod.git) :Galgame解包和打包工具
- [【工具】API HOOK和编码处理工具包](https://www.ai2.moe/topic/29225-【工具】api-hook和编码处理工具包)
- [xupefei/Locale-Emulator](https://github.com/xupefei/Locale-Emulator.git) :转区工具,使用了其中的dll
- 感谢石头门佬[Steins;Gate@御爱同萌](https://www.ai2.moe/profile/12822-steinsgate/)写的Yatagarasu引擎打包脚本，  
之后脚本将会被上传至SExtractor仓库

## Yatagarasu引擎 \*.evt \*.lua SExtractor提取正则

(TXT引擎+cp932编码+JIS替换)

```txt
00_search=^\s{0,}@\[DrawName name = \"(?P<name>.+?)\"\]$
01_search=^\"(.+?)\"\,
02_search=\s{0,}text\=\"(.+?)\"\s{0,}
03_search=\s{0,}ScSetTextWindow\(\s{0,}\"DIALOG\"\,\s{0,}\d+\,\s{0,}\"(.+?)\"\s{0,}\)
04_search=\s{0,}ScSetFlag\(\s{0,}\"T_SelTxt\d+\"\,\s+\"(.+?)\"\s{0,}\)
05_search=\s{0,}ScSetFlag\(\s{0,}\"T_DrawTxt\d+\"\,\s+\"(.+?)\"\s{0,}\)
06_search=\s{0,}ScSetFlag\(\s{0,}\"T_StartText\"\,\s{0,}\"(.+?)\"\s{0,}\)
07_search=\s{0,}drawTxt\s{0,}\=\s{0,}\"(.+?)\"\s{0,}
08_search=lTxt = \"(.+?)\" .. .+? .. \"(.+?)\"
09_search=\s{0,}lTxt = "(.+?)"\s{0,}
10_search=\s{0,}retTxt = "(.+?)"\s{0,}
15_search=txt = \"(.+?)\" .. .+? .. \"(.+?)\"
20_skip=^\s{0,}@
25_skip=^\s+$
30_search=^\s{0,}(.+?)\s{0,}$
postSkip=^[A-Za-z0-9\;\*\<\>\-\t\:\$\&\]\{\}\"\.]
struct=paragraph
```
