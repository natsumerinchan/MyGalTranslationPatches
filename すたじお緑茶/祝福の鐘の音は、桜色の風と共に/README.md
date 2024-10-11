# 祝福の鐘の音は、桜色の風と共に gpt-4o-2024-05-13 翻译补丁 

MD5: `B0FD8B49F5EDD1BD4D109BF14DA86531`

作者： natsumerinchan(Github) == 雨宮ゆうこ(2dfan)

未作测试，可能会出现漏翻，还请多多反馈bug！！！3q

## 使用方法
1.解压压缩包并把所有文件复制到游戏根目录，双击shukufuku_main.exe运行

# Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-3.5/GPT-4/Newbing/Sakura等大语言模型的Galgame自动化翻译解决方案
- [pkuislm/SAS5Tool](https://github.com/pkuislm/SAS5Tool.git) :SAS5的.sec5文件的反编译器和编译器
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本

### 注：
1、SAS5Tool使用新版本即可，之前打包失败的bug作者已修复

2、SExtractor文本提取正则：
```
01_search=★[^★]*★(?P<name>[^★]*)★(?P<message>.*)
sample=
☆0000000F☆☆どうやら玄関はまだ先らしい。
★0000000F★★どうやら玄関はまだ先らしい。

☆00000010☆秀治☆「こ、これが俺の、実家？」
★00000010★秀治★「こ、これが俺の、実家？」

```