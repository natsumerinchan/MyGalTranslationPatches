# DUEL SAVIOR JUSTICE gemini-2.5-pro 翻译补丁

MD5: `C65EEA033B27BD24C2A70ADFB6BC2EC4`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 注
- 1、本补丁与之前的补丁区别在于前补丁基于日文原版，本补丁基于[Tenka Seiha](http://games.seiha.org/)整合JUSTICE和DESTINY的英翻补丁制作(好处是支持主角的剧情和战斗语音)
- 2、由于本补丁基于英文版制作，NEXAS引擎的控制代码无法简单地直接筛除[^@a-zA-Z0-9]，需要用我仓库内的脚本把正文转换为全角字符

## 使用方法
- 1、安装日文原版镜像
- 2、应用修正补丁v1.13和官方免DRM验证更新
- 3、覆盖[Tenka Seiha](https://tenka.seiha.org/)的[JUSTICE&&DESTINY英翻补丁](http://games.seiha.org/patches2/ds/)
- 4、解压压缩包并把所有文件复制到游戏根目录，双击运行`Duel Savior_CHS.exe`

# Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-4/Claude/Deepseek/Sakura等大语言模型的Galgame自动化翻译解决方案
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [GalTools/GalArc](https://github.com/GalTools/GalArc.git) :Galgame解包和打包工具(NEXAS版本2，压缩方式Zlib)
- [【工具】API HOOK和编码处理工具包](https://www.ai2.moe/topic/29225-【工具】api-hook和编码处理工具包)
- [xupefei/Locale-Emulator](https://github.com/xupefei/Locale-Emulator.git) :转区工具,使用了其中的dll
- [Duel Savior Justice Dev Kit](http://tenka.seiha.org/images2019/dsj/DuelSavior_SDK.rar) :英翻补丁作者[Tenka Seiha](https://tenka.seiha.org/)提供的翻译工具包，里面有NEXAS引擎脚本的反编译和重编译工具dstool.exe
- [FunkyFr3sh/cnc-ddraw](https://github.com/FunkyFr3sh/cnc-ddraw.git) :GDI, OpenGL and Direct3D 9 re-implementation of the DirectDraw API for classic 2D games for better compatibility with Windows ME, 2000, XP, Vista, 7, 8, 10, 11, Wine (Linux/macOS/Android) and Virtual Machines

# SExtractor提取正则
1、初步提取
(TXT引擎+cp932编码+不开启JIS替换配置)
```
00_skip=^PushB\s+<[A-Z]{1}[0-9]{0,1}_.+?>$
05_skip=^PushB\s+<.+?_.+?>$
06_skip=^PushB\s+<\d+>$
07_skip=^PushB\s+<\w{3,4}\d+>$
10_skip=^PushB\s+<.+?\.(bin|mpg)>$
15_search=^PushB\s+<(?P<name>Taiga|Lily|Berio|Mia|Kaede|Rico|Principal|Downy|Nanashi|Sel|Crea|Dahlia|Imnity|Black Papillon|Lobelia|Rubinas|Shezar|Mudou|Zombie Girl|Village Chief|Girl|Citizen A|Armor|Commander|Citizen B|Merchant|Chairman|Chamberlain|Undead A|All|Adjutant|Noble A|Undead B|Head Chef|Noble B|Soldier|Undead C|Pharmacist|Girl A|Traitor|Girl B|Dead Girl|Old Woman|Officer A|Thug C|Subordinate|Boy|Student A|Monster|Soldier A|Mother|Man A|Thug A|Noble C|Gargoyle|Councillor A|Man B|Crea's Servant|Citizen|Thug B|Student B|Student C|Lia|Monster A|Man C|Staff|Monster B|Citizen C|Monster C|Student D|Refugee A|Child|Youth|Older Student B|Villager A|Older Student E|Civilian A|Commander B|Man D|Older Student A|Older Student D|Citizen D|Refugee B|Villager B|Daichi|Kaede/Berio/Rico|Old Man|Soldier B|City Guard A|Civilian D|Civilian B|Kid A|Kid B|Officer B|Adjutant B|Guard A|Teacher|Older Student C|Refugee C|Daiki|Civilian C|Kaede/Berio|Councillor B|Councillor C|Villager C|Stall Owner|Civilian E|Citizen E|Students|Doctor|Justy|Waitress|Yuudai|Tohru|Midori|Male Student|Nurse|City Guard B|Chimera|Troops|Father|Operator|Manager|Taisei|Daisuke|Berio & Kaede|Civilians|Pigtail Girl|Officer C|Officer D|Student E|Student F|Student G|Student H|Student I|Guard B|Guard C|Salesman|Golem|Berio & Sel|Berio & Taiga|Taiga & Sel|Student 1|Student 2|Student 3|Taiga and Berio|Lily & Berio|Taiga & Mia|Student|chomp|Noble D|Noble E|Schoolgirl A|Lily & Taiga|Rico & Imnity|Sel & Taiga|Toilet Occupant|Lady|Undead|Mia & Crea|Lily/Mia|Daughter|Woman A|Taiga & Lily|Merchant A|Merchant B|Woman|\?\?\?|\?\?\?\s\w)>$
20_search=^PushB\s+<(.+?)>$
structure=paragraph
```

2、二次提取
(JSON引擎+UTF-8编码+开启JIS替换配置)
```
10_search=(?P<unfinish>[^<>@a-zA-Z0-9－/\r\n\u4e00-\u9fa5]+)
```
