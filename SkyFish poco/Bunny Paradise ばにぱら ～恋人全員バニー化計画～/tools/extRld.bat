@chcp 65001
@echo off

rd .\txt /s /q
md .\txt
python .\rld_dec.py
cd rld && rm *.rld && ren *.bin *.rld
cd .. && python .\extRld.py
echo "[TIPS]请不要重复执行，否则*.rld会被错误地再次解密"
pause