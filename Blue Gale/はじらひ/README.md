# はじらひ gemini-2.5-pro-preview-06-05 翻译补丁

MD5: `FDB13411E27B5FD4899BDA077C7987B8`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 使用方法
- 1.压缩包内字体可以不安装
- 2.将压缩包内所有文件解压至游戏根目录，双击运行01_hajirahi_chs.exe(已自动转区)

## 已知问题
- 1.Win11上无法正常播放OP(原版也播放不了)

# Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-3.5/GPT-4/Newbing/Sakura等大语言模型的Galgame自动化翻译解决方案
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [【工具】API HOOK和编码处理工具包](https://www.ai2.moe/topic/29225-【工具】api-hook和编码处理工具包)
- [xupefei/Locale-Emulator](https://github.com/xupefei/Locale-Emulator.git) :转区工具,使用了其中的dll

### BlueGale引擎 *.bdt SExtractor文本提取正则
(BlueGale_bdt引擎+932编码+生成JIS替换配置)
```
00_search=\!(?P<name>.+?)\s+"(.+?)$
01_search=\!(?P<name>.+?)"(.+?)$
05_search=\"(.+?)$
10_search=QP([^,]+?),([^,]+?),([^,]+?),([^,]+?)$
15_search=QP([^,]+?),([^,]+?),([^,]+?)$
20_search=QP([^,]+?),([^,]+?)$
decrypt=1
extraData=exportIndex
pureText=1
<decrypt=1解密, 默认encrypt=1加密>
```
