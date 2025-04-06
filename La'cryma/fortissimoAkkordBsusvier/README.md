# fortissimo//Akkord:Bsusvier gpt4o-2024-11-20 翻译补丁

MD5: `7464294AAA9BA6EEE42E20A443581002`

作者： natsumerinchan(Github) == 雨宮ゆうこ

未完整测试。有bug请反馈（截图加私发存档）

## 使用方法
- 1.安装fortissimoexa_patch99_fix
- 2.解压压缩包并把所有文件复制到游戏根目录，双击fortissimo_exa_CHS.exe运行

# Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-3.5/GPT-4/Newbing/Sakura等大语言模型的Galgame自动化翻译解决方案
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [regomne/lneditor](https://github.com/regomne/lneditor.git) :翻译人员专用的多行编辑器(使用其批量导出导入功能)
- [Enigma Virtual Box](https://enigmaprotector.com/assets/files/enigmavb.exe) :把脚本文件打包进exe
- [AtomCrafty/UniversalInjectorFramework](https://github.com/AtomCrafty/UniversalInjectorFramework.git) :实现更改字体，jis映射
- [xupefei/Locale-Emulator](https://github.com/xupefei/Locale-Emulator.git) :转区工具,使用了其中的dll

### lneditor Circus社旧版引擎插件 SExtractor文本提取正则
(TXT引擎+UTF-16编码+生成JIS替换配置)
```
00_search=^(?P<name>\$n)$
01_search=^(?P<pre_nameANDmsg>「.+」)$
02_search=^　\\n　\\n　\\n　\\n　\\n　\\n　\\n(?P<name>[^\\n].+?)\\n(「.+」)$
03_search=^　\\n　\\n　\\n　\\n　\\n　\\n　\\n(.+)$
04_search=^　\\n　(?P<name>.+?)\\n(「.+」)$
06_search=^　(?P<name>.+?)\\n(「.+」)$
08_search=^(?P<name>[^\\n].+?)\\n(「.+」)$
09_search=^　\\n(.+)$
10_search=^(.+)$
structure=paragraph
```

### 翻译时踩过的坑
- 1、数字和英文字母必须用全角字符，否则无法导入文本
- 2、旧版Circus引擎每26个字后面必须有一个换行符，否则文字会超出显示范围
(可使用galtransl的text_common_lineBreakFix插件并使用固定字数模式，换行阈值可以设置保守些)
- 3、lneditor导入文本时多点几次导入，否则插件很大概率会抽风漏导入一些译文
