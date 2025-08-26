@chcp 65001
@echo off

@REM 清理旧文件
@REM rd .\rld_chs /s /q & md .\rld_chs
@REM 回封文本到rld文件
python .\packRld.py
@REM 重命名*.rld为*.bin
cd rld_chs && ren *.rld *.bin
@REM 加密rld文件
cd .. && python .\rld_enc.py
@REM 删除未加密rld文件
cd rld_chs && rm *.bin
pause