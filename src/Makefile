VENV = venv
PYTHON = $(VENV)/bin/python3
SYS_PYTHON = python3
PIP = $(VENV)/bin/pip
FILES = src/parser/Parser.py \
		src/algorithms/Algo.py \
		src/algorithms/BFSAlgo.py \
		src/algorithms/DFSAlgo.py \
		src/algorithms/WilsonAlgo.py \

run: dependecies
	$(PYTHON) main.py config.txt

dependecies: $(VENV)/bin/activate requirements.txt
	$(PIP) install -r requirements.txt

$(VENV)/bin/activate:
	$(SYS_PYTHON) -m $(VENV) $(VENV)

clean:
	rm -rf */__pycache__ */*/__pycache__

lint:
	
