# WIZARD GIRL AMBITIOUS claude-3-7-sonnet 翻译补丁

MD5: `0730186F007436B09B204A7FE47F7A0B`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 使用方法
- 1.应用修正补丁1.1
- 2.将压缩包内所有文件解压至游戏根目录，安装压缩包内字体后转区运行wga.exe

## 已知问题
- 1.人名未翻译且显示不正常

# Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-3.5/GPT-4/Newbing/Sakura等大语言模型的Galgame自动化翻译解决方案
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [Lasriel/AosTools](https://github.com/Lasriel/AosTools.git) :Tools for working with .aos archives used by various visual novels.

### LiLiM引擎 *.aos AosTools解包/封包命令
```
解包:
.\AosTools.exe extract .\scr.aos .\

封包:
.\AosTools.exe repack .\scr_cn .\
```

### LiLiM引擎 *.txt SExtractor文本提取正则
(TXT引擎+932编码+生成JIS替换配置)
```
00_search=^\[(?P<name>.+?)\](.+?)$
05_search=^\s+(.+?)$
10_search=^\/(.+?)\/\/$
15_search=^\/(.+?)$
20_search=^(.+?)$
postSkip=^[%A-Za-z0-9#\^\s\/\\\:]
structure=paragraph
```
