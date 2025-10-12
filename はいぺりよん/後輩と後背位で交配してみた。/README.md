# 後輩と後背位で交配してみた。 gpt-4o-2024-11-20翻译补丁 

MD5: `554E60EE21D163705ADF91A0A64D6709`

作者： natsumerinchan(Github) == 雨宮ゆうこ

还未推完，有bug请反馈（截图加发送存档）

## 使用方法
- 1.解压压缩包并把所有文件复制到游戏根目录，安装压缩包内字体后转区运行後輩と後背位で交配してみた.exe

# Credits

- [GalTransl/GalTransl](https://github.com/GalTransl/GalTransl.git) :支持GPT-4/Claude/Deepseek/Sakura等大语言模型的Galgame自动化翻译解决方案
- [detached64/GalArc](https://github.com/detached64/GalArc.git) :Galgame解包和打包工具(取消勾选解密ybn)
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本

*.ybn SExtractor文本提取正则(Yuris引擎,改编自其默认None规则)

```
01_skip=^M[\S\s]{2}"(?=[^\x81-\xEF]|■|◆)
10_search=^M[\S\s]{2}"(.+?)"
15_skip=^[A-Z][\x00-\xFF][\x00-\x04]
20_search=^(?P<name>.{1,20}?)(「.+」)$
21_search=^(?P<name>.{1,20}?)(（.+）)$
22_search=^(?P<name>.{1,20}?)(?P<start_unfinish>「.+)$
23_search=^(?P<name>.{1,20}?)(?P<start_unfinish>『.+)$
24_search=^(?P<end_unfinish>.+」)$
25_search=^(?P<end_unfinish>.+』)$
26_search=^(.+)$
decrypt=\xD3\x6F\xAC\x96
extraData=9

<如果提取内容为空请尝试把ysc.bin放入工作目录>
<decrypt为auto是自动解密，也可以指定密钥，如果已解密则删除decrypt这一行>
<extraData=9表示按参数个数过滤文本，最小为1；选项或人名提取不到时尝试调小该值>
<extraData=all时，设置中打开debug log可以查看对应指令的打印>
<version=0表示自动读取版本>
```
