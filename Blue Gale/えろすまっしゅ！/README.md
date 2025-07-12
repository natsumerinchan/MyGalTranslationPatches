# えろすまっしゅ！ gemini-2.5-pro-preview-06-05 翻译补丁

MD5: `F22C32F00F15C317CC7F86591A03D91D`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 使用方法
- 1.压缩包内字体可以不安装
- 2.将压缩包内所有文件解压至游戏根目录，双击运行01_EROS_CHS.exe(已自动转区)

## 已知问题
- 1.开头有弹窗报错但不影响游戏(SB引擎用日文当函数名，直接删掉那行倒是不报错了但存档界面段落那列就无了)

# Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-3.5/GPT-4/Newbing/Sakura等大语言模型的Galgame自动化翻译解决方案
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [Crass-source](https://github.com/shangjiaxuan/Crass-source.git) :作者：痴汉公贼@飞雪之城（我用DeepSeek-R1将BLUEGALE引擎的cui插件转化为了单独的命令行程序bluegaletool，目前没有实现生成zbm图片和打包snn的功能）
- [【工具】API HOOK和编码处理工具包](https://www.ai2.moe/topic/29225-【工具】api-hook和编码处理工具包)
- [xupefei/Locale-Emulator](https://github.com/xupefei/Locale-Emulator.git) :转区工具,使用了其中的dll

### BlueGale引擎 *.bdt解密/加密命令
```
(解密和加密实际上是对数据的每一位取反)
解密:
.\bluegaletool.exe -t bdt .\scene00.bdt

加密:
.\bluegaletool.exe -t bdt -r .\script\new\scene00.txt
```

### BlueGale引擎 *.txt SExtractor文本提取正则
(TXT引擎+932编码+生成JIS替换配置)
```
00_search=\!(?P<name>.+?)\s+"(.+?)$
05_search=\"(.+?)$
10_search=^\s+QP([^,]+?),([^,]+?),([^,]+?),([^,]+?)$
15_search=^\s+QP([^,]+?),([^,]+?),([^,]+?)$
20_search=^\s+QP([^,]+?),([^,]+?)$
structure=paragraph
```
