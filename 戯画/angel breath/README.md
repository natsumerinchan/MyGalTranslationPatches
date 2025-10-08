# angel breath claude-3-5-sonnet-20240620 翻译补丁 

MD5: `5AA318040B3BB3A4C5BCD89028FD6C37`

作者： natsumerinchan(Github) == 雨宮ゆうこ(2dfan)

已根据攻略ctrl了全线内容，未发现闪退。有其他bug请反馈（截图加私发存档）

## 使用方法
- 1、安装修正补丁v1.01
- 2、应用站内免DVD补丁(实为x64系统兼容补丁，无免DVD效果，首次启动游戏需用DAEMON tools同时挂载disk1和disk2)
- 3、解压压缩包并把所有文件复制到游戏根目录，双击angelbreath.exe运行(无需手动转区因为UniversalInjectorFramework会自动处理)

# Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-3.5/GPT-4/Newbing/Sakura等大语言模型的Galgame自动化翻译解决方案
- [nanami5270/GARbro-Mod](https://github.com/nanami5270/GARbro-Mod.git) :Galgame解包和打包工具
- [ginyoushijin/GIGA_NeXAS](https://github.com/ginyoushijin/GIGA_NeXAS.git) :戏画引擎解封包 (需配合转区软件使用，否则文件名会乱码，这游戏有些古老，解包时文本解密失败但可用于无压缩封包)
- [AtomCrafty/UniversalInjectorFramework](https://github.com/AtomCrafty/UniversalInjectorFramework.git) :实现自动转区和更改字体
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [xupefei/Locale-Emulator](https://github.com/xupefei/Locale-Emulator.git) :转区软件,使用了其中的dll

# SExtractor提取正则
1、初步提取(BIN引擎+自带NeXAS匹配规则+不开启截断)

2、二次提取(JSON引擎)
- 先删除所有假名注释（详见我制作的bitter smile.补丁），再用此正则筛掉控制代码
```
10_search=(?P<unfinish>[^@a-zA-Z0-9－/\r\n]+)
```
