
BLD_EXT = setup.py build_ext --inplace
INSTALL = setup.py install --user

all: python

python: python3

python3: install_py3_ext install_py3

install_py3_ext:
	python3 $(BLD_EXT)

install_py3:
	python3 $(INSTALL)

install_py2_ext:
	python2 $(BLD_EXT)

install_py2:
	python2 $(INSTALL)

clean: clean-co

clean-co:
	rm -f heron/*.c
	rm -f heron/*.so

clean-all:
	rm -rf build
