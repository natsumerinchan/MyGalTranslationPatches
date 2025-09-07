# 姫様限定！～Princess Limited～ gemini-2.5-pro 翻译补丁

MD5: `4F53414A6EBEBC40914270EB63AB4CF0`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 使用方法
- 1、将压缩包内所有文件解压至游戏根目录，安装压缩包内字体后双击运行`姫様限定！_CHS.exe`
- 2、游戏内修改字体为`VL ゴシック`

# Credits

- [julixian/GalTranslPP](https://github.com/julixian/GalTranslPP.git) :GalTransl的C++实现
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [Lasriel/AosTools](https://github.com/Lasriel/AosTools.git) :Tools for working with .aos archives used by various visual novels.
- [【工具】API HOOK和编码处理工具包](https://www.ai2.moe/topic/29225-【工具】api-hook和编码处理工具包)
- [xupefei/Locale-Emulator](https://github.com/xupefei/Locale-Emulator.git) :转区工具,使用了其中的dll

### LiLiM引擎 *.aos AosTools解包/封包命令
```
解包:
.\AosTools.exe extract .\scr.aos .\

封包:
.\AosTools.exe repack .\scr_cn .\
```

### LiLiM引擎 *.txt SExtractor文本提取正则
(TXT引擎+932编码+生成JIS替换配置+半角转直角)
```
00_search=^\[(?P<name>.+?)\](.+?)$
05_search=^\s+(.+?)$
10_search=^\/(.+?)\/\/$
15_search=^\/(.+?)$
20_search=^(.+?)$
postSkip=^[$%A-Za-z0-9#\^\s\/\\\:]
structure=paragraph
```
