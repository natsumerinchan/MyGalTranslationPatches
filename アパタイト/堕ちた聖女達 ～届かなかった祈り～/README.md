# 堕ちた聖女達 ～届かなかった祈り～ gemini-2.5-pro 翻译补丁

MD5: `2626A937B2C77D6934958CFC69363938`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 使用方法
- 1.将压缩包内所有文件解压至游戏根目录，双击运行data\OchitaSeijyotaghi.exe

# Credits

- [GalTransl/GalTransl](https://github.com/GalTransl/GalTransl.git) :支持GPT-4/Claude/Deepseek/Sakura等大语言模型的Galgame自动化翻译解决方案
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [resty-daze/xp3dumper](https://github.com/resty-daze/xp3dumper.git) :krkr2 xp3解包
- [arcusmaximus/KirikiriTools](https://github.com/arcusmaximus/KirikiriTools.git) :Xp3Pack.exe 打包xp3

### krkr2引擎 *.ks SExtractor文本提取正则(仅适用于本作)
(TXT引擎+UTF-16编码+不生成JIS替换配置)
```
00_search=^\[name text="(?P<name>.+?)"\]$
05_search=^(?P<unfinish>.+?)\[r\]$
10_search=^(.+?)$
postSkip=^[\[;*\t\{\}A-Za-z]
structure=paragraph
```
