# bitter smile. gpt-4o-2024-05-13 翻译补丁 

MD5: `01F093A735A5B8139F10587850CFB534`

作者： natsumerinchan(Github) == 雨宮ゆうこ(2dfan)

未作测试，可能会出现漏翻，还请多多反馈bug！！！3q

## 使用方法
应用条目简介评论区里的免DVD补丁后(我个人用的是dll版)，解压压缩包并把所有文件复制到游戏根目录，双击bittersmile.exe运行((无需手动转区因为UniversalInjectorFramework会自动处理))

## 更新日志
2024.10.19 13:20 修复多个会导致闪退的文本问题:
-   1. 本游戏文本的假名注释格式为`@r知世翔@ちせか@`，闪退原因是gpt-4o遇上类似假名注释时可能会漏`@`号，导致假名注释的格式不完整，我把这些假名注释全删了
-   2. 部分假名注释在句子最开头，这类假名注释没有`@r`记号，把这类假名注释删除也会报错，我手动加了回去
-   3. gpt4o把`@n` `@t`等译为了`\n` `\t` ，我批量替换了回去
-   4. 记号`@g`后面只能跟一个全角符号，gpt4o把原来的全角符号译成了半角符号

# Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-3.5/GPT-4/Newbing/Sakura等大语言模型的Galgame自动化翻译解决方案
- [ginyoushijin/GIGA_NeXAS](https://github.com/ginyoushijin/GIGA_NeXAS.git) :戏画引擎解/封包 (需配合转区软件使用，否则解包出来的bin文件名会乱码)
- [AtomCrafty/UniversalInjectorFramework](https://github.com/AtomCrafty/UniversalInjectorFramework.git) :实现自动转区和更改字体，jis映射
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本(BIN引擎+匹配规则:NeXAS+不要截断文本)
- [xupefei/Locale-Emulator](https://github.com/xupefei/Locale-Emulator.git) :转区软件,使用了其中的dll