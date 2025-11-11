# おしえてエッチなレシピ －アナタとワタシのあま～いせいかつ！－ gemini-2.5-pro 翻译补丁

MD5: `CA368C8CEF6D5F8421463C229FFA55DF`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 使用方法

- 1.安装修正补丁V1.02
- 2.解压压缩包并把`Releases`文件夹内所有内容复制到游戏根目录，双击运行`おしえて☆エッチなレシピ_CHS.exe`

## Credits

- [julixian/GalTranslPP](https://github.com/julixian/GalTranslPP.git) :GalTransl的C++实现
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [ZQF-ReVN/RxExHIBIT](https://github.com/ZQF-ReVN/RxExHIBIT) :自动查找ExHIBIT引擎*.rld脚本解密密钥和密钥表
- [Yggdrasill-Moe/Niflheim/ExHIBIT](https://github.com/Yggdrasill-Moe/Niflheim/tree/master/ExHIBIT) :解密rld_dec.py ，加密rld_enc.py
- [regomne/chinesize/ExHIBIT/extRld](https://github.com/regomne/chinesize/tree/master/ExHIBIT/extRld) :提取extRld.py，回封packRld.py
- [natsumerinchan/CELICA_HOOK](https://github.com/natsumerinchan/CELICA_HOOK.git) :个人写的游戏程序hook工具
- 补丁测试人员: [伪恶君子333@御爱同萌](https://www.ai2.moe/profile/9569-伪恶君子333/)

## ExHIBIT/extRld *.txt SExtractor文本提取正则

(TXT引擎+UTF-16编码+JIS替换)

```md
00_search=^\$(?P<name>.+?)$
05_search=^(?P<name>【？？？】|お客？|？？？|？？？　|圭吾|コック|お客Ａ|お客Ｂ|でかいお客|舞奈＆踊子|圭吾＆有原|圭吾＆七理|圭吾＆いつか|リンネ父ちゃん|でかいおっさん|騒がしい店員さん)$
10_search=^\s+(.+)$
15_search=([^\t]+)
20_search=^(.+)$
postSkip=^[$#0-9-a-z*\s\-]
structure=paragraph
```
