# えろどるっ☆ Qwen2.5-72B-Instruct 翻译补丁 

MD5: `CFA19CACA0B390CB39A36085C6516D14`

作者： natsumerinchan(Github) == 雨宮ゆうこ

未作完整测试，有bug请反馈（截图加发送存档）

## 使用方法
1.解压压缩包并把所有文件复制到游戏根目录，安装压缩包内字体后转区运行erodoru_CHS.exe

# Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-3.5/GPT-4/Newbing/Sakura等大语言模型的Galgame自动化翻译解决方案
- [crskycode/GARbro](https://github.com/crskycode/GARbro) :Galgame解包和打包工具
- [ZQF-ReVN/RxPJADV](https://github.com/ZQF-ReVN/RxPJADV.git) :PJADV引擎解封包、脚本提取加解密
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本

# SExtractor提取正则(TXT引擎)
```
05_search=^\s\s*"chr_tra"\s*:\s*"(?P<name>[^"]+)",\s*?$
10_search=^\s\s*"chp_tra"\s*:\s*"(?P<msg>[^"]+)\\\\.+"\s*?$
15_search=^\s\s*"chp_tra"\s*:\s*"(?P<msg>[^"\\]+)"\s*?$
20_search=^\s\s*"sel_tra"\s*:\s*"(?P<msg>[^"]+)\\\\.+"\s*?$
25_search=^\s\s*"sel_tra"\s*:\s*"(?P<msg>[^"\\]+)"\s*?$
30_search=^\s\s*"msg_tra"\s*:\s*"(?P<msg>[^"]+)\\\\.+"\s*?$
35_search=^\s\s*"msg_tra"\s*:\s*"(?P<msg>[^"\\]+)"\s*?$
structure=paragraph
```
