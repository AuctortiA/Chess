
all: init TestModel ChessMain

init: 
	pip install -r requirements.txt

TestModel: 
	python -m unittest

ChessMain:
	python code/main.py