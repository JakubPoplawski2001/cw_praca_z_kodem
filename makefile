install: 
	pip install -r requirements.txt

flask: 
	python3 -m flask run

pylint:
	pylint app.py

