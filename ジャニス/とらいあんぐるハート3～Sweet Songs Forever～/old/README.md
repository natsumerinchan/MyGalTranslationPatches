# とらいあんぐるハート3～Sweet Songs Forever～ gemini-2.5-pro 翻译补丁

MD5: `174E83B22F515D7C86188EF24DBCCF1D`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 使用方法

- 1.解压压缩包并把所有文件复制到游戏根目录，双击运行`TH3_CHS.EXE`

## 更新日志

- 2025.10.15 20:42 首次提交
- 补充main004.th3漏翻的内容并解决美由希线半角句号导致的闪退

## Credits

- [julixian/GalTranslPP](https://github.com/julixian/GalTranslPP.git) :GalTransl的C++实现
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [julixian/MyVisualNovelTransTools](https://github.com/julixian/MyVisualNovelTransTools.git) :`IvoryTool`中的  
`IvoryCryptTool`用于加解密`*.hk2`脚本,本作用`IvoryScriptSimpleTool`提取和导入文本时有bug故改用SE暴提截断提取文本
- [【工具】API HOOK和编码处理工具包](https://www.ai2.moe/topic/29225-【工具】api-hook和编码处理工具包)
- [xupefei/Locale-Emulator](https://github.com/xupefei/Locale-Emulator.git) :转区工具,使用了其中的dll

## ivory引擎 `*.th3` SExtractor暴提正则

(BIN引擎+CP932编码+JIS替换+截断)

```txt
00_skip=^[\S\s]{0,3}$
01_skip=^(囮|ﾈB|@|漾|ﾀ@|ｵ|豸|､|ﾈA|ﾌ+|桷|｢ｳ|ﾎﾌ|ｾﾎ|ﾔ|顯|ﾆ|｢|ﾘ|ｪJ|ｲl|ｺｴ|ｴﾐ|ﾉ|ﾍﾌL?)
02_skip=(\x03|\x1E|\x05|\x12|\r|\x0E|\x15|>|\x00｣|\x0B|\x1c|\x01|\x02)$
03_skip=(\x14|\x19|\x04|\x17|\x1D|\x00\/|\*|\t)$
04_search=^(?P<name>恭也|晶|美由希|レン|忍|那美|フィアッセ|なのは|ノエル|桃子|久遠|美沙斗|フィリス|赤星|アリサ|ティオレ|？？？|薫|弥太|イレイン|さくら|鷹城先生|ゆうひ|ねこ|男|安次郎|狐|女の子|巫女さん|リスティ|愛|士郎|松尾|晶・レン|こねこ|和音|声|瑞乃|女性|女の人|巻島|子猫|お客さん|小飛|ゲ\x81\x5Bム|医師|一同|アイリ\x81\x5Bン|レン・晶|真雪|主|おばちゃん|ＳＥＥＮＡ|店員さん|葉弓|静馬|猫|雫|リポ\x81\x5Bタ\x81\x5B|晶の友達|女の子Ｂ|みずの|加代子|雛村|教師|ＴＶ|小梅|刑事|店員|楓|女の子Ａ|とら猫|藤代|宮司|おっちゃん|イレイン３|バイトの子|男の子|テレビ|母親|男子|子狐|隆平|イレイン５|アナウンス|クレスビ\x81\x5B|イレイン１|レンの友達|イレイン４|かよっち|神咲さん|ィオレ|ナハト|ぎんが|灰色猫|女子|雪虎|二人|老女|老人|犬|バイト店員|女の子たち|ティ\x81\x5Bニャ|晶・なのは|リ\x81\x5Bファ|寮生一同|海中教師|学級委員|学年主任|男の子達|アリシア|アムリタ|女子たち|女の子達|マリ\x81\x5B|バイト|エレン|ひなこ|イリア|なつみ|お嬢様|Ｄ.Ｋ|俺は|北斗|子供|恵子|ＡＤ|あれ)$
05_search=^([\x81-\xFC][\S\s]+)」\x00\x0A$
10_search=^([\x81-\xFC][\S\s]+)\x00\x0A$
15_search=^([\x81-\xFC][\S\s]+)」$
20_search=^([\x81-\xFC][\S\s]+)\xFF\x6E$
25_search=^([\x81-\xFC][\S\s]+)$
ignoreDecodeError=1
separate=(\x00\x20\xFF\x6E|\x00\x00|\x13\x00|\x00\x20)
keepBytes=auto

<暴力匹配，日文仅允许双字节，单字节默认仅支持换行，如需更多半角字符请修改[\r\n]>
```
