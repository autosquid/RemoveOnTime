@echo off

:: ֹͣ����
echo stopping service..
sc stop RemoveOnTime

echo uninstall service...
:: ɾ��windows����
RemoveOnTime.exe -remove

echo uninstallation over. press any key to continue...
pause