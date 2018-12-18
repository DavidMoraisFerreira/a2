; this is the script that becomes the a2.exe in root!
If (!A_IsCompiled)
{
    MsgBox a2_starter should only be run compiled!
    ExitApp
}

_init_has_config_test() {
    user_data_include_path = %A_ScriptDir%\lib\_ user_data_includes.ahk
    IfExist, %user_data_include_path%
        value := true
    Else
        value := false
    return value
}

a2_ahk := _init_get_autohotkey_exe()

Run, %a2_ahk% lib\a2.ahk

if (!_init_has_config_test()) {
    MsgBox, 65, a2 Not configured yet!, Welcome!`nThis a2 package does not seem to be started before and is not configured yet! The Interface can be only opened through the Tray Icon or the a2ui executable.`n`nOr I can do that right now!
    IfMsgBox, Ok
        Run, "%a2_ahk%" a2ui.ahk, %A_ScriptDir%\lib
}

Return ; -----------------------------------------------------------------------------
#include ..\a2init_check.ahk
