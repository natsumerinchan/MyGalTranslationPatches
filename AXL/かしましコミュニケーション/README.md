# かしましコミュニケーション gpt-4o-2024-11-20 + DeepSeek-V3-0324 翻译补丁

MD5: `7E97F2CAD14392B4289A2A5C65692B8F`

作者： natsumerinchan(Github) == 雨宮ゆうこ

还未推完，有bug请反馈（截图加发送存档）

## 使用方法
- 1.应用win8修正补丁(http://mail.sumikko-soft.com/support.htm)
- 2.安装压缩包里的`VLゴシック-Regular.ttf`字体(该字体是用SExtractor的字体脚本将黑体进行jis替换后再用FontCreator伪装为VLゴシック所得)
- 3.解压压缩包并把所有文件复制到游戏根目录下，然后转区运行かしましコミュニケーション.exe(否则背景、立绘会消失)
- 4.进入游戏后在`文字表示`-`フォント`中将字体改为`VL ゴシック`

# Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-3.5/GPT-4/Newbing/Sakura等大语言模型的Galgame自动化翻译解决方案
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [XP3Viewer](https://github.com/Inori/FuckGalEngine/blob/master/Krkr/XP3Viewer.rar) :可用于解包或封包被加密以及exe被保护的krkr2引擎游戏

## krkr2 *.ks SExtractor文本提取正则
(txt引擎+932编码+生成jis替换配置)
```
00_search=^【(?P<name>.+?)】$
01_skip=^[;*@#_A-Za-z0-9\[]
02_search=^(?P<msg>「.+」)$
03_search=^(?P<msg>『.+』)$
04_search=^(?P<start_unfinish>「.+)$
05_search=^\s+(?P<end_unfinish>[^「].+」)$
06_search=^(?P<start_unfinish>『.+)$
07_search=^\s+(?P<end_unfinish>[^『].+』)$
08_search=^(?P<unfinish>\s+.+)$
09_search=^(?P<unfinish>　.+)$
10_search=^(?P<unfinish>.+[^。、！？])$
11_search=^(.+)$
structure=paragraph
```
