# メモリア claude-3.7-sonnet 翻译补丁 v2.0.0

MD5: `8D71F9BC73E7796D712C9F594501EEB0`

作者： natsumerinchan(Github) == 雨宮ゆうこ

本补丁兼容PKG版和DL版。未作完整测试，有bug请反馈（截图加私发存档）。

## 使用方法
- 1.安装修正补丁v1.02(DL版不需要)
- 2.解压压缩包并把所有文件复制到游戏根目录，安装字体后转区运行cmvs32_chs.exe
- 3.游戏中修改字体为VL ゴシック

## 更新日志
- 2024.12.31 19:38 首次提交
- 2025.05.16 17:17 用claude-3.7-sonnet重跑

# Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-3.5/GPT-4/Newbing/Sakura等大语言模型的Galgame自动化翻译解决方案
- [amayra/arc_conv](https://github.com/amayra/arc_conv.git) :由 w8m 使用纯 ASM 编写的命令行视觉小说工具包
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [ZQF-ReVN/RxCMVS](https://github.com/ZQF-ReVN/RxCMVS.git) :CMVS引擎脚本处理(用最新版)、hook工具(git reset --hard到4c9f2874c65c702e47e109e38ea91a060c953c3c并编辑CMVSVersion.h改为使用对应游戏的配置)

### PS3_TextEditor json SExtractor文本提取正则(TXT引擎+UTF-8-SIG编码+JIS替换+导出时name向上移动一位)
```
05_search=^\s\s*"tra":\s*"(?P<name>ハルナ|智枝|アリサ|香奈実|ユウキ|由佳里|アイカ|シャール|真奈実|アカネ)"$
06_search=^\s\s*"tra":\s*"(?P<name>雪枝|サラ|惣太郎|フォルゼン|宏一|猫|店長|二人|店員|キャスター|リポーター)"$
07_search=^\s\s*"tra":\s*"(?P<name>研究者|雪|司会者|ふたり|声|女の子|少年|少女|おばちゃん|みんな)"$
08_search=^\s\s*"tra":\s*"(?P<name>販売員|守衛|男の子|コウイチ|店主|ユキエ|誰かの声)"$
10_search=^\s\s*"tra":\s*"(?P<msg>.+)"$
structure=paragraph
```

### arc_conv .cpz(cpz5) 解包命令（其它版本用garbro解包）
```
.\arc_conv.exe --dest .\script --unpack cpz5 .\script.cpz
.\arc_conv.exe --dest .\update --unpack cpz5 .\update.cpz
```