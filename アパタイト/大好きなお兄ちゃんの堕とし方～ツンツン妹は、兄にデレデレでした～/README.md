# 大好きなお兄ちゃんの堕とし方～ツンツン妹は、兄にデレデレでした～ claude-3-5-sonnet-20240620 翻译补丁

MD5: `8AAF9FC9F2444AB4CA0661E0824706CE`

作者： natsumerinchan(Github) == 雨宮ゆうこ(2dfan)

未作完整测试，可能会出现漏翻，还请多多反馈bug！！！3q

## 使用方法
1.解压压缩包并把所有文件复制到data文件夹，双击DaisukinaOnichanNoOtoshikata.exe运行(无需转区)

# Credits

- [GalTransl/GalTransl](https://github.com/GalTransl/GalTransl.git) :支持GPT-4/Claude/Deepseek/Sakura等大语言模型的Galgame自动化翻译解决方案
- MTool :krkr引擎脚本提取（目前发现只有它可以对加了壳的krkr游戏进行提取）
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [arcusmaximus/KirikiriTools](https://github.com/arcusmaximus/KirikiriTools.git) :Xp3Pack.exe用于封包
- krkrfont.exe :创建krkr字体
- [Emeditor](https://www.emeditor.com/) :脚本批量转码为utf-16-le（有签名）

### SExtractor .ks提取正则
```
00_search=\[name text\=\"(?P<name>.+?)\"\]
01_skip=^[;*@#\[]
02_search=^(?P<unfinish>.+)\[r\]$
03_search=^(.+)$
sample=
[name text="聖良"]
[voice id="sir" file="vf00_000sir0000"]
「ふんっ……大体さ、お兄ちゃんってさぁ……[r]
あ、言っても無駄？　無理？　どーせわかんないよねー！？」
[tp]
```
