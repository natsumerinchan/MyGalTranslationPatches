# ひなたテラス～We don’t abandon you.～ gpt-4o-2024-11-20+DeepSeek-V3 翻译补丁 v1.0.0

MD5: `FAEAEDF52A358D864035B60930C5C426`

作者： natsumerinchan(Github) == 雨宮ゆうこ(2dfan)

未完整测试。有bug请反馈（截图加私发存档）

## 使用方法
- 1、应用站内免DVD补丁
- 2、解压压缩包并把所有文件复制到游戏根目录，安装压缩包内字体后转区运行HinataTerraceWin10NoDVD.exe

# Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-3.5/GPT-4/Newbing/Sakura等大语言模型的Galgame自动化翻译解决方案
- [ginyoushijin/GIGA_NeXAS](https://github.com/ginyoushijin/GIGA_NeXAS.git) :戏画引擎解封包 (需配合转区软件使用，否则文件名会乱码)
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本

# SExtractor提取正则
1、初步提取(BIN引擎+自带NeXAS匹配规则+不开启截断+删掉pre_name)

2、二次提取(JSON引擎)
- 先删除所有假名注释（详见我制作的bitter smile.补丁），再用此正则筛掉控制代码
```
10_search=(?P<unfinish>[^@a-zA-Z0-9－/\r\n]+)
```
