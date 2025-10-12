# Floating Material -The hill where the star born- DeepSeek-V2.5-1210翻译补丁 v1.0.0

MD5: `9002BD53EFCD45B79300C7660113988F`

作者： natsumerinchan(Github) == 雨宮ゆうこ

未作完整测试，有bug请反馈（截图加私发存档）

## 使用方法
- 1、应用免DVD补丁
- 2、本补丁基于修正补丁v1.02无需重复安装
- 3、解压压缩包并把所有文件复制到游戏根目录，转区运行flo_mate.exe

## 已知问题
1、SE开了截断，有文本不完整属正常现象(大约有100来句)
2、Picture Viewer PV64最新版本生成的字体不适用于老版本游戏，故暂时只能以日繁显示。

# Credits

- [GalTransl/GalTransl](https://github.com/GalTransl/GalTransl.git) :支持GPT-4/Claude/Deepseek/Sakura等大语言模型的Galgame自动化翻译解决方案
- [nanami5270/GARbro-Mod](https://github.com/nanami5270/GARbro-Mod.git) :Galgame解包和打包工具
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [Picture Viewer PV64](https://www.yox-project.com/jp/pv/download.htm) :YOX ADV++引擎官方工具

# YOX ADV++引擎 SExtractor暴力提取正则（BIN引擎+截断+JIS替换）
```
10_search=^([\x81-\xFC][\S\s]+)$
checkJIS=[@L\r\n]
ignoreDecodeError=1
separate=(\x40\x49\x40\x50\x00|\x40\x49\x40\x50\x00\x00|\x40\x49\x40\x50\x00\x00\x00|\x40\x49\x40\x50\x00\x00\x00\x00|\x00)
sample=
<暴力匹配，日文仅允许双字节，单字节符号按正则匹配[\r\n]>
```
