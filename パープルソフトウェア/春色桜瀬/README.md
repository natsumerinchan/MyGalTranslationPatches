# 春色桜瀬 DeepSeek-V3 翻译补丁 v1.0.0

MD5: `D92851C2C6DA9A7DB1E2CB680CAC9E3B`

作者： natsumerinchan(Github) == 雨宮ゆうこ

未作完整测试，有bug请反馈（截图加私发存档）。

## 使用方法
- 1.解压压缩包并把所有文件复制到游戏根目录，安装字体后转区运行cmvs_gpt4o.exe

# Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-3.5/GPT-4/Newbing/Sakura等大语言模型的Galgame自动化翻译解决方案
- [vn-tools/arc_unpacker](https://github.com/vn-tools/arc_unpacker.git) :用于从视觉小说中提取图像和声音的 CLI 工具。
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [ZQF-ReVN/RxCMVS](https://github.com/ZQF-ReVN/RxCMVS.git) :CMVS引擎脚本处理(用最新版)、hook工具(git reset --hard到4c9f2874c65c702e47e109e38ea91a060c953c3c并编辑CMVSVersion.h改为使用对应游戏的配置)

### PS3_TextEditor json SExtractor文本提取正则(TXT引擎+UTF-8-SIG编码+JIS替换+导出时name向上移动一位)
```
05_search=^\s\s*"tra":\s*"(?P<name>このは|陸|綾乃|くー|春奈|撫子|太一郎|和馬|美沙|桔梗|ぺちぺち)"$
06_search=^\s\s*"tra":\s*"(?P<name>女の人|皐月|千夏|京子|声|店員|３人|担任|男子Ａ|男Ａ|おばちゃん)"$
07_search=^\s\s*"tra":\s*"(?P<name>教師|焼きそば屋|型抜き屋|通行人Ａ|通行人Ｂ|通行人Ｃ|通行人Ｄ)"$
08_search=^\s\s*"tra":\s*"(?P<name>子桜|少年|三人|犬|みんな|泣き声|恋桜|女の子|鈴蘭|運転手)"$
09_search=^\s\s*"tra":\s*"(?P<name>先輩さん|物体|女子|女子１|女子２|ブティック|本屋|雑貨品)"$
10_search=^\s\s*"tra":\s*"(?P<msg>.+)"$
structure=paragraph
```

### arc_unpacker .cpz(cpz5) 解包命令
```
.\arc_unpacker.exe .\script.cpz
```

### CMVSVersion.h配置
```
//春色桜瀬 PKG
#define CMVS_210_
#define SCRIPTADDR 0x0043D720
#define SCRIPTXOR 0x0043D7E5
#define SCRIPTCOM 0x0043D80A
#define IMAGEADDR 0x0041E96F
```
