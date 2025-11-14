# 恋する夏のラストリゾート gemini-2.5-pro 翻译补丁

MD5: `873C75A67EBD8456C1A361CC1C3E35CE`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 使用方法

- 1.安装修正补丁、`いちゃラブハーレムH追加パッチ`、`水着の日焼けあとパッチ`和`Sweetest Summer`追加补丁
- 2.解压压缩包并把`Releases`文件夹内所有内容复制到游戏根目录，安装字体后转区运行`AdvHD.exe`

## Credits

- [julixian/GalTranslPP](https://github.com/julixian/GalTranslPP.git) :GalTransl的C++实现
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本(使用其中的改版Ws2Explorer对*.ws2脚本批量反编译/编译为json)
- [ZQF-ReVN/RxAdvHD.git](https://github.com/ZQF-ReVN/RxAdvHD.git) :AdvHD引擎工具，使用了其中的ARCV2Editor用于解包和打包*.arc

## AdvHD引擎 Ws2Explorer反编译 *.json SExtractor文本提取正则

(TXT引擎+UTF-8编码+JIS替换)

```md
00_search=^\{\"op\"\:\"Op15_SetDisplayName\"\,\"args\"\:\[\"(?P<name>.+?)\"\,\"
05_search=^\{\"op\"\:\"Op14_DisplayMessage\"\,\"args\"\:\[\d+\,\".+?\"\,\"(.+?)\"\,\"
structure=paragraph
```
