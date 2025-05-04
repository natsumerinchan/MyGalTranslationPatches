# らくてん～この世の楽園？あの世の天国!?～ DeepSeek-V3-0324 翻译补丁

MD5: `910AA26F12D8ED9ABF47B445EF1205F5`

作者： natsumerinchan(Github) == 雨宮ゆうこ

还未推完，有bug请反馈（截图加发送存档）

## 使用方法
- 1.本补丁已集成特典补丁和免DVD补丁，无需另外下载
- 2.安装压缩包里的`unifont-all.ttf`字体(该字体是普通字体并非jis替换字体)
- 3.解压压缩包并把所有文件复制到游戏根目录下，双击运行rakutenDVD.exe

# Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-3.5/GPT-4/Newbing/Sakura等大语言模型的Galgame自动化翻译解决方案
- [crskycode/GARbro](https://github.com/crskycode/GARbro) :Galgame解包和打包工具(krkr2引擎)
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本

## 本作 krkr2 *.ks SExtractor文本提取正则
(TXT引擎+UTF-16+不生成jis配置)
```
00_search=^\s+(?P<name>.+?)\s+$
01_search=^(?P<name>妊娠希望の下級生|良い感じの上級生|興味津々な下級生)$
05_search=^\s+(.+?)$
10_skip=^@eval exp="sf.backlog=0"
15_search=^(?P<predel_unfinish>………………)$
20_search=^(?P<unfinish>.+)$
postSkip=^[;@*]
structure=paragraph
```
