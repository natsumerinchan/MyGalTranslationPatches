# えろすまっしゅ！ gemini-2.5-pro-preview-06-05 翻译补丁

MD5: `E98501C84919D1D7947F73D8F0019ABC`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 使用方法
- 1.压缩包内字体可以不安装
- 2.将压缩包内所有文件解压至游戏根目录，双击运行01_EROS_CHS.exe(已自动转区)

## 更新日志
- 2025.07.12 20:58 首次提交
- 2025.07.13 11:08 修复跳转(感谢satan53佬的提醒)

# Credits

- [xd2333/GalTransl](https://github.com/xd2333/GalTransl.git) :支持GPT-3.5/GPT-4/Newbing/Sakura等大语言模型的Galgame自动化翻译解决方案
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [Crass-source](https://github.com/shangjiaxuan/Crass-source.git) :作者：痴汉公贼@飞雪之城（我用DeepSeek-R1将BLUEGALE引擎的cui插件转化为了单独的命令行程序bluegaletool，现在用不上了因为SExtractor自带bdt解密功能）
- [【工具】API HOOK和编码处理工具包](https://www.ai2.moe/topic/29225-【工具】api-hook和编码处理工具包)
- [xupefei/Locale-Emulator](https://github.com/xupefei/Locale-Emulator.git) :转区工具,使用了其中的dll

### BlueGale引擎 *.bdt SExtractor文本提取正则
(BlueGale_bdt引擎+932编码+生成JIS替换配置)
```
00_search=\!(?P<name>.+?)\s+"(.+?)$
05_search=\"(.+?)$
10_search=^\s+QP([^,]+?),([^,]+?),([^,]+?),([^,]+?)$
15_search=^\s+QP([^,]+?),([^,]+?),([^,]+?)$
20_search=^\s+QP([^,]+?),([^,]+?)$
decrypt=1
extraData=exportIndex
pureText=1
<decrypt=1解密, 默认encrypt=1加密>
```
