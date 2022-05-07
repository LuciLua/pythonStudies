@echo off

if '%1' == '-i' (
    call installfiles/install.bat
) else (
    call python pythonfiles/args.py %1 %2 %3
)



