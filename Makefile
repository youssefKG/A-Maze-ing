VENV = venv
PYTHON = $(VENV)/bin/python3
SYS_PYTHON = python3
PIP = $(VENV)/bin/pip
FILES = src/parser/Parser.py \
		mazegen/algorithms/Algo.py \
		mazegen/algorithms/BFSAlgo.py \
		mazegen/algorithms/DFSAlgo.py \
		mazegen/algorithms/WilsonAlgo.py \

run: dependecies
	$(PYTHON) main.py config.txt

dependecies: $(VENV)/bin/activate requirements.txt
	$(PIP) install . 

$(VENV)/bin/activate:
	$(SYS_PYTHON) -m $(VENV) $(VENV)

clean:
	rm -rf  __pycache__ */__pycache__ */*/__pycache__

lint:
	flake8 . && mypy $(FILES) --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs	
