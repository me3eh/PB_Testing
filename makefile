build:
	rm -rf dist
	cp steps/common_steps_pb_testing.py src/preparation/files_for_user/common_steps_copy.py
	cp environment.py src/preparation/files_for_user/environment_copy.py
	python3 setup.py develop
	python3 -m build
push_test:
	python3 -m twine upload --repository testpypi dist/*
push_prod:
	python3 -m twine upload --repository pypi dist/*
pycache:
	git clean -df *pycache*