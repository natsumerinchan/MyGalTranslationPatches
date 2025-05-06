# 空を飛ぶ、7つ目の魔法。 claude-3.7-sonnet 翻译补丁

MD5: `8E1FB356C68A6EAFD11B33275A1E0352`

作者： natsumerinchan(Github) == 雨宮ゆうこ

还未推完，有bug请反馈（截图加发送存档）

## 使用方法
- 1.解压压缩包并把所有文件复制到游戏根目录，双击运行空を飛ぶ、７つ目の魔法。_CHS.exe(已改GBK无需转区)

## DLL源码

https://github.com/natsumerinchan/soranana_hook.git

# Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-3.5/GPT-4/Newbing/Sakura等大语言模型的Galgame自动化翻译解决方案
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [ZQF-ReVN/RxExHIBIT](https://github.com/ZQF-ReVN/RxExHIBIT) :自动查找ExHIBIT引擎*.rld脚本解密密钥和密钥表
- [Yggdrasill-Moe/Niflheim/ExHIBIT](https://github.com/Yggdrasill-Moe/Niflheim/tree/master/ExHIBIT) :解密rld_dec.py ，加密rld_enc.py
- [regomne/chinesize/ExHIBIT/extRld](https://github.com/regomne/chinesize/tree/master/ExHIBIT/extRld) :提取extRld.py，回封packRld.py

ExHIBIT/extRld *.txt SExtractor文本提取正则
```
00_skip=^(記述|　)$
05_search=^(?P<pre_nameANDmessage>「.+」)$
10_search=^＜(.+?)＞$
15_search=^\s+(.+)$
20_search=([^\t]+)
25_search=^(.+)$
postSkip=^[$0-9-a-z*-]
structure=paragraph
```

## 注
本游戏只有defChara.rld被加密，其余脚本为明文，提取文本时只需解密defChara.rld
