
Library for BDD testing.

# Commands
All commands are typed into terminal
<hr style="border:2px solid gray"/>

```bash
prepare
```
It will create:
- directories: __resources_for_testing, features, steps, pages__
- configuration_file __config.ini__
- __common_steps.py__ file in steps,`` consisting basic commands used in testing
(selenium finding, clicking elements on site)

To scan for urls in your project (you must be in your project directory).
Available frameworks: rails, django
<hr style="border:2px solid gray"/>

```bash
scan_for_urls
```

To get all attributes located at your site with url in your project, type 
<hr style="border:2px solid gray"/>

```bash
attributes_in_sites
```
It will drop directories into your resources_for_testing directory



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

Points to do:
- [x] add class and id into file resources_for_testing
- [ ] decide if project need TUI (terminal interface) or GUI (graphical interface) - probably GUI - more handy
- [ ] think about urls with parameters (what to do with them and how to extract classes and ids from them after picking attributes)
