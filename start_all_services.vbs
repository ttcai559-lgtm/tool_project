Set WshShell = CreateObject("WScript.Shell")
Set objFSO = CreateObject("Scripting.FileSystemObject")

' Get script directory
strScriptPath = objFSO.GetParentFolderName(WScript.ScriptFullName)

' Check if services are already running
Function IsPortInUse(port)
    On Error Resume Next
    Set objHTTP = CreateObject("MSXML2.ServerXMLHTTP.6.0")
    objHTTP.open "GET", "http://localhost:" & port & "/", False
    objHTTP.send
    IsPortInUse = (Err.Number = 0)
    On Error GoTo 0
    Set objHTTP = Nothing
End Function

' Check backend
backendRunning = IsPortInUse(8000)
' We can't easily check frontend, so assume it's not running

If backendRunning Then
    result = MsgBox("Backend is already running!" & vbCrLf & vbCrLf & _
                    "Do you want to:" & vbCrLf & _
                    "YES - Start frontend only" & vbCrLf & _
                    "NO - Restart all services" & vbCrLf & _
                    "CANCEL - Exit", _
                    vbYesNoCancel + vbQuestion, "TestForge")

    If result = vbCancel Then
        WScript.Quit
    ElseIf result = vbNo Then
        ' Stop all services first
        WshShell.Run strScriptPath & "\stop_platform.bat", 0, True
        WScript.Sleep 2000
        backendRunning = False
    End If
End If

' Start backend if needed
If Not backendRunning Then
    ' Build paths
    strVenvPython = strScriptPath & "\venv\Scripts\python.exe"
    strBackendDir = strScriptPath & "\testforge"

    If objFSO.FileExists(strVenvPython) Then
        strBackendCmd = "cmd /c cd /d """ & strBackendDir & """ && """ & strVenvPython & """ -m uvicorn src.api.main:app --host 0.0.0.0 --port 8000 --reload"
    Else
        strBackendCmd = "cmd /c cd /d """ & strBackendDir & """ && python -m uvicorn src.api.main:app --host 0.0.0.0 --port 8000 --reload"
    End If

    WshShell.Run strBackendCmd, 0, False
    WScript.Sleep 3000
End If

' Start frontend
strFrontendDir = strScriptPath & "\forge-apis"
strFrontendCmd = "cmd /c cd /d """ & strFrontendDir & """ && npm run dev"
WshShell.Run strFrontendCmd, 0, False

WScript.Sleep 3000

' Show completion message
MsgBox "TestForge services started!" & vbCrLf & vbCrLf & _
       "Backend API:  http://localhost:8000/" & vbCrLf & _
       "Frontend UI:  http://localhost:8080/" & vbCrLf & vbCrLf & _
       "Opening browser in 3 seconds...", _
       vbInformation, "TestForge"

' Open browser
WScript.Sleep 3000
WshShell.Run "http://localhost:8080/"

Set objFSO = Nothing
Set WshShell = Nothing
