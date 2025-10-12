# お兄ちゃんティーチャー ～秘密の授業を希望します！～ kimi-k2翻译补丁 

MD5: `66DF006C8A150B88078F23D2BB0FF50A`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 使用方法
- 1.依次应用`予約特典 のぞき見ダイアリーパッチ`和修正补丁ver1.01
- 2.压缩包内字体可以不安装
- 3.解压压缩包并把所有文件复制到游戏根目录，双击运行oniT_CHS.exe(无需手动转区)

# Credits

- [GalTransl/GalTransl](https://github.com/GalTransl/GalTransl.git) :支持GPT-4/Claude/Deepseek/Sakura等大语言模型的Galgame自动化翻译解决方案
- [detached64/GalArc](https://github.com/detached64/GalArc.git) :Galgame解包和打包工具(取消勾选解密ybn)
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [【工具】API HOOK和编码处理工具包](https://www.ai2.moe/topic/29225-【工具】api-hook和编码处理工具包)
- [xupefei/Locale-Emulator](https://github.com/xupefei/Locale-Emulator.git) :转区工具,使用了其中的dll

## YU-RIS引擎 *.ybn SExtractor提取正则(仅适用于本作)
(Yuris引擎+cp932编码+生成JIS替换配置)
```
01_skip=^M[\S\s]{2}"(?=[^\x81-\xEF]|■|◆)
02_skip=^.+?\/.+?$
10_search=^M[\S\s]{2}"(.+?)"
15_skip=^[A-Z][\x00-\xFF][\x00-\x04]
20_search=^【(?P<name>.+?)】(?P<end_unfinish>「.+?」)$
21_search=^【(?P<name>.+?)】(?P<start_unfinish>「.+?)$
22_search=^(?P<end_unfinish>.+?」)$
23_search=^【(?P<name>.+?)】(?P<end_unfinish>「.+?）)$
24_search=^【(?P<name>.+?)】(?P<start_unfinish>（.+?)$
25_search=^(?P<end_unfinish>.+?）)$
26_search=^(.+)$
decrypt=\xE8\x01\x8C\x5E
extraData=9

<如果提取内容为空请尝试把ysc.bin放入工作目录>
<decrypt为auto是自动解密，也可以指定密钥，如果已解密则删除decrypt这一行>
<extraData=9表示按参数个数过滤文本，最小为1；选项或人名提取不到时尝试调小该值>
<extraData=all时，设置中打开debug log可以查看对应指令的打印>
<version=0表示自动读取版本>
```
