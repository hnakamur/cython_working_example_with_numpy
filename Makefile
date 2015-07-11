convolve.so: convolve.pyx
	python setup.py build_ext --inplace

clean:
	-rm -r build convolve.[co] convolve.so
