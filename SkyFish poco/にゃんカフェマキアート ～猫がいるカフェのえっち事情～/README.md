# にゃんカフェマキアート ～猫がいるカフェのえっち事情～ gemini-2.5-pro 翻译补丁

MD5: `B6A86A6027C0A29C7AFE4AF3D249F255`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 使用方法

- 1.修正补丁打不打无所谓，里面的`res\c\shortcut.init.rnf`已整合进补丁内
- 2.解压压缩包并把`Releases`文件夹内所有内容复制到游戏根目录，双击运行`ExHIBIT_CHS.exe`

## Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-3.5/GPT-4/Newbing/Sakura等大语言模型的Galgame自动化翻译解决方案
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [ZQF-ReVN/RxExHIBIT](https://github.com/ZQF-ReVN/RxExHIBIT) :自动查找ExHIBIT引擎*.rld脚本解密密钥和密钥表
- [Yggdrasill-Moe/Niflheim/ExHIBIT](https://github.com/Yggdrasill-Moe/Niflheim/tree/master/ExHIBIT) :解密rld_dec.py ，加密rld_enc.py
- [regomne/chinesize/ExHIBIT/extRld](https://github.com/regomne/chinesize/tree/master/ExHIBIT/extRld) :提取extRld.py，回封packRld.py
- [natsumerinchan/CELICA_HOOK](https://github.com/natsumerinchan/CELICA_HOOK.git) :个人写的游戏程序hook工具
- 补丁测试人员: [伪恶君子333@御爱同萌](https://www.ai2.moe/profile/9569-伪恶君子333/)

## ExHIBIT/extRld *.txt SExtractor文本提取正则

(TXT引擎+UTF-16编码+JIS替换)

```md
00_skip=^\$(?P<name>.+?)$
10_search=^262,-1,0,0,0,0,(.+?)$
15_search=^\s+(.+)$
20_search=([^\t]+)
25_search=^(.+)$
postSkip=^[$#0-9-a-z*\s\-]
structure=paragraph
```

## json二次提取正则

(JSON引擎+UTF-8编码+不进行JIS替换)

```md
10_search=(?P<unfinish>[^#A-Za-z0-9《》:]+)
```
