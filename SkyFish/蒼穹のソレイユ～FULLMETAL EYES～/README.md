# 蒼穹のソレイユ～FULLMETAL EYES～ gpt-4.1-2025-04-14 翻译补丁

MD5: `DA4C22236AB6BECB8201CD453A8E0F82`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 使用方法
- 1.安装压缩包内VLゴシック_WenQuanYi_cnjp.ttf字体
- 2.解压压缩包并把所有文件复制到游戏根目录，双击运行ExHIBIT_CHS.exe(无需转区)

## DLL源码

https://github.com/natsumerinchan/ExHIBIT_hook.git

# Credits

- [GalTransl/GalTransl](https://github.com/GalTransl/GalTransl.git) :支持GPT-4/Claude/Deepseek/Sakura等大语言模型的Galgame自动化翻译解决方案
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [ZQF-ReVN/RxExHIBIT](https://github.com/ZQF-ReVN/RxExHIBIT) :自动查找ExHIBIT引擎*.rld脚本解密密钥和密钥表
- [Yggdrasill-Moe/Niflheim/ExHIBIT](https://github.com/Yggdrasill-Moe/Niflheim/tree/master/ExHIBIT) :解密rld_dec.py ，加密rld_enc.py
- [regomne/chinesize/ExHIBIT/extRld](https://github.com/regomne/chinesize/tree/master/ExHIBIT/extRld) :提取extRld.py，回封packRld.py

ExHIBIT/extRld *.txt SExtractor文本提取正则
```
00_skip=^(　)$
05_search=^(?P<name>穹|少女|若者|琉平|大きな影|№０９７|騎士団|朝陽|ハミンギィ|ベルセルク)$
10_search=([^\t]+)
15_search=^(.+)$
postSkip=^[$0-9-a-z*-]
structure=paragraph
```

