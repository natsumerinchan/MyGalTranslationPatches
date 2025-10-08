# 結い橋R ダウンロード版 gemini-2.5-pro-exp-03-25 翻译补丁

MD5: `FD3DD3F50194D02C0A2A53AD8044A7A2`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 使用方法
- 1.解压压缩包并把所有文件复制到游戏根目录，安装字体后转区运行cs2.exe

# Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-3.5/GPT-4/Newbing/Sakura等大语言模型的Galgame自动化翻译解决方案
- [nanami5270/GARbro-Mod](https://github.com/nanami5270/GARbro-Mod.git) :Galgame解包和打包工具
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [regomne/chinesize](https://github.com/regomne/chinesize.git) :galgame破解工具集，使用其中CatSystem2引擎的cstTextProc(脚本处理)

### cstTextProc编译方法
安装go工具链并设置好环境变量后,在cstTextProc目录执行
```
go mod init cstTextProc
go mod tidy
go build .\cst.go
```

### SExtractor cst.exe文本提取正则(TXT引擎+UTF-8-SIG编码+JIS替换)
改编自SExtractor/预设正则.fake.ini的[TXT CatSystem2 二次提取]。<br>
由于cst.exe要求原文和译文txt行数保持一致，所以要用仓库里的del0D0A.py删除文件末尾的换行符。
```
00_skip=^if
01_skip=^\\n$
02_search=^(?P<name>一海|知絵|まつり|詩奈|未依|琳|里美まつり（詩奈）|琳＆里美)$
03_search=^(?P<name>マスター|みい|一史|店員|先生|女の子|声|まつり＆詩奈|ロッキー)$
04_search=^(?P<name>一海＆知絵|受付|？|男の子|客|みんな|母親|ぬいぐるみ|里美)$
05_search=^(?P<name>女性|未依＆先生|未依＆みい|携帯|配達の兄ちゃん|料理長)$
06_search=^(?P<name>琳＆未依|一海＆未依|知絵＆未依|一海＆まつり|パフォーマー)$
07_search=^(?P<name>お客|小鳥|一海＆里美|看護婦|アナウンサー|マスター＆一史)$
08_search=^(?P<name>未依＆琳|おっさん|おばあさん|らん|一海＆詩奈)$
10_search=^[\\a-zA-Z0-9]*([「（].+?[」）])(?:\\@){0,1}$
11_search=^[\\a-zA-Z0-9]*(?P<unfinish>[「（].+?)(?:\\@){0,1}$
15_search=^\\n(?P<pre_unfinish>.+?)(?:\\@){0,1}$
20_search=^[0-9]+?\s[A-Za-z0-9_]+?\s(.+?)$
25_search=^([^@/].*?)(?:\\@){0,1}$
structure=paragraph
```

### json二次提取正则(JSON引擎+UTF-8编码+JIS替换)
```
10_search=(?P<unfinish>[^\r\nA-Za-z0-9\\]+)
```
