echo Hello, I'm here to copy folders out of the virtual file system
@echo off

REM SET VitrualFSPath=%1
REM SET ActualFSPath=%2

SET VirtualFSPath="c:\Users\pbcote\3D Objects\ESRI3DO\ModelMgt_20210127\Edits\edits_before"
SET ActualFSPath="f:\current_work\projects\Boston\Bos3d\Bos3dDevpbc\Workflows\ModelMgt_20201214\ModelBatch\test3do\apricot"
SET UserPath="c:\EPSON"

echo VFSP is %VirtualFSPath% AFSP is %ActualFSPath%

pause 

For %%A in ("%ActualFSPath%") do (
    echo full path: %%~fA
    echo drive: %%~dA
    echo path: %%~pA)
    ::set DestDrive=%%~dA
    ::set DestPath=%%~pA 
pause


cd /D %DestDrive%
if not exist %DestPath%\ (
    echo attempting to creaate %DestPath% 
    mkdir "%DestPath%" )
if exist %DestPath%\NUL (
    echo %DestPath% Exists 
) else (
    echo Cannot create %ActualFSPath% 
    goto end )

pause
rem cd /D c:
pushd %VirtualFSPath%
dir
echo %cd%
pause
rem pushd c:\
if not exist %VirtualFSPath% (
    echo %VirtualFSPath% Does not exist. 
    goto end )
pause
if exist %VirtualFSPath% (
    echo %VirtualFSPath% exists. 
    goto do_it ) 

pause

:do_it
echo Lets do it!
cd /D %DestDrive%
pushd %DestPath%
XCOPY /s %VirtualFSPath%\* 

:end
echo This is the end.
pause
