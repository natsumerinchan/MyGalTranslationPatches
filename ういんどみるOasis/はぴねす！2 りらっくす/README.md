# はぴねす！2 りらっくす Gpt4o-1120+DeepSeek-V3 翻译补丁 v1.0.0

MD5: `8D8A1EFA88C47C38BCFE0D60B591A32E`

作者： natsumerinchan(Github) == 雨宮ゆうこ

简单翻新一下。未作完整测试，有bug请反馈（截图加私发存档）。

## 使用方法
- 1.应用站内免key.dat补丁
- 2.解压压缩包并把所有文件复制到游戏根目录，安装字体后直接运行cs2.exe
- 3.设置中改字体为`ＭＳ ゴシック`
- 4.存档路径可以在config/startup.xml第320-322行自行修改

# Credits

- [GalTransl/GalTransl](https://github.com/GalTransl/GalTransl.git) :支持GPT-4/Claude/Deepseek/Sakura等大语言模型的Galgame自动化翻译解决方案
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
临时注释一下src/main_extract_txt.py的"已补足文件末尾缺少的一个换行符"前中后三行，<br>
因为cst.exe要求原文和译文txt行数保持一致。
```
00_skip=^if
05_skip=^\\n$
10_search=^[\\a-zA-Z0-9]*(?P<pre_name>[「（].+?[」）])(?:\\@){0,1}$
11_search=^[\\a-zA-Z0-9]*(?P<pre_nameANDunfinish>[「（].+?)(?:\\@){0,1}$
15_search=^\\n(?P<pre_unfinish>.+?)(?:\\@){0,1}$
20_search=^([^@/].*?)(?:\\@){0,1}$
structure=paragraph
```
(极少数msg被误识别为name,可在galtransl导出人名替换表时手动翻译一下)

