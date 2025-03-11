# Bunny Paradise ばにぱら ～恋人全員バニー化計画～ qwen-max-latest 翻译补丁

MD5: `A62A06527CFAC41CC02969CC4FECEF34`

作者： natsumerinchan(Github) == 雨宮ゆうこ

还未推完，有bug请反馈（截图加发送存档）

## 使用方法
- 1.安装修正补丁(裸体补丁)
- 2.解压压缩包并把所有文件复制到游戏根目录，安装压缩包内字体后转区运行BunnyParadise_CHS.exe
- 3.进入游戏后在`コンフィグ画面へ` - `使用フォント` 搜索并选择 MS Gothic 字体

# Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-3.5/GPT-4/Newbing/Sakura等大语言模型的Galgame自动化翻译解决方案
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [ZQF-ReVN/RxExHIBIT](https://github.com/ZQF-ReVN/RxExHIBIT) :自动查找ExHIBIT引擎*.rld脚本解密密钥和密钥表
- [Yggdrasill-Moe/Niflheim/ExHIBIT](https://github.com/Yggdrasill-Moe/Niflheim/tree/master/ExHIBIT) :解密rld_dec.py ，加密rld_enc.py
- [regomne/chinesize/ExHIBIT/extRld](https://github.com/regomne/chinesize/tree/master/ExHIBIT/extRld) :提取extRld.py，回封packRld.py

ExHIBIT/extRld *.txt SExtractor文本提取正则
```
startline=1
00_skip=^[0-9]
05_search=^\$(?P<name>.+)$
15_search=^(.+)$
structure=paragraph
```
实际的人名在defChara.rld
