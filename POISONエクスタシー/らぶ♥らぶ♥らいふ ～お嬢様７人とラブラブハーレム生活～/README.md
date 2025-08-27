# らぶ♥らぶ♥らいふ ～お嬢様７人とラブラブハーレム生活～ gemini-2.5-pro 翻译补丁

MD5: `122A482C3BC5027C4EB3ACE69670F336`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 注
- 由于测试时发现翻译defChara.rld里的人名会导致部分立绘消失及部分剧情闪退，<br>
故本补丁不对人名进行翻译（可用压缩包内的name替换表.csv对照人名）
- 为避免原有人名乱码故从GBK编码回退使用JIS替换

## 使用方法
- 1.先前下载过本补丁旧版本的话请删掉rld_chs\defChara.rld
- 2.解压压缩包并把所有文件复制到游戏根目录，安装压缩包内字体后双击运行ExHIBIT_CHS.exe

## 更新日志
- 2025.08.27 00:03 首次提交
- 2025.08.27 14:35 编码从gbk改回cp932并删除defChara.rld(人名列表)的翻译

## DLL源码

https://github.com/natsumerinchan/ExHIBIT_hook.git

# Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-3.5/GPT-4/Newbing/Sakura等大语言模型的Galgame自动化翻译解决方案
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [ZQF-ReVN/RxExHIBIT](https://github.com/ZQF-ReVN/RxExHIBIT) :自动查找ExHIBIT引擎*.rld脚本解密密钥和密钥表
- [Yggdrasill-Moe/Niflheim/ExHIBIT](https://github.com/Yggdrasill-Moe/Niflheim/tree/master/ExHIBIT) :解密rld_dec.py ，加密rld_enc.py
- [regomne/chinesize/ExHIBIT/extRld](https://github.com/regomne/chinesize/tree/master/ExHIBIT/extRld) :提取extRld.py，回封packRld.py

ExHIBIT/extRld *.txt SExtractor文本提取正则
(TXT引擎+UTF-16编码+JIS替换)
```
00_skip=^\$(?P<name>.+?)$
10_search=^262\,-1\,0\,0\,0\,0\,(.+?)$
15_search=^\s+(.+)$
20_search=([^\t]+)
25_search=^(.+)$
postSkip=^[$#0-9-a-z*\s\-]
structure=paragraph
```

