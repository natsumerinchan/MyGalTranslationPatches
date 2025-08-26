# らぶ♥らぶ♥らいふ ～お嬢様７人とラブラブハーレム生活～ gemini-2.5-pro 翻译补丁

MD5: `564B4D2620039ABC9E19BAD36431E866`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 使用方法
- 1.解压压缩包并把所有文件复制到游戏根目录，双击运行ExHIBIT_CHS.exe(已改GBK无需转区)

## DLL源码

https://github.com/natsumerinchan/ExHIBIT_hook.git

# Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-3.5/GPT-4/Newbing/Sakura等大语言模型的Galgame自动化翻译解决方案
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [ZQF-ReVN/RxExHIBIT](https://github.com/ZQF-ReVN/RxExHIBIT) :自动查找ExHIBIT引擎*.rld脚本解密密钥和密钥表
- [Yggdrasill-Moe/Niflheim/ExHIBIT](https://github.com/Yggdrasill-Moe/Niflheim/tree/master/ExHIBIT) :解密rld_dec.py ，加密rld_enc.py
- [regomne/chinesize/ExHIBIT/extRld](https://github.com/regomne/chinesize/tree/master/ExHIBIT/extRld) :提取extRld.py，回封packRld.py

ExHIBIT/extRld *.txt SExtractor文本提取正则
(TXT引擎+UTF-16编码+不进行JIS替换)
```
00_skip=^\$(?P<name>.+?)$
10_search=^262\,-1\,0\,0\,0\,0\,(.+?)$
15_search=^\s+(.+)$
20_search=([^\t]+)
25_search=^(.+)$
postSkip=^[$#0-9-a-z*\s\-]
structure=paragraph
```

