# Miss Each Other gemini-3-pro-preview 翻译补丁

MD5: `5E96F23C3071AB6813D04E7A2CD47807`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 使用方法

- 1.应用修正补丁`meoup121.exe`和`meoup122.exe`
- 2.解压压缩包并把`Releases`文件夹内所有文件复制到游戏根目录，双击运行`MEO_CHS.exe`
- 3.若想打开生肉除了删文件外可以在celica_hook.ini中修改`EnableFileSpoofing=0`为`1`隐藏翻译文件

## Credits

- [julixian/GalTranslPP](https://github.com/julixian/GalTranslPP.git) :GalTransl的C++实现
- [amayra/arc_conv](https://github.com/amayra/arc_conv.git) :由 w8m 以纯 ASM 编写的命令行视觉小说工具包
- [natsumerinchan/CELICA_HOOK](https://github.com/natsumerinchan/CELICA_HOOK.git) :个人写的游戏程序hook工具
- [求助Overflow社引擎的字体问题](https://www.ai2.moe/topic/41193-求助overflow社引擎的字体问题/)
  - 感谢草上飞佬[satan53x](https://github.com/satan53x)对本作字体问题的解答
  - ttf/otf字体转FONTDATA.DAT的python脚本以及xml的提取回封脚本已放在仓库

## overflow引擎 *.cmp arc_conv解封包命令

```pwsh
解包:
arc_conv --dest .\Script --unpack vivid .\Script.cmp

封包:
arc_conv --pack vivid .\Script .\Script.1.cmp
```
