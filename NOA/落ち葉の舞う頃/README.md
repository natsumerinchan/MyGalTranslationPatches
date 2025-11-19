# 落ち葉の舞う頃 gemini-3-pro-preview 翻译补丁

MD5: `2D24CCEF397FFDE3C046404B2EA5E592`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 使用方法

- 1.应用修正补丁`ocb01.exe`
- 2.解压压缩包并把`Releases`文件夹内所有文件复制到游戏根目录，双击运行`ocb_chs.exe`

## Credits

- [julixian/GalTranslPP](https://github.com/julixian/GalTranslPP.git) :GalTransl的C++实现
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [julixian/MyVisualNovelTransTools](https://github.com/julixian/MyVisualNovelTransTools.git) :`IvoryTool`中的  
`IvoryCryptTool`用于加解密`*.OCB`脚本,`IvoryPkArchiveTool`用于解包和打包`*.pk`,`IvoryScriptSimpleTool`用于提取和导入文本
- [natsumerinchan/CELICA_HOOK](https://github.com/natsumerinchan/CELICA_HOOK.git) :个人写的游戏程序hook工具
- [xupefei/Locale-Emulator](https://github.com/xupefei/Locale-Emulator.git) :转区工具,使用了其中的dll

## ivory引擎 IvoryScriptSimpleTool *.txt SExtractor提取正则

(TXT引擎+CP932编码+JIS替换)

```md
00_search=^[A-Z0-9]{8}[:]{5}\<sp\>(.+?)$
05_search=^[A-Z0-9]{8}[:]{5}\<name\>(?P<name>.+?)$
10_search=^[A-Z0-9]{8}[:]{5}(.+?)$
structure=paragraph
```
