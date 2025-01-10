# 幼なじみと甘～くエッチに過ごす方法 DeepSeek-V3 翻译补丁 v1.0.0

MD5: `98AB14EE5A345AB25E9EB00E9BF553C5`

作者： natsumerinchan(Github) == 雨宮ゆうこ

未作完整测试，有bug请反馈（截图加私发存档）。

## 使用方法
- 1.安装修正补丁
- 2.解压压缩包并把所有文件复制到游戏根目录，双击运行Start_dsv3.exe<br>(启动可能有些慢，因为UIF在加载)

# Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-3.5/GPT-4/Newbing/Sakura等大语言模型的Galgame自动化翻译解决方案
- [amayra/arc_conv](https://github.com/amayra/arc_conv.git) :由 w8m 使用纯 ASM 编写的命令行视觉小说工具包
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本(Kaguya_dat引擎+匹配规则None+不截断+生成JIS替换配置)
- [AtomCrafty/UniversalInjectorFramework](https://github.com/AtomCrafty/UniversalInjectorFramework.git) :实现自动转区和更改字体
- [xupefei/Locale-Emulator](https://github.com/xupefei/Locale-Emulator.git) :转区工具,使用了其中的dll
- [Enigma Virtual Box](https://enigmaprotector.com/assets/files/enigmavb.exe) :把脚本文件打包进exe
- [wxMEdit/wxMEdit](https://github.com/wxMEdit/wxMEdit.git) :wxMEdit，跨平台文本/十六进制编辑器，MadEdit 的改进版

### arc_conv message.dat 异或加解密命令
```
解密：
arc_conv --mod xor ff .\message.dat .\message.dat.dec
加密：
arc_conv --mod xor ff .\message.dat.dec .\message.dat
```

### 翻译注意事项
本作主人公的姓名可自定义，姓氏的十六进制码为`F041`(dec,SHIFT_JIS)/`EE8080`(json,UTF-8),<br>
名字则为`F040`(dec,SHIFT_JIS)/`EE8081`(json,UTF-8)，翻译前记得用单字的日文姓名替代，<br>
回封译文后对message.dat解密再用十六进制编辑器批量替换回去，然后再加密回去
