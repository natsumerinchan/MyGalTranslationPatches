# 恋のハニトー ～えっちで甘いハニートラップ～ gpt-4o-2024-05-13 翻译补丁

MD5: `DAD046E0E9092DD1BDA875CF72971942`

作者： natsumerinchan(Github) == 雨宮ゆうこ(2dfan)

未作完整测试，可能会出现漏翻，还请多多反馈bug！！！3q

## 使用方法
1.解压压缩包并把所有文件复制到游戏根目录，双击KOI_HONY.EXE运行

## 已知问题
1.SExtractor开了截断，有的文本缺失属正常现象

# Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-3.5/GPT-4/Newbing/Sakura等大语言模型的Galgame自动化翻译解决方案
- [nanami5270/GARbro-Mod](https://github.com/nanami5270/GARbro-Mod.git) :Galgame解包和打包工具
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本

### SExtractor *.tob暴力提取正则（name会被匹配为msg）

```
00_skip=^[\S\s]{0,3}$
10_search=^([\x81-\xFC][\S\s]+)$
checkJIS=[\r\n]
ignoreDecodeError=1
separate=(\x00|\xFF|\x5B\x20\x0C|\x5B\x20\x0E|\x5B\x20\x1D)
sample=
<暴力匹配，日文仅允许双字节，单字节符号按正则匹配[\r\n]>
```
