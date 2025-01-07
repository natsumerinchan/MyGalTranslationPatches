# てんぷれっ!!  DeepSeek-V3 翻译补丁 v2.0.0

MD5: `2C24502042379043871900C2290DDB8D`

作者： natsumerinchan(Github) == 雨宮ゆうこ(2dfan)

仓库地址：https://github.com/natsumerinchan/TMPL_CN

本人制作的第一个ai翻译补丁。未作测试，可能会出现漏翻以及各种莫名其妙的符号，还请多多反馈bug！！！3q

## 更新历史
2025.01.07 v2.0.0 使用DeepSeek-V3模型重跑，并修复窗口标题乱码

## 使用方法

解压压缩包并把所有文件复制到游戏根目录，双击TMPL_dsv3.exe运行（无需转区）

# Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-3.5/GPT-4/Newbing/Sakura等大语言模型的Galgame自动化翻译解决方案
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [crskycode/CIRCUS_Script_Tool](https://github.com/crskycode/CIRCUS_Script_Tool.git) :用于从CIRCUS社的游戏中导出和导入文本的工具。
- [GalGame汉化教程(一)——Ollydbg修改编码和字体](https://blog.csdn.net/madonghyu/article/details/90029001)
- [てんぷれっ！！ 免DVD免验证补丁 （NoDVD&認証回避 Patch）](https://2dfan.com/downloads/13755)

## SExtractor CIRCUS_Script_Tool 文本处理正则
- 初次提取(TXT引擎+UTF-8编码+不生成JIS替换配置)
```
01_search=^◆.+?◆(?P<pre_nameANDmsg>「.+」)$
02_search=^◆.+?◆(.+)$
structure=paragraph
```

-二次提取(JSON引擎+UTF-8编码+不生成JIS替换配置)
```
10_search=(?P<unfinish>[^@a-zA-Z0-9－\\/\r\n]+)
```
(用于筛除控制代码)
