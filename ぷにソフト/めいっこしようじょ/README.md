# めいっこしようじょ gpt-4o-2024-11-20 翻译补丁

MD5: `5DB31766052AC43C9D84A00180A1286B`

作者： natsumerinchan(Github) == 雨宮ゆうこ

还未推完，有bug请反馈（截图加发送存档）

## 
- 1.解压压缩包并把所有文件复制到游戏根目录下，然后双击运行siyoujo.exe
- 2.进入游戏后在`文字表示`-`字体`中将字体改为WenQuanYi Micro Hei

# Credits

- [GalTransl/GalTransl](https://github.com/GalTransl/GalTransl.git) :支持GPT-4/Claude/Deepseek/Sakura等大语言模型的Galgame自动化翻译解决方案
- [nanami5270/GARbro-Mod](https://github.com/nanami5270/GARbro-Mod.git) :Galgame解包和打包工具(krkr2引擎)
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本

krkr2 *.ks SExtractor文本提取正则(仅适用于本游戏)
```
00_search=^(?P<name>【.+】)\[r\]$
05_search=^\[link target=\*select[0-9]\](?P<msg>.+)\[endlink\]\[r\]
10_skip=^[→;,*@$#/\[{}]
15_search=^(?P<unfinish>.+)\[r\]$
20_search=^(.+)\[repage\]$
25_search=^(.+)$
structure=paragraph
```
