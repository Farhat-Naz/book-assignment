@echo off
echo ================================================
echo   PUSHING TO: Farhat-Naz/book-assignment
echo ================================================
echo.

cd /d "D:\quarterr 4\book\humaniod-robotics"

echo Checking git status...
git status --short
echo.

echo ================================================
echo   Ready to push 4 commits with 170 files
echo ================================================
echo.
echo When prompted:
echo   Username: Farhat-Naz
echo   Password: [paste your token]
echo.
pause

git push -u origin main

echo.
echo ================================================
if %ERRORLEVEL% EQU 0 (
    echo   SUCCESS! View at:
    echo   https://github.com/Farhat-Naz/book-assignment
) else (
    echo   ERROR! Check your token permissions
)
echo ================================================
echo.
pause
