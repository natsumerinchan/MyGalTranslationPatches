# 翼をください DeepSeek-R1 翻译补丁

MD5: `61CEE72B261FA2FFC256FF63C9144D05`

作者： natsumerinchan(Github) == 雨宮ゆうこ

还未推完，有bug请反馈（截图加发送存档）

## 
- 1.解压压缩包并把所有文件复制到游戏根目录下，然后双击运行fwing_chs.exe
- 2.如果之前启动过日文原版请到C:\Users\<用户名>\Appdata\Roaming\skysphere\FWing删除ctwizenv.dat文件以免字形显示不一，除非你不介意。

# Credits

- [GalTransl/GalTransl](https://github.com/GalTransl/GalTransl.git) :支持GPT-4/Claude/Deepseek/Sakura等大语言模型的Galgame自动化翻译解决方案
- [qtlark/noa_pac](https://github.com/qtlark/noa_pac.git) :EntisGLS引擎解包/打包工具
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本(tools\EntisGLS文件夹的工具可获取noa_pac使用的解包密码)
- [nanami5270/EntisGLS_Tools](https://github.com/nanami5270/EntisGLS_Tools.git) :EntisGLS/Cotopha引擎.csx脚本处理工具

EntisGLS_Tools *.txt SExtractor文本提取正则(仅适用于本游戏)
(本引擎支持UTF-16-LE，无需SJIS替换)
```
05_search=^◆.+?◆(?P<msg>\\\\r;.+)$
10_skip=^◆.+?◆[（）．→;,*%&-_@.$0-9A-Za-z:\s#\/\\[{}]
15_search=^◆.+?◆(?P<pre_nameANDmsg>「.+」)$
20_search=^◆.+?◆(?P<pre_nameANDmsg>『.+』)$
25_search=^◆.+?◆(.+)$
structure=paragraph
```
