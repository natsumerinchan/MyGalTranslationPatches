# 恋ではなく ―― It’s not love，but so where near. gemini-2.5-pro 翻译补丁

MD5: `59497376820FDE55498632506B7BAB9B`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 使用方法

- 1、安装压缩包内字体

- 2、将压缩包内所有文件解压至游戏根目录，双击运行恋ではなく.exe

- 3、在`文字表示`-`フォント`中将字体切换为`Unifont Smooth`

## Credits

- [julixian/GalTranslPP](https://github.com/julixian/GalTranslPP.git) :GalTransl的C++实现
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [crskycode/GARbro](https://github.com/crskycode/GARbro) :Galgame解包和打包工具
- [arcusmaximus/KirikiriTools](https://github.com/arcusmaximus/KirikiriTools.git) :Xp3Pack.exe 打包xp3
- 测试人员： [伪恶君子333@御爱同萌](https://www.ai2.moe/profile/9569-伪恶君子333/)

## krkr *.ks SExtractor提取正则(仅适用于本作)

(TXT引擎+UTF-16编码+不进行JIS替换)

```txt
00_search=^@nm\s+t\=\"\"\s{0,}rt\=\"(?P<name>.+?)\"
01_search=^@nm\s+t\=\"(?P<name>.+?)\"
04_skip=^\s{0,}(kag|sf|if|sf|f\[|var|for|try|System|tf)
05_skip=^\[(np|else|endif)\]$
06_skip=^\s{0,}\[\s{0,}(trans|eval|jump|if|chr|wait|eff|se)
10_search=^\[resetwait\]\s{0,}(.+?)\[np\]$
14_search=^\s{0,}(.+?)\[weff.+?\]\[np\]$
15_search=^\s{0,}(.+?)\[np\]$
20_search=^\[resetwait\]\s{0,}(.+?)$
25_search=^\[nowait\]\s{0,}(.+?)\[endnowait\]$
30_search=^@overlap_ch\s+txt1\=\"\s{0,}(.+?)\"\s+txt2\=\"\s{0,}(.+?)\"\s+txt3\=\"\s{0,}(.+?)\"$
35_search=^@overlap_ch\s+txt1\=\"\s{0,}(.+?)\"\s+txt2\=\"\s{0,}(.+?)\"$
40_search=txt\=\"(.+?)\"
45_search=^\s{0,}(.+?)$
postSkip=^[\*\;@\/\\\{\}\t]
```
