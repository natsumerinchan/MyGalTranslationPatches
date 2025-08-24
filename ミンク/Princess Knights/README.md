# Princess Knights gemini-2.5-pro 翻译补丁 

MD5: `A67FD67267BE38193307F0D8C1BC843D`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 注
- 1、需打入注册表iv32+iv50.reg否则无法在win10和win11上播放OP
- 2、开头旁白是bmp图片形式，我翻了但程序无法正常读取显示，自己对照着看吧

## 使用方法
- 1.将scr.det重命名为scr.det.bak
- 2.解压压缩包并把所有文件复制到游戏根目录，双击运行pRIkNI_CHS.exe

## 更新日志
- 2025.08.24 12:29 首次提交
- 2025.08.24 14:18 修复剧情bug

# Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-3.5/GPT-4/Newbing/Sakura等大语言模型的Galgame自动化翻译解决方案
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [crskycode/GARbro](https://github.com/crskycode/GARbro) :Galgame解包和打包工具
- [AtomCrafty/UniversalInjectorFramework](https://github.com/AtomCrafty/UniversalInjectorFramework.git) :实现更改字体，jis映射
- [xupefei/Locale-Emulator](https://github.com/xupefei/Locale-Emulator.git) :转区工具,使用了其中的dll

## μ-GameOperationSystem引擎 *.txt SExtractor文本提取正则
(TXT引擎+932编码+JIS替换)
```
00_skip=^\t$
05_search=^(?P<name>.+?)\s+(「.+?」)$
10_search=^\s+(.+?)$
15_search=^(.+?)$
postSkip=^[A-Za-z0-9\!\\\/\.@]
structure=paragraph
JisEncodeName=shift-jis
```
