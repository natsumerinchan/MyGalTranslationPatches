# 夏色あさがおレジデンス gemini-3-pro-preview 翻译补丁

MD5: `6FDFA1CE8B52DDF220E617FB3946B12A`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 使用方法

- 1.解压压缩包并把`Releases`文件夹内所有文件复制到游戏根目录，双击运行`夏色あさがおレジデンス_CHS.exe`

## Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-3.5/GPT-4/Newbing/Sakura等大语言模型的Galgame自动化翻译解决方案
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [yanhua0518/GALgameScriptTools](https://github.com/yanhua0518/GALgameScriptTools.git) :SiglusEngine解包和打包工具
- [natsumerinchan/CELICA_HOOK](https://github.com/natsumerinchan/CELICA_HOOK.git) :个人写的游戏程序hook工具
- 补丁测试人员： [伪恶君子333@御爱同萌](https://www.ai2.moe/profile/9569-伪恶君子333/)

## SiglusTools *.txt SExtractor文本提取正则

(TXT引擎+utf-8编码+生成jis替换配置)

```md
00_skip=^●\d+●\d{2}_
05_skip=^●\d+●[\u3040-\u309F・]{2,}$
06_skip=^●\d+●(タマ)$
07_skip=^●\d+●\s+$
10_search=^●\d+●(?P<name>渡|景|明|玲|周平|雛子|葉月|キキ|真白|軍司|羽鳥|男子生徒|女子生徒|書記局|一同|渡／周平|渡／周平／景|明・雛子・キキ・葉月|景・渡・周平|景・渡・周平|雛子・キキ・葉月|景・周平|生物研|葉月・キキ・玲|玲／雛子|明・葉月|店員|景／雛子|葉月・キキ|軍司・羽鳥|雛子・父|キキ／葉月|葉月／渡|？？？|葉月／キキ|明／キキ／葉月|新聞部|生徒達|ハト|マジック研|観客|バレー部|電子戦研究会|正す会リーダー|バレー部女子|主将|ドラゴンのＳＥ|ロボのＳＥ|バレー部男子|放送部|正す会|モブＡ|モブＢ|演劇部|水泳部|さくらの皆さん|写真の男子|参加者達|被害者達|参加者達|教師|葉月／雛子|渡／葉月|神社生まれのＧさん|雛子／葉月|ギャラリー|キキ／渡|男子達|葉月／周平／渡|渡／雛子|見物人達|男子生徒達|景／軍司|バトミントン部|バスケ部|いじめっ子)$
15_search=^●\d+●(?P<end_unfinish>「.+?」|選択肢)$
20_search=^●\d+●(?P<end_unfinish>≪.+?≫)$
25_search=^●\d+●(?P<end_unfinish>[^「].+?」)$
30_search=^●\d+●(?P<end_unfinish>[^「].+?[。？！－]{1})$
35_search=^●\d+●(?P<pre_unfinish>」)$
40_search=^●\d+●(?P<end_unfinish>[。？！－]{1})$
45_search=^●\d+●(?P<start_unfinish>「)$
50_search=^●\d+●(?P<start_unfinish>「.+?[^」].+?)$
55_search=^●\d+●(?P<pre_unfinish>\s+.+?)$
60_search=^●\d+●(?P<unfinish>.+?)$
skipIgnoreUnfinish=True
structure=paragraph
```
