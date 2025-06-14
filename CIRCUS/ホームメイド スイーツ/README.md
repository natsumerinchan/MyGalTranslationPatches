# ホームメイド スイーツ claude-3-7-sonnet 翻译补丁

MD5: `4BA4A3454C0B90052FD18BBD58B680EC`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 使用方法
- 1.将压缩包内所有文件解压至游戏根目录，双击运行HMSW_CHS.EXE(已改GBK编码无需转区)

## DLL源码
https://github.com/natsumerinchan/circus_hook.git

# Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-3.5/GPT-4/Newbing/Sakura等大语言模型的Galgame自动化翻译解决方案
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [cokkeijigen/MesTextTool](https://github.com/cokkeijigen/MesTextTool.git) :CIRCUS引擎*.mes脚本处理工具
- [CFF_Explorer 8.0 汉化版](https://bbs.kanxue.com/thread-158547-1.htm) :PE工具，可用于便捷修改dll导入表

### MesTextTool *.txt SExtractor文本提取正则
(TXT引擎+UTF-8编码+不生成JIS替换配置)
```
00_search=^★.+?★(?P<name>芹人|藤|桜美|蓮奈|クララ|桂花|水蓮|楓|あやめ|くらら|理事)$
01_search=^★.+?★(?P<name>謙太郎|克比古|桂|すず|森少尉|目黒|函南|昭浩|メリッサ|男の子)$
02_search=^★.+?★(?P<name>正樹|桜実|速水卿|浜路|茉莉|晃次|芹杜|男|長瀞|母|司会者|楓の声)$
03_search=^★.+?★(?P<name>ミセス・ヨーコ|岩崎|啓祐|ディビッド|メイド|岬|樹|島岡|くま坂)$
04_search=^★.+?★(?P<name>メイド１|メイド２|ウィロビー卿|イリス|旦那様|谷部|継母|使用人Ｄ)$
05_search=^★.+?★(?P<name>マーカス卿|客|？？？|父|犯人|三ツ峰翁|ホルスト|鈴原卿|少女)$
06_search=^★.+?★(?P<name>美術教師|使用人|女性|娼婦達|少年|紳士|男子学生|店主|担任)$
07_search=^★.+?★(?P<name>世界史教師|運転手|審査委員長|速水卿の声|ふみ乃|医師|暴徒)$
08_search=^★.+?★(?P<name>日本史教師|桜美の声|蓮奈の声|男子寮生|紳士Ｂ|進行役|父親)$
09_search=^★.+?★(?P<name>紳士Ａ|令嬢Ａ|子供|化学教師|小学生|函南のメイド|教師|桂の声)$
10_search=^★.+?★(?P<name>女子学生|アナウンサー|駅員|先生|メイド長|娼婦|アナウンス|毅)$
11_search=^★.+?★(?P<name>男子学生Ａ|学生たち|サーバント科の学生|審査委員Ｂ|令嬢Ｂ)$
12_search=^★.+?★(?P<name>浜路の声|女の子|店員|谷部の声|あやめの声|司会|インタビュアー)$
13_search=^★.+?★(?P<name>中継|女子学生Ａ|使用人Ａ|使用人Ｂ|使用人Ｅ|審査委員Ａ|男の声)$
14_search=^★.+?★(?P<name>学生|同級生|藤の声|コメンテーター|クララの声|犬|クラスメイト)$
15_search=^★.+?★(?P<name>使用人Ｃ|長瀞の声|通行人|配達員|女子Ａ|岩崎の声|一同|僕|紳士Ｃ)$
16_search=^★.+?★(?P<name>茉莉＆啓祐|茉莉・啓祐|子供の声|子供たち|茉莉の声|メイドたち)$
17_search=^★.+?★(?P<name>芹人・目黒|体育教師|函南の声|男子学生Ｂ|男子学生Ｃ|配達員Ａ)$
18_search=^★.+?★(?P<name>ガードマン|従業員|ホテル従業員|女子学生１|女子学生２|教師Ａ)$
19_search=^★.+?★(?P<name>藤・桜美|男子学生１|男三人|使用人たち|野次馬たち|目黒＆芹人)$
20_search=^★.+?★(?P<name>芹人・クララ|女子Ｂ|女学生たち|女子|女子学生一同|蓮奈・水蓮)$
25_search=^★.+?★@[a-z](.+?)@n$
30_search=^★.+?★@[a-z](.+?)$
35_search=^★.+?★\s+(.+?)$
40_search=^★.+?★(.+?)$
structure=paragraph
```
