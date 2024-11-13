# おしえて Re：メイド Memorial Edition claude-3-5-sonnet-20240620 翻译补丁 

MD5: `4B7E5F9CB2A75EF6606AE48C928A42B1`

作者： natsumerinchan(Github) == 雨宮ゆうこ(2dfan)

本补丁适用于Memorial Edition版本。未经完整测试，有bug请反馈（截图加私发存档）

## 使用方法
- 解压压缩包并把所有文件复制到游戏根目录，双击angelbreath.exe运行(无需手动转区因为UniversalInjectorFramework会自动处理)

# Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-3.5/GPT-4/Newbing/Sakura等大语言模型的Galgame自动化翻译解决方案
- [crskycode/GARbro](https://github.com/crskycode/GARbro) :Galgame解包和打包工具
- [ZQF-ReVN/RxPJADV](https://github.com/ZQF-ReVN/RxPJADV.git) :PJADV引擎解封包、脚本提取加解密
- [AtomCrafty/UniversalInjectorFramework](https://github.com/AtomCrafty/UniversalInjectorFramework.git) :实现自动转区和更改字体
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [xupefei/Locale-Emulator](https://github.com/xupefei/Locale-Emulator.git) :转区软件,使用了其中的dll

# SExtractor提取正则(TXT引擎)
```
10_search=^\s\s*"chr_tra"\s*:\s*"(?P<name>[^"]+)",\s*?$
20_search=^\s\s*"chp_tra"\s*:\s*"(?P<msg>[^"]+)"\s*?$
30_search=^\s\s*"sel_tra"\s*:\s*"(?P<msg>[^"]+)"\s*?$
40_search=^\s\s*"msg_tra"\s*:\s*"(?P<msg>[^"]+)"\s*?$

structure=paragraph
```

