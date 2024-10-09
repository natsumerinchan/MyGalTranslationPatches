# 永焔の戦姫 gpt-4o-2024-05-13 翻译补丁 

MD5: `ACA419DB1A391689B36729185E391272`

作者： natsumerinchan(Github) == 雨宮ゆうこ(2dfan)

未作测试，绝大多数译名没有和战z、幻1、幻2的人工汉化统一，可能会出现漏翻，还请多多反馈bug！！！3q

## 使用方法
1.解压压缩包并把所有文件复制到游戏根目录，双击AGE_gpt4o.exe运行((无需手动转区因为UniversalInjectorFramework会自动处理))

## 已知Bug
存在文本重复

# Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-3.5/GPT-4/Newbing/Sakura等大语言模型的Galgame自动化翻译解决方案
- [foxofice/alf](https://github.com/foxofice/alf.git) :Eushully社解包工具
- [Kelebek1/Eushully-Decompiler](https://github.com/Kelebek1/Eushully-Decompiler.git) :Eushully社脚本反编译和重编译工具
- [AtomCrafty/UniversalInjectorFramework](https://github.com/AtomCrafty/UniversalInjectorFramework.git) :实现自动转区和更改字体，jis映射
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [xupefei/Locale-Emulator](https://github.com/xupefei/Locale-Emulator.git) :转区软件,使用了其中的dll
- [Eushully社脚本SExtractor文本提取正则](https://2dfan.com/downloads/27652) :作者2dfan@julixian(在压缩包的补丁说明里)
- [[AGE] Eushully ASProtect 脱壳](https://github.com/Dir-A/Dir-A_Essays_MD/blob/eb87f07ee39e1d026901867169df7d7d43113ee3/Reverse/%5BAGE%5D%20Eushully%20ASProtect%20%E8%84%B1%E5%A3%B3/%5BAGE%5D%20Eushully%20ASProtect%20%E8%84%B1%E5%A3%B3.md) :作者Dir-A

SExtractor文本提取正则(作者2dfan@julixian)：
```
01_skip=end-text-line 0
02_search=^show-text 0 "(?P.*?)"$
03_search=^display-furigana 0 "(?P.*?)" ".*"$
04_search=^set-string \(.*\) "【.*?】(?P.*?)"$
05_search=^set-string \(.*\) "(?P.*?)"$
structure=paragraph
```