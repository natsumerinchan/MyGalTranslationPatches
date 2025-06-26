# あいれぼ～IDOL☆REVOLUTION～ gemini-2.5-pro-preview-06-05 翻译补丁

MD5: `5CAE8D7A36BA6B6EE4D8D4FDD3CFD523`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 使用方法
- 1.把savedata中的*.fcd字体文件全部删除
- 2.压缩包内字体可以不安装
- 3.将压缩包内所有文件解压至游戏根目录，双击运行AIREBO_CHS.exe(已自动转区)

# Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-3.5/GPT-4/Newbing/Sakura等大语言模型的Galgame自动化翻译解决方案
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [amayra/arc_conv](https://github.com/amayra/arc_conv.git) :由 w8m 以纯 ASM 编写的命令行视觉小说工具包
- [marcussacana/SacanaWrapper](https://github.com/marcussacana/SacanaWrapper.git) :文本提取插件管理器
- [【工具】API HOOK和编码处理工具包](https://www.ai2.moe/topic/29225-【工具】api-hook和编码处理工具包)
- [xupefei/Locale-Emulator](https://github.com/xupefei/Locale-Emulator.git) :转区工具,使用了其中的dll

### majiro引擎 *.arc arc_conv解包/封包命令
```
解包:
arc_conv --dest .\scenario --unpack majiro .\scenario.arc

封包:
arc_conv --pack majiro .\scenario .\scenario.arc {1|2|3}
(本作为2)
```

### SacanaWrapper文本提取/回封命令
```
提取：
stringtool -Dump .\scenario .\txt

回封：
stringtool -Wordwrap .\scenario .\txt\new .\scenario_cn
```

### Powershell批量重命名*_Wordwrap.mjo为*.mjo
```
Get-ChildItem -Filter "*_Wordwrap.mjo" | ForEach-Object {
    $newName = $_.Name -replace '_Wordwrap', ''
    Rename-Item -Path $_.FullName -NewName $newName -WhatIf
}
```

### majiro引擎 *.txt SExtractor文本提取正则
(TXT引擎+UTF-8编码+生成JIS替换配置)
```
00_search=^＠(?P<name>.+?)\s+(「.+?」)$
05_search=^＠(?P<name>.+?)$
10_search=^(?P<pre_nameANDmessage>「.+」)$
15_search=^(.+)$
structure=paragraph
```
