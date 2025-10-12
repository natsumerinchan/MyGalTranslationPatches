# ツゴウノイイ家族 Win10 gemini-2.5-pro 翻译补丁 

MD5: `7B20DB0BC443EFD5A526B8235D9FB910`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 注
- 本补丁基于[【170224】ツゴウノイイ彼女タチ＆ツゴウノイイ家族パック](https://vndb.org/r50697) 中的ツゴウノイイ家族 Win10制作，<br>
未在2013年的旧版进行测试，若在旧版使用本补丁请务必打上修正补丁v1.1和v1.2

## 使用方法
- 1.解压压缩包并把所有文件复制到游戏根目录，转区运行游戏

# Credits

- [GalTransl/GalTransl](https://github.com/GalTransl/GalTransl.git) :支持GPT-4/Claude/Deepseek/Sakura等大语言模型的Galgame自动化翻译解决方案
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [nanami5270/GARbro-Mod](https://github.com/nanami5270/GARbro-Mod.git) :Galgame解包和打包工具

## Artemis引擎 *.txt SExtractor文本提取正则
(TXT引擎+932编码+JIS替换)
```
00_search=^#v\s+(?P<name>.+?)\,
05_search=^#v\s+(?P<name>.+?)$
10_search=^(.+?)\[
15_search=^(.+?)$
postSkip=^[A-Za-z0-9#*\/\\\[\]\t\;]
structure=paragraph
```
