# マジスキ～Marginal Skip～ gemini-2.5-pro 翻译补丁

MD5: `D86F208F9B5259DD94C39D89BF0E384F`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 使用方法
- 1.解压压缩包并把所有文件复制到游戏根目录，转区运行マジスキ_CHS.exe

## DLL源码

https://github.com/natsumerinchan/ExHIBIT_hook.git

# Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-3.5/GPT-4/Newbing/Sakura等大语言模型的Galgame自动化翻译解决方案
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [ZQF-ReVN/RxExHIBIT](https://github.com/ZQF-ReVN/RxExHIBIT) :自动查找ExHIBIT引擎*.rld脚本解密密钥和密钥表
- [Yggdrasill-Moe/Niflheim/ExHIBIT](https://github.com/Yggdrasill-Moe/Niflheim/tree/master/ExHIBIT) :解密rld_dec.py ，加密rld_enc.py
- [regomne/chinesize/ExHIBIT/extRld](https://github.com/regomne/chinesize/tree/master/ExHIBIT/extRld) :提取extRld.py，回封packRld.py
- [AtomCrafty/UniversalInjectorFramework](https://github.com/AtomCrafty/UniversalInjectorFramework.git) :实现更改字体，jis映射

## ExHIBIT/extRld *.txt SExtractor文本提取正则
(TXT引擎+UTF-16编码+JIS替换)
```
00_skip=^\$(?P<name>.+?)$
05_skip=^(?P<name>記述)$
10_search=^\s+(?P<pre_nameANDmessage>「.+?」)$
11_search=^\s+(?P<pre_nameANDmessage>.+?」)$
12_search=^\s+(?P<pre_nameANDmessage>「.+?)$
13_search=^\s+(?P<pre_nameANDmessage>（.+?）)$
14_search=^\s+(?P<pre_nameANDmessage>.+?）)$
15_search=^\s+(?P<pre_nameANDmessage>（.+?)$
16_search=^\s+(?P<pre_nameANDmessage>『.+?』)$
17_search=^\s+(?P<pre_nameANDmessage>《.+?)$
18_search=^(?P<pre_nameANDmessage>「.+?」)$
19_search=^(?P<pre_nameANDmessage>「.+?)$
20_search=^(?P<pre_nameANDmessage>.+?」)$
21_search=^(?P<pre_nameANDmessage>（.+?）)$
22_search=^(?P<pre_nameANDmessage>.+?）)$
23_search=^(?P<pre_nameANDmessage>（.+?)$
24_search=^(?P<pre_nameANDmessage>『.+?』)$
25_search=^(?P<pre_nameANDmessage>《.+?)$
26_search=^[#n]+(?P<pre_nameANDmessage>「.+?」)$
27_search=^[#n]+(?P<pre_nameANDmessage>「.+?)$
28_search=^[#n]+(?P<pre_nameANDmessage>.+?」)$
29_search=^[#n]+(?P<pre_nameANDmessage>（.+?）)$
30_search=^[#n]+(?P<pre_nameANDmessage>.+?）)$
31_search=^[#n]+(?P<pre_nameANDmessage>（.+?)$
32_search=^[#n]+(?P<pre_nameANDmessage>『.+?』)$
33_search=^[#n]+(?P<pre_nameANDmessage>《.+?)$
34_search=^\s+(.+?)$
35_search=([^\t]+)
36_search=^[#n]+\s+(.+?)$
37_search=^[#n]+(.+?)$
38_search=^(.+?)$
postSkip=^[$#0-9-a-z*\s\-]
structure=paragraph
```

## json二次提取正则
先处理ruby标签`《([^A-Za-z]+?):([^0-9]+?)》`只保留第一个未命名捕获组`$1`的内容即被注释的正文<br>
(JSON引擎+UTF-8编码+不进行JIS替换)
```
10_search=(?P<unfinish>[^A-Za-z0-9#@《》\:]+)
```
