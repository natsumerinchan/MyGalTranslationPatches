# Magical Marriage Lunatics!! claude-3-7-sonnet 翻译补丁

MD5: `5DD31033F0C973B89C14B49A5A423D33`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 注
本补丁仅支持2013.09.27发行的日文DVD版，不兼容DL版和英文版

## 使用方法
- 1.安装序列号为 ウチにもお姫様やってきて
- 2.解压压缩包并把所有文件复制到游戏根目录，双击运行ExHIBIT_CHS.exe(已改gbk无需转区)

## DLL源码

https://github.com/natsumerinchan/ExHIBIT_hook.git

# Credits

- [GalTransl/GalTransl](https://github.com/GalTransl/GalTransl.git) :支持GPT-4/Claude/Deepseek/Sakura等大语言模型的Galgame自动化翻译解决方案
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
10_search=(?P<unfinish>[^#A-Za-z0-9《》:]+)
```

