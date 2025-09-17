# 装甲悪鬼村正 贖罪編 gemini-2.5-pro 翻译补丁 

MD5: `E121D80DC6FBC765746B69DDCC73FFF1`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 注
- 本作无语音，属正常现象

## 使用方法
- 1.解压压缩包并把所有文件复制到游戏根目录，双击运行MuramasaSS.exe

# Credits
- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-3.5/GPT-4/Newbing/Sakura等大语言模型的Galgame自动化翻译解决方案
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [crskycode/GARbro](https://github.com/crskycode/GARbro) :Galgame解包和打包工具
- [Wilhansen/nipa](https://github.com/Wilhansen/nipa.git) :用于Nitroplus社N2System引擎游戏的解包和打包工具
- [AtomCrafty/UniversalInjectorFramework](https://github.com/AtomCrafty/UniversalInjectorFramework.git) :实现更改字体，jis映射
- [xupefei/Locale-Emulator](https://github.com/xupefei/Locale-Emulator.git) :转区工具,使用了其中的dll
- 补丁测试人员： [伪恶君子333@御爱同萌](https://www.ai2.moe/profile/9569-伪恶君子333/)

## N2System引擎 *.nss SExtractor文本提取正则
(TXT引擎+932编码+JIS替换)
```
00_skip=^\</PRE\>$
01_skip=^\s+$
02_skip=^\<PRE
03_skip=name=\"(?P<name>.+?)\"
04_skip=name=\'(?P<name>.+?)\'
05_search=^\s+(?P<end_unfinish>.+?)\<k\>$
10_search=^(?P<end_unfinish>.+?)\<k\>$
15_search=^\s+\<k\>(?P<start_unfinish>.+?)$
20_search=^\<k\>(?P<start_unfinish>.+?)$
25_search=^\s+(?P<unfinish>.+?)$
30_search=^(?P<unfinish>.+?)$
postSkip=^[A-Za-z0-9\{\}\[\]\\\/#*@=$\.\s\t\"]
structure=paragraph
```
