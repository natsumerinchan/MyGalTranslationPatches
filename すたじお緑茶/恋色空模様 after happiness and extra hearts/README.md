# 恋色空模様 after happiness and extra hearts gpt-4o-2024-05-13 翻译补丁 

MD5: `31E4C6FD168CF2E3EE646CCEF9FA58B0`

作者： natsumerinchan(Github) == 雨宮ゆうこ(2dfan)

未作测试，可能会出现漏翻，还请多多反馈bug！！！3q

## 使用方法
1.解压压缩包并把所有文件复制到游戏根目录，双击koisora_ex_main.exe运行

# Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-3.5/GPT-4/Newbing/Sakura等大语言模型的Galgame自动化翻译解决方案
- [pkuislm/SAS5Tool](https://github.com/pkuislm/SAS5Tool.git) :SAS5的.sec5文件的反编译器和编译器
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本

### 注：
SExtractor文本提取正则：
```
01_search=★[^★]*★(?P<name>[^★]*)★(?P<message>.*)
sample=
☆00000004☆誠悟☆「分かってるって」
★00000004★誠悟★「分かってるって」

☆00000005☆☆まだ始まったばかりで、お客さんの姿はまばらだ。
★00000005★★まだ始まったばかりで、お客さんの姿はまばらだ。

```