testowy:
	echo "testowy"
build:
	rm -rf dist
	python3 -m build
push_test:
	python3 -m twine upload --repository testpypi dist/*