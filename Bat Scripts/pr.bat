@echo off
setlocal

set "search_string=prank.txt"
set "content=The prankster is here!!!"
set "prank_file=prank.txt"

rem checks if the prank.txt exist in the current directory
if exist "%prank_file%" (
    echo Found text file: %prank_file%
    start notepad "%prank_file%"
) else (
    echo %content% > "%prank_file%"
    start notepad "%prank_file%"
)

rem To close the text file after 5 seconds
timeout /t 5 /nobreak >nul
taskkill /f /im notepad.exe >nul

endlocal

