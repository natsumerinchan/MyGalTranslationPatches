# BALDR BULLET “REVELLION” gemini-2.5-pro 翻译补丁

MD5: `466C578908488C90F56B8A4BA627E259`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 注
- 1、本作使用自定义字库fnt，由于个人水平有限暂时只能显示日繁
- 2、本补丁适用于初回版和BALDR MASTERPIECE CHRONICLE并基于前者的exe和后者的SCRIPT制作，<br>
初回版需要借助DDrawCompat修复DirectDraw且backlog容易闪退但其未加壳可以用于人名位置修复，<br>
BMC的exe虽兼容win10和win11但加了壳无法进行修改
- 3、由于"你"字在游戏内无法正常显示，用“汝”字进行了替代

## 使用方法
- 1、初回版应用修正补丁v1.01，BALDR MASTERPIECE CHRONICLE应用修正补丁v1.03
- 2、解压压缩包并把所有文件复制到游戏根目录，转区运行`BBR_CHS.exe`。(本体是BMC时若追求稳定性不在乎人名下沉可用其原exe启动)

## 更新日志
- 2025.09.17 23:31 更新DDrawCompat至v0.6.0
- 2025.09.17 11:21 修复backlog闪退
- 2025.09.16 23:22 首次提交

# Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-4/Claude/Deepseek/Sakura等大语言模型的Galgame自动化翻译解决方案
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [narzoul/DDrawCompat](https://github.com/narzoul/DDrawCompat.git) :About DirectDraw and Direct3D 1-7 compatibility, performance and visual enhancements for Windows Vista, 7, 8, 10 and 11
- [补丁测试人员名单](https://github.com/natsumerinchan/MyGalTranslationPatches/issues/4) : [Kanadeforever@Github](https://github.com/Kanadeforever) [Whereis-Alice@Github](https://github.com/Whereis-Alice)

# SExtractor提取正则
1、初步提取
(BIN引擎+cp932编码+不开启JIS替换配置+截断)
```
00_skip=^[\S\s]{0,3}$
01_skip=\.(scr|bmp)$
02_skip=^(bmp|dummy|adv)
03_skip=^[A-Za-z0-9]+$
05_search=＞\/[a-z0-9]+?(?P<name>[^＞a-z0-9\/]+?)(「.+?」)$
10_search=＞(?P<name>[^＞]+?)(「.+?」)$
15_search=^\/[a-z0-9]+?(?P<name>[^＞a-z0-9\/].+?)(「.+?」)$
20_search=^(?P<name>[^＞]+?)(「.+?」)$
25_search=＞(.+?)$
30_search=^(?P<name>.+?)(「.+?」)\x81\x40$
35_search=^(?P<name>.+?)(「.+?」)$
40_search=^(.+?)$
ignoreDecodeError=1
separate=(\x00|\xFF)
postSkip=^[\b]
struct=paragraph
JisEncodeName=shift-jis
```

2、二次提取
(JSON引擎+UTF-8编码+开启JIS替换配置)
```
10_search=(?P<unfinish>[^<>@a-zA-Z0-9－\\\/\r\n, !]+)
```
