# ANI嫁だからっ！ gpt-4o-2024-11-20 翻译补丁

MD5: `EF76E370693C8955A37E06FFC9A8840A`

作者： natsumerinchan(Github) == 雨宮ゆうこ

有bug请反馈（截图加私发存档）

## 使用方法
- 1、应用修正补丁Ver1.01
- 2、解压压缩包并把所有文件复制到游戏根目录，双击运行Aniyome_CHS.exe

# Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-4/Claude/Deepseek/Sakura等大语言模型的Galgame自动化翻译解决方案
- [crskycode/GARbro](https://github.com/crskycode/GARbro) :Galgame解包和打包工具
- [nel1391/BcsExtractor](https://github.com/nel1391/BcsExtractor.git) :Tanuki Soft和Kaeru Soft视觉小说脚本提取工具(*.bcs)
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [AtomCrafty/UniversalInjectorFramework](https://github.com/AtomCrafty/UniversalInjectorFramework.git) :实现自动转区和更改字体，jis映射
- [xupefei/Locale-Emulator](https://github.com/xupefei/Locale-Emulator.git) :转区工具,使用了其中的dll

# SExtractor提取正则(CSV引擎+932编码)
```
00_skip=^$
10_search=^([\S\s]+)$
extractKey=name8,14
postSkip=^[ -~]
extraData=useIndex

<extractKey为列名的正则匹配>
<当extraData为nohead或者useIndex时，extractKey为列序号列表，如：1,name2,3>
```
