@chcp 65001
@echo off

rd .\rld_chs /s /q && md .\rld_chs
python .\packRld.py
cd rld_chs && ren *.rld *.bin
cd .. && python .\rld_enc.py
cd rld_chs && rm *.bin
pause