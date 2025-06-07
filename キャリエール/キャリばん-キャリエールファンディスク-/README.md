# キャリばん-キャリエールファンディスク- gemini-2.5-pro-exp-03-25 翻译补丁

MD5: `87C22518CAF534B9B42E2DD96776F09B`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 使用方法
- 1.本补丁已集成cariban040813up修正补丁无需另外下载
- 2.解压压缩包并把所有文件复制到游戏根目录，安装字体后转区运行Cariban_CHS.exe

## DLL源码

https://github.com/natsumerinchan/carriere_hook.git

# Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-3.5/GPT-4/Newbing/Sakura等大语言模型的Galgame自动化翻译解决方案
- [crskycode/GARbro](https://github.com/crskycode/GARbro) :Galgame解包和打包工具(打包时选yks格式)
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本

### SExtractor Carriere引擎 *.eve 文本提取正则(TXT引擎+932编码+JIS替换)
```
00_skip=^NEXT$
05_search=^CALS\,SET_\,\$s__Talk\,(?P<pre_nameANDmessage>「.+?」)$
10_search=^CALS\,SET_\,\$s__Talk\,(?P<pre_nameANDmessage>『.+?』)$
15_search=^CALS\,SET_\,\$s__Talk\,(?P<pre_nameANDstart_unfinish>「.+?)$
20_search=^CALS\,SET_\,\$s__Talk\,(?P<pre_nameANDstart_unfinish>『.+?)$
25_search=^CALS\,SET_\,\$s__Talk\,\s+(?P<end_unfinish>.+?」)$
30_search=^CALS\,SET_\,\$s__Talk\,\s+(?P<end_unfinish>.+?』)$
35_search=^CALS\,SET_\,\$s__Talk\,\s(?P<unfinish>.+?)$
40_search=^CALS\,SET_\,\$s__Talk\,(?P<unfinish>.+?)$
45_search=^CALS\,SET_\,\$s__Select\-Text\,(?P<predel_unfinish>.+?)$
structure=paragraph
postSkip=^[\s]
JisEncodeName=shift-jis
```

