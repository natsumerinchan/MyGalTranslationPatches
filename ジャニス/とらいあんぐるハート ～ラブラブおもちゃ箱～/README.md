# とらいあんぐるハート ～ラブラブおもちゃ箱～ gemini-2.5-pro 翻译补丁

MD5: `25B95EEF802A297AFD2CBC0A8ED22FDC`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 注

- 本补丁基于`[020614]とらいあんぐるハート１・２・３ DVD EDITION 初回特典版`制作

## 使用方法

- 1.解压压缩包并把所有文件复制到游戏根目录，双击运行`hk1_chs.exe`

## Credits

- [julixian/GalTranslPP](https://github.com/julixian/GalTranslPP.git) :GalTransl的C++实现
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [julixian/MyVisualNovelTransTools](https://github.com/julixian/MyVisualNovelTransTools.git) :`IvoryTool`中的  
`IvoryCryptTool`用于加解密`*.TH2`脚本,`IvoryPkArchiveTool`用于解包和打包`*.pk`
- [【工具】API HOOK和编码处理工具包](https://www.ai2.moe/topic/29225-【工具】api-hook和编码处理工具包)
- [xupefei/Locale-Emulator](https://github.com/xupefei/Locale-Emulator.git) :转区工具,使用了其中的dll

## ivory引擎 `*.TH2` SExtractor暴提正则

(BIN引擎+CP932编码+JIS替换+截断)

```txt
00_search=^(?P<name>\x90\x5E一郎|雪|小虎|美緒|次郎|耕介|みなみ|知佳|ゆうひ|薫|\x90\x5E雪|愛|リスティ|七瀬|瞳|さくら|唯子|いづみ|\x8F\x5C六夜|小鳥|御架月|\x8B\x7C華|ななか|望|裕子|\x8A\x5B|女の人|猫|焼肉屋の親父|店員|？？？|氷那|\x83\x7D\x83\x58\x83\x5E\x81\x5B|ことら|あかげ|黒影|一同|子猫|子供|みみ|バスケ部員達|ぎんめ|さんざし|やまじ|ゆっこ|女の子|ざから|さすけ|医師|ゴマ|柳|みなみ・子供|耕介・\x90\x5E一郎|唯子・美緒|\x90\x5E雪・薫|薫・耕介|審判|哲平|触手|全員|二人|３人)$
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
