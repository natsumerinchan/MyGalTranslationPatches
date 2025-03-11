@chcp 65001
@echo off

@REM 清理旧内容
rd .\txt /s /q & md .\txt
@REM 解密rld文件
python .\rld_dec.py
@REM 删除未解密rld文件并重命名*.bin为*.rld
cd rld && rm *.rld && ren *.bin *.rld
@REM 提取文本
cd .. && python .\extRld.py
echo "[TIPS]请不要重复执行，否则*.rld会被错误地再次解密"
pause