# 南十字星恋歌 gpt-4o-2024-05-13 翻译补丁 

MD5: `016FC653AC3FB80EF6217DE8B17E38E9`

作者： natsumerinchan(Github) == 雨宮ゆうこ(2dfan)

未作测试，可能会出现漏翻，还请多多反馈bug！！！3q

## 使用方法
1.解压压缩包并把所有文件复制到游戏根目录，双击nankoi_main.exe运行

# Credits

- [GalTransl/GalTransl](https://github.com/GalTransl/GalTransl.git) :支持GPT-4/Claude/Deepseek/Sakura等大语言模型的Galgame自动化翻译解决方案
- [pkuislm/SAS5Tool](https://github.com/pkuislm/SAS5Tool.git) :SAS5的.sec5文件的反编译器和编译器
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本

### 注：
1、SAS5Tool我回退到了commit:`a4186178ba52d19e90903d4daf132072d0f0e03d`，因为最新版本打包南十字的文本时会报错

2、SExtractor文本提取正则：
```
01_search=★[^★]*★(?P<name>[^★]*)★(?P<message>.*)
sample=
☆00000004☆亮輔☆「はぐれた」
★00000004★亮輔★「はぐれた」

☆00000005☆☆初めてやってきた海外に浮き足立っていた俺は、物珍しさもあって辺りを見渡していた。
★00000005★★初めてやってきた海外に浮き足立っていた俺は、物珍しさもあって辺りを見渡していた。

```