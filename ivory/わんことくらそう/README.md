# わんことくらそう claude-3-7-sonnet 翻译补丁

MD5: `DEE3FEBF3A6D08D1BA6D4DCD320D6B12`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 使用方法
- 1.应用修正补丁v10
- 2.将压缩包内所有文件解压至游戏根目录，安装压缩包内字体后转区运行WANKO.EXE

## 已知问题
- 1.人名未翻译且显示不正常

# Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-3.5/GPT-4/Newbing/Sakura等大语言模型的Galgame自动化翻译解决方案
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [amayra/arc_conv](https://github.com/amayra/arc_conv.git) :由 w8m 以纯 ASM 编写的命令行视觉小说工具包
- 测试人员： [伪恶君子333@御爱同萌](https://www.ai2.moe/profile/9569-伪恶君子333/)

### Marble引擎 *.mbl arc_conv解包/封包命令
```
解包(执行命令后在窗口选择文件)：
.\arc_conv.exe --fmt mbl

封包:
.\arc_conv.exe --pack mbl .\scripts .\mg_data2.mbl
```

### Marble引擎 *.txt SExtractor文本提取正则
(TXT引擎+UTF-8编码+不生成JIS替换配置)
```
00_search=^\>(?P<name>.+?)$
05_search=^(「.+?」)$
10_search=^(?P<name>.+?)(「.+?」)$
15_search=^\{(.+?)$
20_search=^\s+(.+?)$
25_search=^(.+?)$
JisEncodeName=shift-jis
postSkip=^[*A-Za-z0-9\\!@=:\{\}>]
structure=paragraph
```
