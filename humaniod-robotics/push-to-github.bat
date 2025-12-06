@echo off
echo ========================================
echo   Pushing to GitHub: Farhat-Naz/book-assignment
echo ========================================
echo.

cd /d "D:\quarterr 4\book\humaniod-robotics"

echo Setting remote URL...
git remote set-url origin https://github.com/Farhat-Naz/book-assignment.git

echo.
echo Pushing to GitHub...
echo You will be prompted for:
echo   Username: Farhat-Naz
echo   Password: (use your token)
echo.

git push -u origin main

echo.
if %ERRORLEVEL% EQU 0 (
    echo ========================================
    echo   SUCCESS! Code pushed to GitHub!
    echo ========================================
    echo.
    echo View your repository at:
    echo https://github.com/Farhat-Naz/book-assignment
) else (
    echo ========================================
    echo   FAILED! There was an error.
    echo ========================================
)

echo.
pause
