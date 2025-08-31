# ミニパイくれ～ま～ ～文句を言いたいのにおっぱいが感じちゃう～ gemini-2.5-pro 翻译补丁 

MD5: `90D8AE6CF13D3FF8B20EDD1430BA938D`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 使用方法
- 1.解压压缩包并把所有文件复制到游戏根目录，双击运行GAME_SYS_CHS.EXE

# Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-3.5/GPT-4/Newbing/Sakura等大语言模型的Galgame自动化翻译解决方案
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本(Kaguya引擎+截断+JIS替换)
- [【工具】API HOOK和编码处理工具包](https://www.ai2.moe/topic/29225-【工具】api-hook和编码处理工具包)
- [xupefei/Locale-Emulator](https://github.com/xupefei/Locale-Emulator.git) :转区工具,使用了其中的dll

## TBLSTR.json 二次提取正则
(JSON引擎+UTF-8编码+不进行JIS替换)
```
10_search=(?P<unfinish>[^@a-zA-Z0-9－/\r\n\t ]+)
```

## 踩坑过程
- 1、本作需要截断（善用galtransl的AdditionalPrompt功能命其“译文字数不得超过原文”，多刷几次，最后再手动缩短少量仍然比原文长的译文即可）
- 2、换行符位置不能变（仓库内有对二次提取json译文进行处理的python脚本,使\r\n的位置保持与原文一致，字数不够会填充全角空格，<br>
少数几处原文夹带半角字符会影响脚本对字数的判断，需在截断时手动删全角空格直到无截断警告）
- 3、每行字数不得超过26个字（满足1和2的话则不可能有机会触发）
