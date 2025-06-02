# 初恋サクラメント gemini-2.5-pro-exp-03-25 翻译补丁

MD5: `63DA51EFEDF009436EB0D8EB69A8BF7D`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 使用方法
- 1.安装修正补丁v1.01
- 2.解压压缩包并把所有文件复制到游戏根目录，安装字体后转区运行cmvs32_chs.exe
- 3.游戏中修改字体为VL ゴシック

## 更新日志
- 2025.06.02 15:22 首次提交

# Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-3.5/GPT-4/Newbing/Sakura等大语言模型的Galgame自动化翻译解决方案
- [amayra/arc_conv](https://github.com/amayra/arc_conv.git) :由 w8m 使用纯 ASM 编写的命令行视觉小说工具包
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [ZQF-ReVN/RxCMVS](https://github.com/ZQF-ReVN/RxCMVS.git) :CMVS引擎脚本处理(用最新版)、hook工具(git reset --hard到4c9f2874c65c702e47e109e38ea91a060c953c3c并编辑CMVSVersion.h改为使用对应游戏的配置)
- 补丁测试及gemini额度提供： [伪恶君子333@御爱同萌](https://www.ai2.moe/profile/9569-伪恶君子333/)

### PS3_TextEditor json SExtractor文本提取正则(TXT引擎+UTF-8-SIG编码+JIS替换+导出时name向上移动一位)
```
00_search=^\s\s*"tra":\s*"(?P<name>勇飛|ヒカリ|岬|星見|いろは|文雪)"$
05_search=^\s\s*"tra":\s*"(?P<name>ノア|鏡香|樹|旭|ユダ|真一|由梨)"$
10_search=^\s\s*"tra":\s*"(?P<name>摩子|楓|姫|内海|夜咲|山下|？？？)"$
15_search=^\s\s*"tra":\s*"(?P<msg>.+)"$
postSkip=^[A-Za-z\-]
structure=paragraph
```

### arc_conv .cpz(cpz5) 解包命令
```
.\arc_conv.exe --dest .\script --unpack cpz5 .\script.cpz
.\arc_conv.exe --dest .\update --unpack cpz5 .\update.cpz
```