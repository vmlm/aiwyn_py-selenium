@echo off

where python > nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python 3 or greater before continuing.
    exit /b 1
)

echo Creating virtual environment...
python -m venv venv

echo Activating virtual environment...
call venv\Scripts\activate

echo Installing project dependencies...
pip install -r requirements.txt

echo Setup completed successfully.