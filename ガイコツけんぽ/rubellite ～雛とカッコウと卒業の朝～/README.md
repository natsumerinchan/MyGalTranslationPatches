# rubellite ～雛とカッコウと卒業の朝～ gemini-2.5-pro 翻译补丁

MD5: `AA50B0C2A702F9AE276043DF81BAB38B`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 使用方法
- 1.将压缩包内所有文件解压至游戏根目录，双击运行rubellite.exe

## 更新日志
- 2025.08.08 12:21 首次提交
- 2025.08.09 20:09 修复Ｘデーa_TRUE.ks 1793行报错

# Credits

- [GalTransl/GalTransl](https://github.com/GalTransl/GalTransl.git) :支持GPT-4/Claude/Deepseek/Sakura等大语言模型的Galgame自动化翻译解决方案
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [nanami5270/GARbro-Mod](https://github.com/nanami5270/GARbro-Mod.git) :Galgame解包和打包工具
- [arcusmaximus/KirikiriTools](https://github.com/arcusmaximus/KirikiriTools.git) :Xp3Pack.exe 打包xp3

### krkr2引擎 *.ks SExtractor文本提取正则(仅适用于本作)
(TXT引擎+UTF-16编码+不生成JIS替换配置)
```
00_search=^【(?P<name>.+?)】(.+?)\[p\]$
05_search=^【(?P<name>.+?)】(.+?)$
10_search=^(.+?)\[p\]$
15_search=^(.+?)\s+\[r\]$
20_search=^(.+?)$
postSkip=^[A-Za-z0-9;*\[\]\s@\{\}\\\/]
skipIgnoreUnfinish=true
structure=paragraph
```
