# Soranica Ele claude-3-7-sonnet 翻译补丁

MD5: `7C19D25ED85407898D96B91033EB4202`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 使用方法
- 1.安装压缩包内VLゴシック_WenQuanYi_cnjp.ttf
- 2.解压压缩包并把所有文件复制到游戏根目录，转区运行malie_chs.exe
- 3.在テキスト設定把字体修改为VL ゴシック

## 更新日志
- 2025.05.26 12:00 首次提交

# Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-3.5/GPT-4/Newbing/Sakura等大语言模型的Galgame自动化翻译解决方案
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [nanami5270/Malie_Script_Tool](https://github.com/nanami5270/Malie_Script_Tool.git) :FreeMalie Engine Script Disassembler
- [resourcehacker](https://www.angusj.com/resourcehacker/) :exe资源编辑器，用于提取和替换EXEC文件

### malie引擎 SExtractor文本提取正则

(TXT引擎+utf-8编码+生成JIS替换配置)

```
00_search=^◆.+?◆(?P<name>オフィーリア|カグヤ|ゼノビア|鳴|さや|未明|蒼|空)$
05_search=^◆.+?◆(?P<name>菊哉|フェルナン|印南|『終』の司|司|レアチーズ)$
10_search=^◆.+?◆(?P<name>マキ|アナウンス|？？？|源治郎|店員|一郎|女子生徒)$
15_search=^◆.+?◆(?P<name>Ａ壱|Ｂ次郎|香奈子|てれこ|裏司|フォンバウザー三世)$
20_search=^◆.+?◆\x01ÿ\x00\x00(.+?)$
25_search=^◆.+?◆(.+?)$
postSkip=^[\s]
structure=paragraph
```

### json二次提取正则
(JSON引擎+utf-8编码+不生成JIS替换配置)
```
10_search=(?P<unfinish>[^\x00-\x1a\[\]\{\}.･\_#\s=\"\'%<>\(\)@a-zA-Z0-9－/\r\n,-]+)
```
