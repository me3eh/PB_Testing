
Library for BDD testing. Work in Progress. Have fun using this library.
This command will initialize needed directories for testing with our project
Pushing to repo

```bash
create-dirs
```

To create script file, you will need to type command below
```terminal
new-scenario --name <name_of_file>
```

Required arguments:
- --name <name_of_file>
    - set the name of created scenario


Little tips:
creating fixtures

```bash
python3 manage.py dumpdata auth.User --indent 4 > users.json
```

and after that to run server with date from fixtures

```bash
python3 ./manage.py testserver users.json --addrport 7000 & PID=$
```
<div style="background-image: linear-gradient(to left, violet, indigo, blue, green, yellow, orange, red); text-align: center; color: black;">
<h1 style="margin-bottom: 20px">Little tips for me</h1>
</div>
Building dist files for python pypi

```bash
python3 -m build
```
<br/>

Pushing files for python pypi

```bash
python3 -m twine upload --repository testpypi dist/*
```