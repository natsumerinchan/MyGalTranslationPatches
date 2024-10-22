# Strawberry Nauts -ストロベリーノーツ- Full HD Memorial Plus gpt-4o-2024-05-13 翻译补丁

MD5: `05185FF40C0540D9AA0578F43D2D5825`

作者： natsumerinchan(Github) == 雨宮ゆうこ(2dfan)

未作测试，可能会出现漏翻，还请多多反馈bug！！！3q

## 使用方法
1.安装修正补丁v1.01
2.解压压缩包并把所有文件复制到游戏根目录，双击StrawberryNauts_gpt4o.exe运行(不需要转区)
3.pit BBS mode仍然显示日文的，更新补丁后从头开始skip到你玩到的位置，读档的话文本缓存没更新

# Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-3.5/GPT-4/Newbing/Sakura等大语言模型的Galgame自动化翻译解决方案
- [crskycode/GARbro](https://github.com/crskycode/GARbro) :Galgame解包和打包工具
- [crskycode/BGI_Script_Tool](https://github.com/crskycode/BGI_Script_Tool.git) :BGI引擎脚本提取和打包工具
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [Enigma Virtual Box](https://enigmaprotector.com/assets/files/enigmavb.exe) :把脚本文件打包进exe
- [AtomCrafty/UniversalInjectorFramework](https://github.com/AtomCrafty/UniversalInjectorFramework.git) :实现更改字体，jis映射
- [Strawberry Nauts -ストロベリーノーツ- Full HD Memorial Plus免DVD补丁](https://2dfan.com/downloads/28970)

### SExtractor文本提取正则

先用两条正则删除所有◇行`^◇.+?◇.+`和空行`^(\t)*$\n`

再用SExtractor提取文本:
```
00_skip=^◆.+?◆[　#_A-Za-z0-9]
10_search=^◆.+?◆(?P<pre_nameANDmsg>「.+)$
20_search=^◆.+?◆(?P<msg>.+)$
structure=paragraph
```