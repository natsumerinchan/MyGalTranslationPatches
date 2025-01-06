# つくしてあげるのに！PLUS DeepSeek-V3 翻译补丁 v1.0.0

MD5: `904BDE09E027364DE82359CB8539EA66`

作者： natsumerinchan(Github) == 雨宮ゆうこ

未作完整测试，有bug请反馈（截图加私发存档）。

## 使用方法
- 1.安装修正补丁
- 2.解压压缩包并把所有文件复制到游戏根目录，安装字体后转区运行tukusi_Plus_gpt4o.exe

# Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-3.5/GPT-4/Newbing/Sakura等大语言模型的Galgame自动化翻译解决方案
- [crskycode/GARbro](https://github.com/crskycode/GARbro) :Galgame解包和打包工具(打包时选yks格式)
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [Inori/FuckGalEngine](https://github.com/Inori/FuckGalEngine.git) :galgame破解工具集，使用其中YukaScript引擎的text_export.py和text_import.py(脚本处理)

### SExtractor text_export.py文本提取正则(TXT引擎+UTF-16编码+JIS替换)
```
01_skip=^★.+?★((SYSTEM|BGM|BG|TA|EV|VOICE|ETC|avi|se|SE).+)$
02_skip=^★.+?★((bgm|system|voice).+)$
03_search=^★.+?★(?P<pre_nameANDmsg>「.+」)$
04_search=^★.+?★(.+)$
structure=paragraph
```
