# 艶花サクラメント gpt-4o-2024-11-20翻译补丁 v1.0.0

MD5: `C0C4D15771BF535646DC25CF45957DA7`

作者： natsumerinchan(Github) == 雨宮ゆうこ(2dfan)

目前仅ctrl了日向线，有bug请反馈（截图加私发存档）

## 使用方法
- 解压压缩包并把所有文件复制到游戏根目录，转区运行adebana_gpt4o.exe

# Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-3.5/GPT-4/Newbing/Sakura等大语言模型的Galgame自动化翻译解决方案
- [crskycode/GARbro](https://github.com/crskycode/GARbro) :Galgame解包和打包工具
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [EsuBinE](https://cottony-vase-131.notion.site/EsuBinE-6f81af237d414e2397f8e98a2104e2a1) :Escu:de引擎脚本提取和回封
- [aeae8888|escu:de 闇染Liberator游戏优化机翻方法](https://tieba.baidu.com/p/7365346652)

# SExtractor提取正则
- EsuBinE双行文本转换(TXT引擎)
```
01_search=^\%\%.+?\%\%\|(.+)$
sample=
##000004##|神川さんの身体は悪霊に取り憑かれてはいるが、<r>意識までは支配されていない。
%%000004%%|神川さんの身体は悪霊に取り憑かれてはいるが、<r>意識までは支配されていない。
```

- db_scr.bin人名暴力提取(BIN引擎+截断+不生成JIS替换配置)

使用SE自带暴提正则，但separate=(\x00|\x20)，只修改人名，其他的内容原样封回。

# exe爆改GBK编码
转区运行游戏后用x32dbg附加调试，在`视图`-`模块`中切换到主程序视图(如adebana.exe)，右键`搜索`-`当前区域`-`跨模块调用`，搜`CreateFontIndirectA`后点开，往上不远处可见数字`80`或`0x80`，右键`汇编`把`0x80`改为`0x86`，然后在`文件`-`补丁`-`修补文件`保存修改。

# 其它修改
- [aeae8888|escu:de 闇染Liberator游戏优化机翻方法](https://tieba.baidu.com/p/7365346652)
- 改用自定义字体(自行用解包evbunpack解包查看adebana_gpt4o文件夹)：搜mess.font_type = -3;
