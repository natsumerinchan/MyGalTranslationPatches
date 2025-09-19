# Always ～ふと、気が付けばキミとの日常…～ gemini-2.5-pro 翻译补丁

MD5: `D8EEBB123FCAA294D821C28CA795A53D`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 注
- 本作人名是bmz图片形式(可用GSD_BMZ_Editor.exe转换为bmp，`name01.bmz`-`name21.bmz`位于DATA.gsp)，<br>
人名生成脚本已放在仓库内（需安装依赖Pillow）。

## 使用方法
- 1、解压压缩包并把所有文件复制到游戏根目录，双击运行`always_chs.exe`。

# Credits

- [julixian/GalTranslPP](https://github.com/julixian/GalTranslPP.git) :GalTransl的C++实现
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [Dir-A/ReVN](https://github.com/Dir-A/ReVN.git) :GSD引擎工具包(本作脚本是txt明文不需要处理*.spt，解包和打包*.gsp用GSD_GSP_Editor.exe，处理*.bmz图片用GSD_BMZ_Editor.exe)

# GSD引擎 *.txt SExtractor提取正则
(TXT引擎+cp932编码+开启JIS替换配置)
```
00_search=^\[.+?\](?P<name>.+?)(「.+?」)\s{0,}$
05_search=^(?P<name>.+?)(「.+?」)\s{0,}$
10_search=^\s{0,}(.+?)$
postSkip=^[\/\\<\(\)]
structure=paragraph
```

