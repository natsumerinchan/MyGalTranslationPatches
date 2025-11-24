# ぱ・ぴ・こ・ん ～双子の娘はどうきゅうせい!?～ gemini-3-pro-preview 翻译补丁

MD5: `AC535B0C30134D76E1F21B735EBDB2C8`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 使用方法

- 1.需要免转区启动的请将游戏根目录名修改为纯英文如`papicon`
- 2.将`data.xp3`重命名为`data.xp3.bak`
- 3.解压压缩包并把`Releases`文件夹内所有文件复制到游戏根目录，双击或转区运行`papicon_chs.exe`
- 4.每次关闭游戏`kwlib.dll`都有很大概率因不明原因被删除，可执行`修复kwlib.dll.bat`或手动复制文件到相应位置

## Credits

- [julixian/GalTranslPP](https://github.com/julixian/GalTranslPP.git) :GalTransl的C++实现
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [nanami5270/GARbro](https://github.com/nanami5270/GARbro) :Galgame解包和打包工具
- [arcusmaximus/KirikiriTools](https://github.com/arcusmaximus/KirikiriTools.git) :Xp3Pack.exe 打包xp3

## krkr *.ks SExtractor提取正则(仅适用于本作)

(TXT引擎+UTF-16编码+不进行JIS替换)

```md
00_search=^\@cm2.*name\=\"(?P<name>.+?)\"
05_search=^\s{0,}(?P<unfinish>.+?)\[r\]$
10_search=^\s{0,}(?P<end_unfinish>.+?)\[p2\]$
15_search=^\s{0,}(.+?)$
postSkip=^[\[;@*]
structure=paragraph
```
