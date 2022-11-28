# PB TESTING
Library for testing using Page Object Pattern and Behaviour Driven Development.

## Commands
All commands are typed into terminal, using venv

To activate venv type command
```bash
source venv/bin/activate
```
It will look like this. venv will show up next to your name
and command prompt
![img_5.png](wip_files_for_readme/img_5.png)
<hr style="border:2px solid gray"/>

```bash
prepare
```

It will create:
- directories: __resources_for_testing, features, steps, pages__
- configuration_file __config.ini__
- __common_steps.py__ file in steps,`` consisting basic commands used in testing
(selenium finding, clicking elements on site)
- database for keeping urls from your project

__This step is crucial, because it will setup all directoreies for using this library__

Available frameworks for url scan: rails, django
<hr style="border:2px solid gray"/>

```bash
pb_configuration
```

This method will pop gui with urls from your project and urls used in tests.
It will look like this.
![img.png](wip_files_for_readme/how_pb_configuration_looks.png)
On left we have urls scanned from project.
On the right side there are urls that will be used in testing.

After clicking one of choices here

![img_3.png](wip_files_for_readme/img_3.png)

and clicking button with arrow pointing to the right

![img_4.png](wip_files_for_readme/img_4.png)

it will add url to the right column, to collection of urls used in testing with the help of my application.


![](wip_files_for_readme/how_app_works.gif)
<hr style="border:2px solid gray"/>

```bash
step_creator
```
This gui is responsible for creating tests, using scanning urls and 
