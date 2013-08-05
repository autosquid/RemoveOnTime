@echo off

echo  install service now
RemoveOnTime.exe -install

echo  set auto startup
sc config RemoveOnTime start= AUTO

sc start RemoveOnTime

echo install succeed. press any key to continue...
pause