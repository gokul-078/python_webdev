# python_webdev

# Steps to install python virtual environment and run the app

1. Install python - install python3
2. Install  virtual environment - python3 -m venv venv_folderName.  (Eg:- python3 -m venv venv)
3. Activate the virtual environment - source venv_folderName/bin/activate.  (Eg:- source venv/bin/activate)
4. To install Fastapi - pip install fastapi
5. To install uvicorn which is used to run the python application - pip install uvicorn
6. To Run the application - uvicorn main:app --reload    (Here, main is the filename where our core run file of the app)