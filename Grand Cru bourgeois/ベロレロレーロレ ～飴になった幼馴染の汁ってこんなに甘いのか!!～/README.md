# ベロレロレーロレ ～飴になった幼馴染の汁ってこんなに甘いのか!!～ DeepSeek-V3 翻译补丁 v1.0.0

MD5: `1E3ED4E4804D80BC377B8BF342511443`

作者： natsumerinchan(Github) == 雨宮ゆうこ

未完整测试。有bug请反馈（截图加私发存档）

## 使用方法
1.解压压缩包并把所有文件复制到游戏根目录，双击berorero_dsv3运行

# Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-3.5/GPT-4/Newbing/Sakura等大语言模型的Galgame自动化翻译解决方案
- [crskycode/GARbro](https://github.com/crskycode/GARbro) :Galgame解包和打包工具
- [crskycode/BGI_Script_Tool](https://github.com/crskycode/BGI_Script_Tool.git) :BGI引擎脚本提取和打包工具(要改源码把写入时的编码从utf-8改为shift-jis)
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [Enigma Virtual Box](https://enigmaprotector.com/assets/files/enigmavb.exe) :把脚本文件打包进exe
- [AtomCrafty/UniversalInjectorFramework](https://github.com/AtomCrafty/UniversalInjectorFramework.git) :实现更改字体，jis映射

### SExtractor文本提取正则

```
00_skip=^◆.+?◆[　#_A-Za-z0-9]
10_search=^◆.+?◆(?P<pre_nameANDmsg>「.+)$
20_search=^◆.+?◆(?P<msg>.+)$
structure=paragraph
```
