# あかときっ -もっと脱がせて恋の魔砲- gpt-4.1-2025-04-14 + DeepSeek-V3-0324 翻译补丁

MD5: `E3D5BD4DDC553FD5AA647F23636B9322`

作者： natsumerinchan(Github) == 雨宮ゆうこ

未作完整测试，有bug请反馈（截图加私发存档）

## 使用方法
- 1、应用修正补丁v1.01和v1.02
- 2、解压压缩包并把所有文件复制到游戏根目录，安装VLゴシック-Regular.ttf字体，转区运行akatoki.exe

## 更新日志
- 2025.04.22 22:43 首次提交
- 2025.04.23 11:00 取消enigma打包以修复人名翻译

# Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-3.5/GPT-4/Newbing/Sakura等大语言模型的Galgame自动化翻译解决方案
- [crskycode/GARbro](https://github.com/crskycode/GARbro) :Galgame解包和打包工具
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [EsuBinE](https://cottony-vase-131.notion.site/EsuBinE-6f81af237d414e2397f8e98a2104e2a1) :Escu:de引擎脚本提取和回封

# SExtractor提取正则
- EsuBinE(ORG版)双行文本转换(TXT引擎+932编码+生成JIS替换配置)
```
01_search=^\%\%.+?\%\%\|(.+)$
sample=
##000004##|神川さんの身体は悪霊に取り憑かれてはいるが、<r>意識までは支配されていない。
%%000004%%|神川さんの身体は悪霊に取り憑かれてはいるが、<r>意識までは支配されていない。
```

- json二次提取正则(JSON引擎+utf-8编码)
```
10_search=(?P<unfinish>[^@a-zA-Z0-9－'=+<>/\r\n\t\s]+)
```

- enum_scr.bin人名和data.bin文本暴力提取(BIN引擎+截断+生成JIS替换配置)

使用SE自带暴提正则，但separate=(\x00|\x20)。

