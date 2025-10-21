# とらいあんぐるハート 外伝 gemini-2.5-pro 翻译补丁

MD5: `3927D8E6DA6440C6DCCF9C56A87C8F7A`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 注

- 本补丁基于`[020614]とらいあんぐるハート１・２・３ DVD EDITION 初回特典版`的`おまけシナリオ`制作

## 使用方法

- 1.解压压缩包并把所有文件复制到游戏根目录，双击运行`thg_chs.exe`

## Credits

- [julixian/GalTranslPP](https://github.com/julixian/GalTranslPP.git) :GalTransl的C++实现
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [julixian/MyVisualNovelTransTools](https://github.com/julixian/MyVisualNovelTransTools.git) :`IvoryTool`中的  
`IvoryCryptTool`用于加解密`*.HK2`脚本,`IvoryPkArchiveTool`用于解包和打包`*.pk`
- [【工具】API HOOK和编码处理工具包](https://www.ai2.moe/topic/29225-【工具】api-hook和编码处理工具包)
- [xupefei/Locale-Emulator](https://github.com/xupefei/Locale-Emulator.git) :转区工具,使用了其中的dll

## ivory引擎 `*.HK2` SExtractor暴提正则

(BIN引擎+CP932编码+JIS替换+截断)

```txt
00_search=^(?P<name>\x90\x5E一郎|七瀬|さくら|美緒|小鳥|唯子|忍|恭也|\x8B\x7C華|いづみ|\x90\x5E雪|ノエル|知佳|みなみ|耕介|ななか|那美|美由希|瞳|なのは|晶|桃子|レン|薫|リスティ|ゆうひ|望|愛|楓|理恵|小虎|フィアッセ|\x8F\x5C六夜|美沙斗|久遠|大輔|フィリス|火影|次郎|アンケ\x81\x5Bト|神奈|一同|ＤＪ|？？？|霊|女の子Ａ|舞|八百屋|奈緒|\x83\x7D\x83\x58\x83\x5E\x81\x5B|影虎|猫たち|ねこ|女の子Ｃ|森さん|大虎|二人|店員|女の子Ｂ|指導員|たくや|松尾|黒虎|猫|ウェイトレス|女の子たち|レン・晶|晶・レン|女の子|ＴＶ|いづみ・\x8B\x7C華|唯子・小鳥|アナウンス|工事職員|学校職員|さすけ|やまじ|チ\x81\x5Bフ|虎次郎|小飛|陽子|桃子・なのは|美由希・忍|美緒・\x90\x5E雪|那美・久遠|おばさん|美緒・舞|選手一同|受け付け|高町祖母|みみ|祖母|藤岡|虎猫)$
05_skip=^[\S\s]{0,3}$
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
