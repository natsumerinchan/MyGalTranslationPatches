# bitter smile. gpt-4o-2024-05-13 翻译补丁 

MD5: `81A83A11D5F1226953F1831125B8C97D`

作者： natsumerinchan(Github) == 雨宮ゆうこ(2dfan)

未作测试，可能会出现漏翻，还请多多反馈bug！！！3q

## 使用方法
应用站内免DVD补丁后(我个人用的是dll版)，解压压缩包并把所有文件复制到游戏根目录，双击bittersmile.exe运行((无需手动转区因为UniversalInjectorFramework会自动处理))

## 更新日志
1、修复部分文本闪退的问题(解决方法是把文本中所有的假名注释都删掉，如@r知世翔@ちせか@改为知世翔，闪退原因是gpt-4o遇上类似假名注释时可能会漏@号，导致假名注释的格式不完整)

# Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-3.5/GPT-4/Newbing/Sakura等大语言模型的Galgame自动化翻译解决方案
- [ginyoushijin/GIGA_NeXAS](https://github.com/ginyoushijin/GIGA_NeXAS.git) :戏画引擎解/封包 (需配合转区软件使用，否则解包出来的bin文件名会乱码)
- [AtomCrafty/UniversalInjectorFramework](https://github.com/AtomCrafty/UniversalInjectorFramework.git) :实现自动转区和更改字体，jis映射
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [xupefei/Locale-Emulator](https://github.com/xupefei/Locale-Emulator.git) :转区软件,使用了其中的dll