# HoneyComing - クレアファンディスク gpt-4o-2024-11-20翻译补丁 v1.0.0

MD5: `31FF871E8A61174EED20CFE97C17822B`

作者： natsumerinchan(Github) == 雨宮ゆうこ(2dfan)

已ctrl未出现闪退，有bug请反馈（截图加私发存档）

## 使用方法
- 解压压缩包并把所有文件复制到游戏根目录，安装字体"MSGothic_WenQuanYi_cnjp.ttf"后转区运行HoneyComing.exe

# Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-3.5/GPT-4/Newbing/Sakura等大语言模型的Galgame自动化翻译解决方案
- [nanami5270/GARbro-Mod](https://github.com/nanami5270/GARbro-Mod.git) :Galgame解包和打包工具(打包格式为.ykc，重命名为.dat后缀即可)
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本,并使用其jis替换字体

# Yuka Script *.yks SExtractor暴力提取正则(BIN引擎+截断)
```
00_skip=^[\S\s]{0,3}$
01_skip=\xCE\xFF\xFF\xFF\x6B
10_search=^(?P<pre_nameANDmsg>「[\x81-\xFC][\S\s].+)$
11_search=^([\x81-\xFC][\S\s]+)$
ignoreDecodeError=1
separate=\x00
struct=paragraph
sample=
<暴力匹配，日文仅允许双字节，单字节符号按正则匹配[\r\n]>
```
