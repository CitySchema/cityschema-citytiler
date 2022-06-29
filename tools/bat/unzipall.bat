rem unzipall.bat
rem Unzips all of the zip archives in a folder

echo Usage: unzipall.bat folder 

for /R "%1" %%I in ("*.zip") do (
  rem To unpack zip contents to individual sub-folders:
    rem "%ProgramFiles(x86)%\7-Zip\7z.exe" x -y -o"%%~dpnI" "%%~fI"
  rem To unpack contents of each zip to folder 
       "%ProgramFiles(x86)%\7-Zip\7z.exe" x -y -o"%%~dpI" "%%~fI"   
)

