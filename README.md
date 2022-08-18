
Library for BDD testing. Work in Progress. Have fun using this library.
This command will initialize needed directories for testing with our project
Pushing to repo

```bash
create-dirs
```

To create script file, you will need to type command below
```terminal
new-scenario
```
After that the menu will apear. Hopefully everything will be understandable from this point

Little tips:
creating fixtures

```bash
python3 manage.py dumpdata auth.User --indent 4 > users.json
```

and after that to run server with date from fixtures

```bash
python3 manage.py testserver users.json groups.json --addrport 7000 & PID=$
```
<div style="background-image: linear-gradient(to left, violet, indigo, blue, green, yellow, orange, red); text-align: center; color: black;">
<h1 style="margin-bottom: 20px">Little tips for building python package<br/>( probably only me)</h1>
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

if you want to test input
```python
def test_something_that_involves_user_input(monkeypatch):

    # monkeypatch the "input" function, so that it returns "Mark".
    # This simulates the user entering "Mark" in the terminal:
    monkeypatch.setattr('builtins.input', lambda _: "Mark")

    # go about using input() like you normally would:
    i = input("What is your name?")
    assert i == "Mark"
```