:: use get-pip to install "requirements.txt" || also can be use pyinstaller to make dist folder. "https://www.pyinstaller.org/"
python get-pip.py

:: change directory
cd ../flask_jsonapi/

:: pip install
pip install -r requirements.txt

:: set virtual environment
py -m venv env
CALL env\Scripts\activate

:: set "flask" env variables
set FLASK_APP=vg_test_app.py
set FLASK_ENV=development
set FLASK_RUN_PORT=5120

:: run APP
flask run
:: also can use below command to specify the port.
:: # flask run --port=2000

pause