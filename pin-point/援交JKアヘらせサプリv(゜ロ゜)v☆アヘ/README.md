# 援交JKアヘらせサプリv(゜ロ゜)v☆アヘ DeepSeek-V3 翻译补丁 v1.0.0

MD5: `6BC6DECE94684A58D4525EBF8A09A3C2`

作者： natsumerinchan(Github) == 雨宮ゆうこ(2dfan)

未作完整测试，可能会出现漏翻，还请多多反馈bug！！！3q

## 使用方法
1.解压压缩包并把所有文件复制到游戏根目录即可

# Credits

- [GalTransl/GalTransl](https://github.com/GalTransl/GalTransl.git) :支持GPT-4/Claude/Deepseek/Sakura等大语言模型的Galgame自动化翻译解决方案
- [nanami5270/GARbro-Mod](https://github.com/nanami5270/GARbro-Mod.git) :Galgame解包和打包工具(用于解包xp3)
- [detached64/GalArc](https://github.com/detached64/GalArc.git) :Galgame 封包工具(用于封包xp3)
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [Emeditor](https://zh-cn.emeditor.com/#download) :文本编辑器，可用于批量修改文本编码(SHIFT_JIS -> UTF-16 LE 有签名)

### SExtractor *.ks文本提取正则
- 初次提取(TXT引擎+UTF-16编码+换行符@r@n+不生成JIS替换配置)
```
00_search=^\[.+\]【(?P<name>.+?)】\[aaa\]$
01_skip=^[;*{}@#\[]
02_skip=^(\s\s.+)$
03_search=^(?P<unfinish>.+)\[r\]$
04_search=^(.+」)\[.+\]$
05_search=^(.+)\[.+\]$
06_search=^(.+)$
structure=paragraph
```

- 二次提取(JSON引擎+UTF-8编码+换行符\r\n+不生成JIS替换配置)
```
10_search=(?P<unfinish>[^@a-zA-Z0-9－\\/\r\n\[\]]+)
```
(用于筛除控制代码)
