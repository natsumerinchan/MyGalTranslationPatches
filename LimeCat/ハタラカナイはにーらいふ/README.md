# ハタラカナイはにーらいふ gpt-4o-2024-05-13 翻译补丁

MD5: `DA932B9BF4D4029943C5BA5EBC321AE0`

作者： natsumerinchan(Github) == 雨宮ゆうこ(2dfan)

未作完整测试，可能会出现漏翻，还请多多反馈bug！！！3q

## 使用方法
1.解压压缩包并把所有文件复制到游戏根目录，双击hatahani_gpt4o.exe运行

# Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-3.5/GPT-4/Newbing/Sakura等大语言模型的Galgame自动化翻译解决方案
- [xmoezzz/KrkrExtract](https://github.com/xmoezzz/KrkrExtract.git) :krkr引擎xp3解包功能,以及Universal Patch
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [Enigma Virtual Box](https://enigmaprotector.com/assets/files/enigmavb.exe) :把脚本文件打包进exe

### SExtractor 未加密*.scn文本提取正则

```
01_search=^@【(?P<name>.*?)】$
02_skip=^[;*@#_A-Za-z0-9]
03_search=^(?P<msg>.+」)$
04_search=^(?P<unfinish>.+)$
```

### Enigma Virtual Box 打包内容
- 输出名: hatahani_gpt4o.exe
- 主程序: hatahani_patch.exe (由KrkrExtract生成)
- 其它文件内容:
    - ProjectDir :文件夹，可存放脚本、图片等文件，里面不可有文件夹
    - hatahani.exe :游戏原主程序，避免EVB认为执行hatahani_patch.exe后程序就结束了
    - KrkrUniversalPatch.dll :(由KrkrExtract生成)
- 属性设置:
    - %DEFAULT FOLDER%和ProjectDir设置为`New Folders and Files Become Virtual`
    - hatahani.exe设置为`从不写入磁盘`
    - KrkrUniversalPatch.dll设置为`写入磁盘(如果不存在)`
