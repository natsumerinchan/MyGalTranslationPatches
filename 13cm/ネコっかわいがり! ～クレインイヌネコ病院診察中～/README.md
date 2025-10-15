# ネコっかわいがり! ～クレインイヌネコ病院診察中～ gemini-2.5-pro 翻译补丁

MD5: `74EC3A82739817891E356D264BBF83AA`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 使用方法

- 1.解压压缩包并把所有文件复制到游戏根目录，双击运行REALLIVE.exe

## Credits

- [julixian/GalTranslPP](https://github.com/julixian/GalTranslPP.git) :GalTransl的C++实现
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本(tools文件夹有Reallive引擎相关工具和教程)
- [AtomCrafty/UniversalInjectorFramework](https://github.com/AtomCrafty/UniversalInjectorFramework.git) :实现更改字体，jis映射
- [xupefei/Locale-Emulator](https://github.com/xupefei/Locale-Emulator.git) :转区工具,使用了其中的dll
- 补丁测试人员： [伪恶君子333@御爱同萌](https://www.ai2.moe/profile/9569-伪恶君子333/)

## 本作使用的提取正则(改编自SE自带的REALLIVE引擎_None规则)

(Reallive引擎+cp932编码+JIS替换)

```txt
00_skip=^\s*$
01_skip=^【　】$
10_search=^【(?P<name>.+?)】([\S\s]+)$
20_search=^([\S\s]+?)$
extraData=fixNote,checkPos


<decrypt处理二次加密，值是GameType，配置在tools/RealLive/seen_fix.py里>
<fixNote,fixLinebreak分别处理掉原有注音和换行，换行默认会换为<n>，译文中允许额外增加换行>
<仅针对arc_conv解包后的txt>
<version=1 可选1,2,3,4,5>
```
