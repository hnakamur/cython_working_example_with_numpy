profile: convolve.so
	time python profile_convolve.py

convolve.so: convolve.pyx
	python setup.py build_ext --inplace

clean:
	-rm -r build convolve.[co] convolve.so
