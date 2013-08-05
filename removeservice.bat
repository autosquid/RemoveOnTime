@echo off

:: 停止服务
echo stopping service..
sc stop RemoveOnTime

echo uninstall service...
:: 删除windows服务
RemoveOnTime.exe -remove

echo uninstallation over. press any key to continue...
pause