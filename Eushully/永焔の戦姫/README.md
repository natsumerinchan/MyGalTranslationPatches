# 永焔の戦姫 gemini-2.5-pro 翻译补丁

MD5: `60E3217590486B75FDDC9E84C91F5699`

作者： natsumerinchan(Github) == 雨宮ゆうこ

人名翻译参考了[Eushully 中文 Wiki](https://eushully.fandom.com/zh/wiki/EuWiki:%E9%A6%96%E9%A0%81)，但绝大多数译名没有和战z、幻1、幻2的人工汉化统一，  
且有少数人名因为原文被换行导致GPT字典没匹配到未能统一。

## 使用方法

1.解压压缩包并把`Releases`文件夹内所有文件复制到游戏根目录，双击AGE_CHS.exe运行

## 更新日志

- 2025.11.10 重新脱壳修复win7上找不到combase.dll的问题并更新CELICA_HOOK
- 2025.11.05 使用gemini-2.5-pro重跑
- 2025.02.18 使用qwen-max-latest重跑
- 2024.10.19 解决部分文本对话有重复，以及部分字句未汉化的问题，并把默认字体改为隶书

## Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-3.5/GPT-4/Newbing/Sakura等大语言模型的Galgame自动化翻译解决方案
- [foxofice/alf](https://github.com/foxofice/alf.git) :Eushully社解包工具
- [Kelebek1/Eushully-Decompiler](https://github.com/Kelebek1/Eushully-Decompiler.git) :Eushully社脚本反编译和重编译工具
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [xupefei/Locale-Emulator](https://github.com/xupefei/Locale-Emulator.git) :转区软件,使用了其中的dll
- [Eushully社脚本SExtractor文本提取正则](https://www.moyu.moe/patch/253/resource) :作者御爱@julixian(在压缩包的补丁说明里)
- [[AGE] Eushully ASProtect 脱壳](https://github.com/Dir-A/Dir-A_Essays_MD/blob/eb87f07ee39e1d026901867169df7d7d43113ee3/Reverse/%5BAGE%5D%20Eushully%20ASProtect%20%E8%84%B1%E5%A3%B3/%5BAGE%5D%20Eushully%20ASProtect%20%E8%84%B1%E5%A3%B3.md) :作者Dir-A
- [natsumerinchan/CELICA_HOOK](https://github.com/natsumerinchan/CELICA_HOOK.git) :个人写的游戏程序hook工具

## Eushully-Decompiler *.txt SExtractor文本提取正则(改编自御爱@julixian的版本)

(TXT引擎+UTF-8编码+JIS替换)

```md
00_skip=wait-for-input 0
01_search=^show-text 0 "\s{0,}(?P<unfinish>.*?)"$
02_search=^display-furigana 0 "\s{0,}(?P<unfinish>.*?)" ".*"$
03_skip=^set-string \(.*\) ""$
04_search=^set-string \(.*\) "\s{0,}【.*?】\s{0,}(?P<msg>.*?)"$
05_search=^set-string \(.*\) "\s{0,}(?P<msg>.*?)"$
structure=paragraph
```
