# Princess Party～プリンセスパーティー～ gpt4o-2024-11-20+DeepSeek-V3 翻译补丁 v1.0.0

MD5: `61485F932D8B945159A42AB215FB0995`

作者： natsumerinchan(Github) == 雨宮ゆうこ

未完整测试。有bug请反馈（截图加私发存档）

## 使用方法
- 1.安装修正补丁v1.01
- 2.解压压缩包并把所有文件复制到游戏根目录，双击PURIPA_CN.exe运行

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
01_search=^(?P<pre_nameANDmsg>「.+」)$
02_search=^　(.+)$
03_search=^(.+)$
structure=paragraph
```

### 翻译时踩过的坑
- 1、数字和英文字母必须用全角字符，否则无法导入文本
- 2、旧版Circus引擎每21个字后面必须有一个换行符，否则文字会超出显示范围
- 3、lneditor导入文本时多点几次导入，否则插件很大概率会抽风漏导入一些译文
