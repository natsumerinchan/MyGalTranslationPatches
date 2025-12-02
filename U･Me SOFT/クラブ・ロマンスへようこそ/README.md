# クラブ・ロマンスへようこそ gemini-3-pro-preview 翻译补丁

MD5: `AD883D33845E6F24023D61E4971113DE`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 使用方法

- 1.以追加模式安装`初回版(包含千影 夏海 有希)`、`明日香`、`純子`和`みらい`
- 2.解压压缩包并把`Releases`文件夹内所有内容复制到游戏根目录，安装字体后双击运行`ClubRomance_CHS.exe`

## Credits

- [julixian/GalTranslPP](https://github.com/julixian/GalTranslPP.git) :GalTransl的C++实现
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本(使用其中tools/U-MeSoft/PK_pack.py用于打包*.PK)
- [natsumerinchan/CELICA_HOOK](https://github.com/natsumerinchan/CELICA_HOOK.git) :个人写的游戏程序hook工具
- [xupefei/Locale-Emulator](https://github.com/xupefei/Locale-Emulator.git) :转区工具,使用了其中的dll

## U-MeSoft引擎 *.SCR SExtractor文本提取正则

(TXT引擎+cp932编码+JIS替换)

```md
00_skip=^$
01_skip=^"MUS
05_search=^mes\("(?P<name>[^"]+)"
10_search=^savesetex\("([^"]+)"
11_search=^saveset\("([^"]+)"
12_search=^menu\(.*?"([^"]+)"
13_search=^mesname\(.*?"([^"]+)"
15_skip=^[^"]
20_search=^"(.+)\$L"
21_search=^"(?P<unfinish>.+)\\n"
22_search=^"(.+)\\x0"\)\;$
23_search=^"(.+)"\)\;\;$
24_search=^"(.+)"\)\;$
25_search=^"(.+)"\)$
26_search=^"(.+)\\x0"
structure=paragraph
```
