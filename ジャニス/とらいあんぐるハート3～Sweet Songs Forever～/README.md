# とらいあんぐるハート3～Sweet Songs Forever～ gemini-2.5-pro 翻译补丁

MD5: `BD47AFB2817C22DA978EFCCE38917A14`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 注

- 本补丁基于`[020614]とらいあんぐるハート１・２・３ DVD EDITION 初回特典版`，  
旧补丁基于`[001208]	とらいあんぐるハート３ ～Sweet Songs Forever～ 通常版`制作。

## 使用方法

- 1.解压压缩包并把所有文件复制到游戏根目录，双击运行`th3_chs.exe`

## Credits

- [julixian/GalTranslPP](https://github.com/julixian/GalTranslPP.git) :GalTransl的C++实现
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [julixian/MyVisualNovelTransTools](https://github.com/julixian/MyVisualNovelTransTools.git) :`IvoryTool`中的  
`IvoryCryptTool`用于加解密`*.TH3`脚本,`IvoryPkArchiveTool`用于解包和打包`*.pk`
- [【工具】API HOOK和编码处理工具包](https://www.ai2.moe/topic/29225-【工具】api-hook和编码处理工具包)
- [xupefei/Locale-Emulator](https://github.com/xupefei/Locale-Emulator.git) :转区工具,使用了其中的dll

## ivory引擎 `*.TH3` SExtractor暴提正则

(BIN引擎+CP932编码+JIS替换+截断)

```txt
00_search=^(?P<name>恭也|晶|美由希|レン|忍|那美|フィアッセ|なのは|ノエル|桃子|久遠|美沙斗|フィリス|赤星|アリサ|ティオレ|？？？|薫|弥太|イレイン|さくら|鷹城先生|ゆうひ|ねこ|男|安次郎|狐|女の子|巫女さん|リスティ|愛|士郎|松尾|晶・レン|こねこ|和音|声|瑞乃|女性|女の人|巻島|子猫|お客さん|小飛|ゲ\x81\x5Bム|医師|一同|アイリ\x81\x5Bン|レン・晶|\x90\x5E雪|主|おばちゃん|ＳＥＥＮＡ|店員さん|葉\x8B\x7C|静馬|猫|雫|\x83\x8A\x83\x7C\x81\x5B\x83\x5E\x81\x5B|晶の友達|女の子Ｂ|みずの|加代子|雛村|教師|ＴＶ|小梅|刑事|店員|楓|女の子Ａ|とら猫|藤代|宮司|おっちゃん|イレイン３|バイトの子|男の子|テレビ|母親|男子|子狐|隆平|イレイン５|アナウンス|クレスビ\x81\x5B|イレイン１|レンの友達|イレイン４|かよっち|神咲さん|ナハト|ぎんが|灰色猫|女子|雪虎|二人|老女|老人|犬|バイト店員|女の子たち|ティ\x81\x5Bニャ|晶・なのは|リ\x81\x5Bファ|寮生一同|海中教師|学級委員|学年主任|男の子達|アリシア|\x83\x41\x83\x80\x83\x8A\x83\x5E|女子たち|女の子達|マリ\x81\x5B|バイト|エレン|ひなこ|イリア|なつみ|お嬢様|Ｄ\x00.Ｋ|北斗|子供|恵子|ＡＤ)$
05_skip=^[\S\s]{0,3}$
10_search=^([\x81-\xFC][\S\s]+)」\x00\x0A$
15_search=^([\x81-\xFC][\S\s]+)\x00\x0A$
20_search=^([\x81-\xFC][\S\s]+)」$
25_search=^([\x81-\xFC][\S\s]+)\xFF\x6E$
30_search=^([\x81-\xFC][\S\s]+)$
checkJIS=[\x20-\x7E\xFF\x00]
ignoreDecodeError=1
separate=(\x00\x20\xFF\x6E|\x00\x00|\x13\x00|\x00\x20)

<暴力匹配，日文仅允许双字节，单字节默认仅支持换行，如需更多半角字符请修改[\r\n]>
```
