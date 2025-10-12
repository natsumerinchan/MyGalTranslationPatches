# 月下之煌 qwen-max-latest 翻译补丁

MD5: `2D9E5D3FB6D1C6926712CB0F495A2D48`

作者： natsumerinchan(Github) == 雨宮ゆうこ

还未推完，有bug请反馈（截图加发送存档）

## 使用方法
1.解压压缩包并把所有文件复制到游戏根目录下，然后双击运行gekka.exe
2.进入游戏后在设置-字体中将字体改为WenQuanYi Micro Hei

# Credits

- [GalTransl/GalTransl](https://github.com/GalTransl/GalTransl.git) :支持GPT-4/Claude/Deepseek/Sakura等大语言模型的Galgame自动化翻译解决方案
- [nanami5270/GARbro-Mod](https://github.com/nanami5270/GARbro-Mod.git) :Galgame解包和打包工具(krkr2引擎)
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [krkr字体选择时如何支持中文字体](https://zhuanlan.zhihu.com/p/21775023)

krkr2 *.ks SExtractor文本提取正则(仅适用于本游戏)
```
05_search=^\[em\]\[quake.+?\]\[pv.+?\](?P<name>.+)(?P<msg>「.+」)\[ps\]
10_search=^\[em\]\[pv.+?\](?P<name>.+)(?P<msg>「.+」).+\[ps\]
15_search=^\[em\]\[pv.+?\](?P<name>.+)(?P<msg>「.+」)\[ps\]
20_search=^\[em\](?P<name>.+)(?P<msg>「.+」)\[ps\]
25_search=^\[em\]\[quake.+\](?P<msg>.+)\[ps\]
30_search=^\[em\]\[pv.+?\](?P<msg>.+)\[ps\]
35_search=^\[em\](?P<msg>.+)\[ps\]
```
