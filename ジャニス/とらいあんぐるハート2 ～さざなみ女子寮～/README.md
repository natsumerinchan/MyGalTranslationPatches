# とらいあんぐるハート2 ～さざなみ女子寮～ gemini-2.5-pro 翻译补丁

MD5: `906FFFF9B27062269CB64E1105D97BEA`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 注

- 本补丁基于`[020614]とらいあんぐるハート１・２・３ DVD EDITION 初回特典版`制作

## 使用方法

- 1.解压压缩包并把所有文件复制到游戏根目录，双击运行`th2_chs.exe`

## Credits

- [julixian/GalTranslPP](https://github.com/julixian/GalTranslPP.git) :GalTransl的C++实现
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [julixian/MyVisualNovelTransTools](https://github.com/julixian/MyVisualNovelTransTools.git) :`IvoryTool`中的  
`IvoryCryptTool`用于加解密`*.th2`脚本,`IvoryPkArchiveTool`用于解包和打包`*.pk`
- [【工具】API HOOK和编码处理工具包](https://www.ai2.moe/topic/29225-【工具】api-hook和编码处理工具包)
- [xupefei/Locale-Emulator](https://github.com/xupefei/Locale-Emulator.git) :转区工具,使用了其中的dll

## ivory引擎 `*.th2` SExtractor暴提正则

(BIN引擎+CP932编码+JIS替换+截断)

```txt
00_search=^(?P<name>耕介|知佳|ゆうひ|愛|\x90\x5E\x90\xE1|薫|みなみ|美緒|\x8F\x5C\x98\x5A\x96\xE9|リスティ|ななか|瞳|望|御架月|？？？|神奈|矢沢|佐波田|さとみ|国見|神主|次郎|裕子|小虎|猫|理恵|\x98\x61\x90\x5E|女の子|子供|店員|里香子|巫女|女性|新聞少年|\x90\x5E一郎|\x90\x5E由|母|男の子|椎名|医師|\x8C\x5B\x8C\xE1|エルシ\x81\x5B|山村|編集|クロ\x81\x5Bン|中村|森田|望母|ことら|刑事|男|子猫|一同|麗|尾崎|石原|柳|劉|お客|大川|警官|修平|滝|また別の男|スカウト|バ\x81\x5Bテン|女の子Ｂ|おやじ|テレビ|\x89\xC1\x94\x5B|ねこ|受付|部屋|月緒|\x81\x79\x8F\x5C\x98\x5A\x96\xE9\x81\x7A|中年医師|女の子Ｃ|中年男性|女の子Ａ|老医師|\x89\x5E\x93\x5D\x8E\xE8|６番|父|みなみの友達|声をかけた男|ウィンディ|ウインディ|別の女性|女性職員|由紀子|ツバメ|母親|記者|医者|案内|杏子|校長|弘|謎の機械音|ファックス|\x90\x5E雪・耕介|更に別の男|矢沢医師|問題４８|耕介・薫|問題４５|問題４６|問題４７|いたち|整備員|別の男|謎の音|あかげ|子供達|依頼人|うひ|手紙|文鳥|部下|電話|黒虎|ひよ|メモ|鳥)$
05_skip=^[\S\s]{0,3}$
06_skip=^(凄嚢I|∫綺7)$
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
