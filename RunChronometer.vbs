Set WshShell = CreateObject("WScript.Shell")
WshShell.Run chr(34) & "D:\Directory\RunChronometer.bat" & Chr(34), 0
Set WshShell = Nothing