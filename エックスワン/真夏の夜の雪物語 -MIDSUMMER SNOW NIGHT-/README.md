# 真夏の夜の雪物語 -MIDSUMMER SNOW NIGHT- gemini-2.5-pro 翻译补丁

MD5: `302EB0065081E3DC3D8E9F68247F4538`

作者： natsumerinchan(Github) == 雨宮ゆうこ

## 使用方法

- 1.应用修正补丁v1.1
- 2.解压压缩包并把所有文件复制到游戏根目录，双击运行cs2.exe

## Credits

- [julixian/GalTranslPP](https://github.com/julixian/GalTranslPP.git) :GalTransl的C++实现
- [crskycode/GARbro](https://github.com/crskycode/GARbro) :Galgame解包和打包工具
- [satan53x/SExtractor](https://github.com/satan53x/SExtractor.git) :从GalGame脚本提取和导入文本
- [regomne/chinesize](https://github.com/regomne/chinesize.git) :galgame破解工具集，使用其中CatSystem2引擎的exthg3(hg3图片解包和封包)
- [lifegpc/msg-tool](https://github.com/lifegpc/msg-tool.git) :多引擎文本提取和导入工具
- [xd2333/GalTransl_DumpInjector](https://github.com/xd2333/GalTransl_DumpInjector.git) :VNTranslationTools和msg-tool的GUI界面
- [【工具】API HOOK和编码处理工具包](https://www.ai2.moe/topic/29225-【工具】api-hook和编码处理工具包)
- [xupefei/Locale-Emulator](https://github.com/xupefei/Locale-Emulator.git) :转区工具,使用了其中的dll

## exthg3编译方法

安装go工具链并设置好环境变量后,在exthg3目录执行

```pwsh
go mod init exthg3
go mod tidy
go get github.com/regomne/bstream
go build -buildvcs=false -o .\hg3tool.exe .
```

## msg-tool导出json SExtractor二次提取正则

(JSON引擎+UTF-8编码+JIS替换)

```txt
10_search=(?P<unfinish>[^@a-zA-Z0-9\;\\\/\r\n ]+)
```

## 本作人名处理

本作人名为图片形式，位于image.int的`sys_log_name.hg3`和`sys_meswnd_name.hg3`，处理步骤如下：  

- 1、使用hg3tool解包
- 2、分别在两个解包出来的目录打开powershell执行以下命令生成文件名列表`input.txt`

```pwsh
get-ChildItem -Filter *.png | Select-Object -ExpandProperty BaseName | Out-File input.txt -Encoding UTF8
```

- 3、`input.txt`中文件名与译文用制表符`\t`隔开（即`<TAB>`键），若第三列为`true`则会生成灰色长条框
- 4、将仓库内的`name2png.py`放入目录并执行`python .\name2png.py`
  - 需安装依赖`pip install pillow`
  - 生成图片需要`input.txt`以及hg3tool解包过程中生成的`info.json`
- 5、使用hg3tool打包
- 6、在游戏根目录创建`image`文件夹把刚打包的hg3文件扔进去即可（CatSystem2引擎支持免封包）
