# 青春フラジャイル claude-3-5-sonnet-20241022 翻译补丁

MD5: `F53A7FF607DDB20DBF832B15CE08857C`

作者： natsumerinchan(Github) == 雨宮ゆうこ

应人请求进行重翻（据其称旧有补丁的人名不统一及人称代词有误）

## 使用方法
- 1.解压压缩包并把所有文件复制到游戏根目录，安装字体后转区运行cmvs32_chs.exe
- 2.游戏中修改字体为VL ゴシック

# Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-3.5/GPT-4/Newbing/Sakura等大语言模型的Galgame自动化翻译解决方案
- [morkt/GARbro](https://github.com/morkt/GARbro.git) :Galgame解包和打包工具(使用morkt原版，nanami5270版解不了CPZ包)
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [ZQF-ReVN/RxCMVS](https://github.com/ZQF-ReVN/RxCMVS.git) :CMVS引擎脚本处理(用最新版)、hook工具(git reset --hard到4c9f2874c65c702e47e109e38ea91a060c953c3c并编辑CMVSVersion.h改为使用对应游戏的配置)

### PS3_TextEditor json SExtractor文本提取正则
(TXT引擎+UTF-8-SIG编码+JIS替换+导出时name向上移动一位)
```
00_search=^\s\s*"tra":\s*"(?P<name>優人|リズ|氷緒|せつな|透音|響希)"$
05_search=^\s\s*"tra":\s*"(?P<name>ゆら|ＥＳ|エリス|晴弥|カラス|女子生徒Ａ)"$
10_search=^\s\s*"tra":\s*"(?P<name>？？？|優人３|優人２|少女|板長)"$
15_search=^\s\s*"tra":\s*"(?P<name>優人＆氷緒|宿泊客Ｄ|男Ａ|男Ｂ)"$
20_search=^\s\s*"tra":\s*"(?P<name>宿泊客Ａ|従業員|魚屋のおじさん)"$
25_search=^\s\s*"tra":\s*"(?P<name>観光客|記者|宿泊客Ｅ|優人＆透音)"$
30_search=^\s\s*"tra":\s*"(?P<name>薬局のお姉さん|カメラマン|宿泊客Ｂ)"$
35_search=^\s\s*"tra":\s*"(?P<name>宿泊客Ｃ|優人＆響希|優人＆せつな)"$
40_search=^\s\s*"tra":\s*"(?P<name>優人＆リズ|透音＆リズ|せつな＆ゆら)"$
45_search=^\s\s*"tra":\s*"(?P<name>リズ＆ＥＳ|透音＆ゆら|男子学生たち)"$
50_search=^\s\s*"tra":\s*"(?P<msg>.+)"$
postSkip=^[A-Za-z\-]
structure=paragraph
```
