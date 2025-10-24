# とらいあんぐるハート gemini-2.5-pro 翻译补丁

MD5: `64736A59E128363F486522A7582D4CBD`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 更新日志

- 2025.10.19 19:58 首次提交
- 2025.10.24 18:48 修复半角句号`｡`导致的闪退

## 注

- 本补丁基于`[020614]とらいあんぐるハート１・２・３ DVD EDITION 初回特典版`制作

## 使用方法

- 1.解压压缩包并把所有文件复制到游戏根目录，双击运行`th1_chs.exe`

## Credits

- [julixian/GalTranslPP](https://github.com/julixian/GalTranslPP.git) :GalTransl的C++实现
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [julixian/MyVisualNovelTransTools](https://github.com/julixian/MyVisualNovelTransTools.git) :`IvoryTool`中的  
`IvoryCryptTool`用于加解密`*.th1`脚本,`IvoryPkArchiveTool`用于解包和打包`*.pk`
- [【工具】API HOOK和编码处理工具包](https://www.ai2.moe/topic/29225-【工具】api-hook和编码处理工具包)
- [xupefei/Locale-Emulator](https://github.com/xupefei/Locale-Emulator.git) :转区工具,使用了其中的dll

## ivory引擎 `*.th1` SExtractor暴提正则

(BIN引擎+CP932编码+JIS替换+截断)

```txt
00_search=^(?P<name>\x90\x5E\x88\xEA\x98\x59|唯子|小鳥|いづみ|瞳|さくら|七瀬|\x8B\x7C\x89\xD8|ななか|大輔|氷村|女の子|男|３年生|火影|１年生|？？？|昂|部員|\x90\x5E\x97\x52|店員|先生|二人|一同|唯子の母|陵|先輩|男子|２年生|母親|審判|尚護|父|女の子の声|友田|藤沢|篠崎|\x90\x5E\x8B\xD5|紺袴の子|母|剣道部員|野々村父|大輔の母|同級生|なぎさ|男Ａ|痴漢|御堂さん|紺袴の人|女の人|小鳥父|小猫|男Ｂ|男の子の声|ＴＶの声|女子Ｂ|女子Ｃ|ゆ\x81\x5Bき|吉野|信田|斎藤|三人|美奈|女|コ\x81\x5Bトの男|アナウンス|おばあさん|権田原さん|２年女子|春原さん|女子Ａ|男の人|\x90\x5E\x88\xEA\x98\x4E|瞳の声|佐藤|警官|担任|青年|吉岡|\x90\x5E\x88\xEA\x98\x59・瞳|おばちゃん|瞳・\x90\x5E\x88\xEA\x98\x59|唯子・小鳥|美奈ちゃん|優しい声|白袴の子|春山さん|第３８条|綺堂さん|１年女子|唯子ママ|相川母|看護婦|第四問|男の声|綺堂|藤屋|田中|女子|教師|３人|尾崎|主審|子供|父親|全員)$
01_skip=^[\S\s]{0,3}$
10_search=^([\x81-\xFC][\S\s]+)」\x00\x0A$
15_search=^([\x81-\xFC][\S\s]+)\x00\x0A$
20_search=^([\x81-\xFC][\S\s]+)」$
25_search=^([\x81-\xFC][\S\s]+)\xFF\x6E$
30_search=^([\x81-\xFC][\S\s]+)$
checkJIS=[A-Za-z0-9\xFF\x00]
ignoreDecodeError=1
separate=(\x00\x20\xFF\x6E|\x00\x00|\x13\x00|\x00\x20)

<暴力匹配，日文仅允许双字节，单字节默认仅支持换行，如需更多半角字符请修改[\r\n]>
```
