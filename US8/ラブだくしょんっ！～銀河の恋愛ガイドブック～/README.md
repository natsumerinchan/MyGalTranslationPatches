# ラブだくしょんっ！～銀河の恋愛ガイドブック～ claude-3-7-sonnet-20250219翻译补丁 

MD5: `EDAA54E04780645EB45061006365ADB3`

作者： natsumerinchan(Github) == 雨宮ゆうこ

还未推完，有bug请反馈（截图加发送存档）

## 使用方法
- 1.解压压缩包并把所有文件复制到游戏根目录，安装压缩包内字体后转区运行Rabudaku_CHS.exe
- 2.所有路线通关后再打上已经翻译的通关秘密补丁，转区运行Rabudaku_Secret_CHS.exe

(注：原秘密补丁有密码，需要通关所有路线后才会在游戏中显示，我也使用了相同的密码对翻译后补丁进行加密。
想提前打补丁的可自己用GalArc解包cg.ypf，密码在ev/mail/mail_true_01.png，我就不剧透了。)

# Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-3.5/GPT-4/Newbing/Sakura等大语言模型的Galgame自动化翻译解决方案
- [detached64/GalArc](https://github.com/detached64/GalArc.git) :Galgame解包和打包工具(取消勾选解密ybn)
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [Enigma Virtual Box](https://enigmaprotector.com/assets/files/enigmavb.exe) :把脚本文件打包进exe

*.ybn SExtractor文本提取正则(Yuris引擎,改编自其默认None规则)

```
00_skip=^M[\S\s]{2}"(?=[^\x81-\xEF]|■|◆)
05_search=^M[\S\s]{2}"(.+?)"
10_skip=^[A-Z][\x00-\xFF][\x00-\x04]
15_search=^(.+?「.+?」.+[^」])$
20_search=^(?P<name>？（.+?）)(「.+」)$
25_search=^(?P<name>.{1,20}?)(「.+」)$
30_search=^(?P<name>.{1,20}?)(?P<unfinish>「.+[^」])$
35_search=^(.+?『.+?』.+[^』])$
40_search=^(?P<name>？（.+?）)(『.+』)$
45_search=^(?P<name>.{1,20}?)(『.+』)$
50_search=^(?P<name>.{1,20}?)(?P<unfinish>『.+[^」。])$
55_search=^(?P<end_unfinish>.+[」』])$
60_search=^(?P<unfinish>.+[^。])$
65_search=^(.+)$
decrypt=\xD3\x6F\xAC\x96
extraData=9

<如果提取内容为空请尝试把ysc.bin放入工作目录>
<decrypt为auto是自动解密，也可以指定密钥，如果已解密则删除decrypt这一行>
<extraData=9表示按参数个数过滤文本，最小为1；选项或人名提取不到时尝试调小该值>
<extraData=all时，设置中打开debug log可以查看对应指令的打印>
<version=0表示自动读取版本>
```
