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

' Check existing services
backendRunning = IsPortInUse(8000)
frontendRunning = IsPortInUse(8080)

If backendRunning Or frontendRunning Then
    statusMsg = "Services already running:" & vbCrLf
    If backendRunning Then statusMsg = statusMsg & "- Backend (port 8000)" & vbCrLf
    If frontendRunning Then statusMsg = statusMsg & "- Frontend (port 8080)" & vbCrLf

    result = MsgBox(statusMsg & vbCrLf & _
                    "Do you want to:" & vbCrLf & _
                    "YES - Start missing services only" & vbCrLf & _
                    "NO - Restart all services" & vbCrLf & _
                    "CANCEL - Exit", _
                    vbYesNoCancel + vbQuestion, "TestForge Platform")

    If result = vbCancel Then
        WScript.Quit
    ElseIf result = vbNo Then
        ' Stop all services first
        WshShell.Run strScriptPath & "\stop_platform.bat", 0, True
        WScript.Sleep 2000
        backendRunning = False
        frontendRunning = False
    End If
End If

' Build paths
strVenvPython = strScriptPath & "\venv\Scripts\python.exe"
strBackendDir = strScriptPath & "\testforge"
strFrontendDir = strScriptPath & "\forge-apis"

' Determine Python executable
If objFSO.FileExists(strVenvPython) Then
    strPython = """" & strVenvPython & """"
Else
    strPython = "python"
End If

' Start backend if needed (FastAPI on port 8000)
If Not backendRunning Then
    strBackendCmd = "cmd /c cd /d """ & strBackendDir & """ && " & strPython & " -m uvicorn src.api.main:app --host 0.0.0.0 --port 8000 --reload"
    WshShell.Run strBackendCmd, 0, False
    WScript.Sleep 3000
End If

' Start frontend if needed (Vite on port 8080)
If Not frontendRunning Then
    strFrontendCmd = "cmd /c cd /d """ & strFrontendDir & """ && npm run dev"
    WshShell.Run strFrontendCmd, 0, False
    WScript.Sleep 4000
End If

' Show completion message with all service URLs
MsgBox "TestForge Platform Started Successfully!" & vbCrLf & vbCrLf & _
       "=== Services Running ===" & vbCrLf & _
       "Frontend (with AI):  http://localhost:8080/" & vbCrLf & _
       "Backend API:         http://localhost:8000/" & vbCrLf & _
       "API Docs:            http://localhost:8000/docs" & vbCrLf & vbCrLf & _
       "Opening main platform in 3 seconds...", _
       vbInformation, "TestForge Platform"

' Open browsers
WScript.Sleep 3000

' Ask which services to open
openChoice = MsgBox("Which services do you want to open?" & vbCrLf & vbCrLf & _
                    "YES - Open Main Platform + API Docs" & vbCrLf & _
                    "NO/CANCEL - Open Main Platform only", _
                    vbYesNo + vbQuestion, "TestForge Platform")

' Open main platform
WshShell.Run "http://localhost:8080/"
WScript.Sleep 1000

If openChoice = vbYes Then
    ' Open API docs
    WshShell.Run "http://localhost:8000/docs"
End If

Set objFSO = Nothing
Set WshShell = Nothing
