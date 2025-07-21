# らぶらぶ♥プリンセス ～お姫さまがいっぱい！もっとエッチなハーレム生活!!～ claude-3-5-sonnet-20241022 翻译补丁

MD5: `3CE87CE5EF6CDEEDC0443B04659379CE`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 注
本补丁仅支持2015.07.31发行的日文DVD版，不兼容DL版

## 使用方法
- 1.rld_chs的defChara.rld默认基于原版制作，若你应用了特典补丁请将其更换为`defChara_chs\特典版`里的版本
- 2.解压压缩包并把所有文件复制到游戏根目录，双击运行ExHIBIT_CHS.exe(已改gbk无需转区)

## DLL源码

https://github.com/natsumerinchan/ExHIBIT_hook.git

# Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-3.5/GPT-4/Newbing/Sakura等大语言模型的Galgame自动化翻译解决方案
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [ZQF-ReVN/RxExHIBIT](https://github.com/ZQF-ReVN/RxExHIBIT) :自动查找ExHIBIT引擎*.rld脚本解密密钥和密钥表
- [Yggdrasill-Moe/Niflheim/ExHIBIT](https://github.com/Yggdrasill-Moe/Niflheim/tree/master/ExHIBIT) :解密rld_dec.py ，加密rld_enc.py
- [regomne/chinesize/ExHIBIT/extRld](https://github.com/regomne/chinesize/tree/master/ExHIBIT/extRld) :提取extRld.py，回封packRld.py

## ExHIBIT/extRld *.txt SExtractor文本提取正则
(TXT引擎+utf-16编码+不生成jis替换配置)
```
00_search=^\$(?P<name>.+?)$
15_search=^\s+(.+)$
20_search=([^\t]+)
25_search=^(.+)$
postSkip=^[$#0-9-a-z*\s\-]
structure=paragraph
```

## json二次提取正则
(JSON引擎+utf-8编码+不生成jis替换配置)
```
10_search=(?P<unfinish>[^#A-Za-z0-9《》:\.\"\- ]+)
```

