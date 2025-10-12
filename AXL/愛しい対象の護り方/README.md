# 愛しい対象の護り方 gpt-4o-2024-11-20 + DeepSeek-V3-0324 翻译补丁

MD5: `6EBA178702B4BC4FA8D69802FBEB5323`

作者： natsumerinchan(Github) == 雨宮ゆうこ

还未推完，有bug请反馈（截图加发送存档）

## 使用方法
- 1.应用win8修正补丁(http://mail.sumikko-soft.com/support.htm)
- 2.安装压缩包里的`unifont-all.ttf`字体(该字体是普通字体并非jis替换字体)
- 3.解压压缩包并把所有文件复制到游戏根目录下，然后转区运行愛しい対象の護り方.exe(否则会报错弹窗)
- 4.进入游戏后在`文字表示`-`フォント`中将字体改为`Unifont Smooth`

# Credits

- [GalTransl/GalTransl](https://github.com/GalTransl/GalTransl.git) :支持GPT-4/Claude/Deepseek/Sakura等大语言模型的Galgame自动化翻译解决方案
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [XP3Viewer](https://github.com/Inori/FuckGalEngine/blob/master/Krkr/XP3Viewer.rar) :可用于解包或封包被加密以及exe被保护的krkr2引擎游戏
- [sqlitebrowser/sqlitebrowser](https://github.com/sqlitebrowser/sqlitebrowser.git) :SQLite 数据库浏览器

## krkr2 scenedata.sdb导出text.csv SExtractor文本提取正则
(CSV引擎+utf-8编码+不生成jis替换配置)
```
05_search=^%[%0-9]*([\S\s]+)$
10_search=^([\S\s]+)$
extractKey=4
extraData=useIndex

<extractKey为列名的正则匹配>
<当extraData为nohead或者useIndex时，extractKey为列序号列表，如：1,name2,3>
```

## 翻译过程
本作是krkr2引擎但比较特殊，文本存储在scenedata.sdb，name存储在scene.sdb（皆为SQLite3数据库文件）<br>
可使用sqlitebrowser分别导出text.csv和name.csv。<br>
直接在scene.sdb修改name会导致语音消失，<br>
可将翻译好的text.csv和name.csv放在相同目录运行仓库内的merge_name.py将名字写入text.csv的disp列，<br>
然后只把text.csv导入回scenedata.sdb(导入时若卡死可尝试在首选项Restore Defaults)，最后把新的scenedata.sdb和原scene.sdb一起扔进patch.xp3。
