# じゅ～にんかんり！ ～10人の乙女に愛の手を～ gemini-3-pro-preview 翻译补丁

MD5: `1D20B15848D63B1C6E6A2193C2EE08F5`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 使用方法

- 1.解压压缩包并把`Releases`文件夹内所有内容复制到游戏根目录，安装字体后双击运行`AdvHD_CHS.exe`

## Credits

- [julixian/GalTranslPP](https://github.com/julixian/GalTranslPP.git) :GalTransl的C++实现
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本(使用其中的改版Ws2Explorer对*.ws2脚本批量反编译/编译为json)
- [ZQF-ReVN/RxAdvHD.git](https://github.com/ZQF-ReVN/RxAdvHD.git) :AdvHD引擎工具，使用了其中的ARCV2Editor用于解包和打包*.arc

## AdvHD引擎 Ws2Explorer反编译 *.json SExtractor文本提取正则

(TXT引擎+UTF-8编码+JIS替换)

```md
00_search=^\{\"op\"\:\"Op15_SetDisplayName\"\,\"args\"\:\[\"(?P<name>.+?)\"\,\"
05_search=^\{\"op\"\:\"Op14_DisplayMessage\"\,\"args\"\:\[\d+\,\".+?\"\,\"(.+?)\"\,\"
postSkip=^[%]
structure=paragraph
```
