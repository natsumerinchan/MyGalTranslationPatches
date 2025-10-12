# 艶花サクラメント gpt-4o-2024-11-20翻译补丁 v1.0.1

MD5: `BAB84B40A4BD1F935D37CF3515874D2F`

作者： natsumerinchan(Github) == 雨宮ゆうこ(2dfan)

已由恶君子@2dfan全线测试，有bug请向我反馈（截图加私发存档）

## 使用方法
- 解压压缩包并把所有文件复制到游戏根目录，安装MSGothic_WenQuanYi_cnjp.ttf字体，转区运行adebana_gpt4o.exe

# Credits

- [GalTransl/GalTransl](https://github.com/GalTransl/GalTransl.git) :支持GPT-4/Claude/Deepseek/Sakura等大语言模型的Galgame自动化翻译解决方案
- [nanami5270/GARbro-Mod](https://github.com/nanami5270/GARbro-Mod.git) :Galgame解包和打包工具
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [EsuBinE](https://cottony-vase-131.notion.site/EsuBinE-6f81af237d414e2397f8e98a2104e2a1) :Escu:de引擎脚本提取和回封
- [aeae8888|escu:de 闇染Liberator游戏优化机翻方法](https://tieba.baidu.com/p/7365346652)

# SExtractor提取正则
- EsuBinE(ORG版)双行文本转换(TXT引擎+932编码+生成JIS替换配置)
```
01_search=^\%\%.+?\%\%\|(.+)$
sample=
##000004##|神川さんの身体は悪霊に取り憑かれてはいるが、<r>意識までは支配されていない。
%%000004%%|神川さんの身体は悪霊に取り憑かれてはいるが、<r>意識までは支配されていない。
```

- db_scr.bin人名暴力提取(BIN引擎+截断+生成JIS替换配置)

使用SE自带暴提正则，但separate=(\x00|\x20)，只修改人名，其他的内容原样封回。

# 其它修改(自行用解包evbunpack解包查看adebana_gpt4o文件夹)
- 改为调用系统的ＭＳ ゴシック字体：搜mess.font_type = -1;
