# てすた～Teach&Study～ Gpt4o-1120+DeepSeek-V3 翻译补丁 v1.0.0

MD5: `FB629A3E20D290A993D2D0A873F13CC9`

作者： natsumerinchan(Github) == 雨宮ゆうこ

未作完整测试，有bug请反馈（截图加私发存档）。

## 使用方法
- 1.解压压缩包并把所有文件复制到游戏根目录，安装字体后转区运行てすた.exe

# Credits

- [GalTransl/GalTransl](https://github.com/GalTransl/GalTransl.git) :支持GPT-4/Claude/Deepseek/Sakura等大语言模型的Galgame自动化翻译解决方案
- [detached64/GalArc](https://github.com/detached64/GalArc.git) :Galgame解包和打包工具(选择EmonEngine引擎)
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本

### SExtractor EmonEngine引擎 明文*.txt 提取正则(TXT引擎+cp932编码+JIS替换)
```
00_skip=^\#文章表示\(0,0\)$
01_skip=^#.+#文章表示\(0,.+\)$
05_search=^#文章表示\((?P<name>.+?),.+\)$
06_search=^#.+#文章表示\((?P<name>.+?),.+\)$
10_skip=^#
15_search=^(?P<unfinish>.+)#Return$
20_search=^(.+)$
structure=paragraph
```
