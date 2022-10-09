<h1 style="color: black"> 
    <span style="color: blue">P</span><span style="color: red">B</span>_TESTING</h1>

<h3 style="color: black">Library for testing using
    <span style="color: blue"> Page Object Pattern</span>
    and
    <span style="color: red">Behaviour Driven Development.</span>
</h3>

## Commands
All commands are typed into terminal
<hr style="border:2px solid gray"/>

```bash``
prepare
```
It will create:
- directories: __resources_for_testing, features, steps, pages__
- configuration_file __config.ini__
- __common_steps.py__ file in steps,`` consisting basic commands used in testing
(selenium finding, clicking elements on site)
- database for keeping urls and attributes

To scan for urls in your project (you must be in your project directory).
Available frameworks: rails, django
<hr style="border:2px solid gray"/>

```bash
pb_configuration
```

This method will pop gui with urls from your project, urls used in testing and attributes to those urls,
which could be used in tests.
![img.png](img.png)
It will look like this.

On left we have urls scanned from project.

In the middle there are urls that will be used in testing.

On the right side there will be attributes(ids, input names, css classes) also used in tests.
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




<hr style="border:2px solid gray"/>

```bash
create-scenario-gui
```
This command is responsible for gui for creating tests.
![img_1.png](img_1.png)
It look like this and it will be used for creating bdd type tests. 
<hr style="border:2px solid gray"/>
When having problems with starting python test database with dumped data

## Dumping data from 
```bash
python3 manage.py dumpdata auth.User --indent 4 > users.json
```

and after that to run server with date from fixtures

```bash
python3 manage.py testserver users.json groups.json --addrport 7000 & PID=$
```
