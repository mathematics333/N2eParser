#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.
Menu,Tray,Icon, N2eParser.png
Menu, tray, Icon , N2eParser.ico, 1, 1

Gui, Add, Button, w100 h30 gButtonClicked, PARSE VIEWPOINTS
Gui, Show, w125 h50, Single Button GUI
return

ButtonClicked:
    Run N2E.py
    Sleep 1000
    Run E2E.py
    return

GuiClose:
GuiEscape:
    ExitApp
return

