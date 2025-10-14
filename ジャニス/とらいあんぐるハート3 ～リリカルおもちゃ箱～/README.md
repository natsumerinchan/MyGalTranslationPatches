# とらいあんぐるハート3 ～リリカルおもちゃ箱～ gemini-2.5-pro 翻译补丁

MD5: `298782B0C1049C437D9E447B4F24F853`

作者： natsumerinchan(Github) == 雨宮ゆうこ

とらいあんぐるハート3～Sweet Songs Forever～的FD， 《魔法少女奈叶》的前身。  
目前只翻了FD，本篇等明天下午gemini额度重置后再翻。

## 注

- 1、问答闯关相关内容未翻译

## 使用方法

- 1.解压压缩包并把所有文件复制到游戏根目录，双击运行`HAKO2_CHS.EXE`

## Credits

- [julixian/GalTranslPP](https://github.com/julixian/GalTranslPP.git) :GalTransl的C++实现
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [julixian/MyVisualNovelTransTools](https://github.com/julixian/MyVisualNovelTransTools.git) :`IvoryTool`中的  
`IvoryCryptTool`用于加解密`*.hk2`脚本,本作用`IvoryScriptSimpleTool`提取和导入文本时有bug故改用SE暴提截断提取文本
- [【工具】API HOOK和编码处理工具包](https://www.ai2.moe/topic/29225-【工具】api-hook和编码处理工具包)
- [xupefei/Locale-Emulator](https://github.com/xupefei/Locale-Emulator.git) :转区工具,使用了其中的dll

## ivory引擎 `*.hk2` SExtractor暴提正则

(BIN引擎+CP932编码+JIS替换+截断)

```txt
00_skip=^[\S\s]{0,3}$
01_skip=^(ﾈB|@|漾|ﾀ@|ｵ|豸|､|ﾈA|ﾌ+|桷|｢ｳ|ﾎﾌ|ｾﾎ|ﾔ|顯|ﾆ|｢|ﾘ|ｪJ|ｲl|ｺｴ|ｴﾐ|ﾉ)
02_skip=(\x03|\x1E|\x05|\x12|\r|\x0E|\x15|>|\x00｣|\x0B)$
03_skip=(\x14|\x19|\x04|\x17|\x1D|\x00\/|\*|\t)$
04_search=^(?P<name>なのは|桃子|美由希|恭也|クロノ|忍|フィリス|晶|レン|リンディ|久遠|那美|フィアッセ|美沙斗|士郎|美緒|ななか|リスティ|ノエル|アイリ\x81\x5Bン|さくら|井上|薫|みずの|愛|唯子|女性|赤星|ゆうひ|？？？|アルバ\x81\x5Bト|黒い男の子|男|おじさん|真雪|ティオレ|松尾|看護婦|ねこ|女の子|小飛|猫|舞|声|レポ\x81\x5Bタ\x81\x5B|店員|ひなこ|支配人|女の人|側近|二人|隆弘|外人|店長|啓吾|機械|警備員|男の子|篠田|コロッケ屋|晶・レン|ゴ\x81\x5Bスト|八百屋|観客|子猫|一同|刑事|雪虎|アナウンス|桃子の母|女の子Ａ|タクシ\x81\x5B|運転手|ぎんが|司会|警備長|コック|奥様|親戚|静馬|犬|印刷店店主|ワグナ\x81\x5B|看護婦Ａ|女の子Ｃ|女の子Ｂ|救急隊員|全機械|征二|母親|知佳|医師|敗者|警備|三人|飛鳥|鳥|たこ焼き屋|とらじま猫|お巡りさん|和食料理長|コック一同|中華料理長|レフェリ\x81\x5B|看護婦Ｂ|小さな声|女性秘書|会談相手|レン・晶|舞・美緒|レン・忍|スタッフ|看護婦Ｃ|側近Ｃ|対戦者|家政婦|側近Ｂ|側近Ａ|こねこ|参拝客|やまね|機械２|機械３|灰色猫|赤虎|患者|耕介|秘書|女子|洋猫|花乃|和真|北斗|虎鉄)$
05_search=^([\x81-\xFC][\S\s]+)」\x00\x0A$
10_search=^([\x81-\xFC][\S\s]+)\x00\x0A$
15_search=^([\x81-\xFC][\S\s]+)」$
20_search=^([\x81-\xFC][\S\s]+)$
ignoreDecodeError=1
separate=(\x00\x00|\x13\x00)
keepBytes=auto

<暴力匹配，日文仅允许双字节，单字节默认仅支持换行，如需更多半角字符请修改[\r\n]>

```
