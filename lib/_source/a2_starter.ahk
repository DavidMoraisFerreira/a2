; This is the script that becomes the a2.exe in root!
;@Ahk2Exe-SetMainIcon ..\..\ui\res\a2.ico

; If (!A_IsCompiled) {
;     MsgBox, 16, ERROR, a2_starter should ONLY be run compiled!
;     ExitApp
; }

a2_ahk := _init_get_autohotkey_exe()
lib_path := _init_get_lib_path()
root_path := path_dirname(lib_path)
a2data := a2_get_user_data_path(root_path)
global a2cfg := a2_get_user_config(a2data)

if (A_Args.Length()) {
    args := _gather_args()
    Run, %a2_ahk% %lib_path%\a2.ahk %args%, %root_path%
}
else
    Run, %a2_ahk% %lib_path%\a2.ahk, %root_path%

check_load_time_errors(lib_path)

If !FileExist(path_join(root_path, "_ user_data_include")) {
    ; Start the ui by default if there is no include file written yet.
    Run, "%a2_ahk%" a2ui.ahk, %lib_path%
}

Return ; -----------------------------------------------------------------------
#include ..\a2init_check.ahk
#include ..\a2_exceptions.ahk
#include ..\a2_user_data.ahk

check_load_time_errors(lib_path) {
    script_name := "a2.ahk"
    a2_popup := script_name " ahk_class #32770 ahk_exe Autohotkey.exe"
    WinWaitActive, %a2_popup%,, 2
    If ErrorLevel
        return

    ; win_id := WinExist(a2_popup)
    ; idstr := "ahk_id " win_id
    ControlGetText, ctrl_txt, Static1, %a2_popup%
    WinClose, %a2_popup%
    a2_on_startup_exception(ctrl_txt, path_join(lib_path, script_name))
}

_gather_args() {
    args := ""
    for _, arg in A_Args {
        if InStr(arg, A_Space) {
            args .= string_quote(arg) . " "
        }
        else
            args .= arg . " "
    }
    return args
}
