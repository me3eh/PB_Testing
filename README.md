# PB TESTING
Library for testing using Page Object Pattern and Behaviour Driven Development.

## Usage
This application is experimental and is used mainly for Engineer's Thesis.

It will be maintained for errors and probably in near future might get some new features.
## Before using

Before creating any tests, you need geckodriver.
It's crucial, because selenium, which is responsible for initializing the browser and doing actions,
need this driver to work.
Link for geckodriver: https://github.com/mozilla/geckodriver/releases.

There are several ways for preparing driver to coopearte with library, depending on Operating System.
On each of systems: Microsoft Windows, macOS and Linux it looks a bit different.
I was using Linux, so I will describe it here, but here are links for other OS:

Windows: http://www.learningaboutelectronics.com/Articles/How-to-install-geckodriver-Python-windows.php

macOS: https://medium.com/dropout-analytics/selenium-and-geckodriver-on-mac-b411dbfe61bc

On Linux you need to:
- download driver,
- unpack it with any tool,
- set execute rights for user __chmod <file> 700__,
- put library on path __/usr/local/bin__. It can be done by moving it to location(mv),
copying to location(cp) or linking to directory(ln). Each command will work
__<command> <geckodriver_name> /usr/local/bin__

It's worth mentioning that is not only working way to put geckodriver to work with selenium.

## Commands
All commands are typed into terminal, using venv

To activate venv type command
```bash
source venv/bin/activate
```
It will look like this. venv will show up next to your name
and command prompt
![source_venv.png](https://raw.githubusercontent.com/me3eh/PB_Testing/production/hosting_for_images/wip_files_for_readme/source_venv.png)
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
It will look like this:
![how_pb_configuration_looks.png](https://raw.githubusercontent.com/me3eh/PB_Testing/production/hosting_for_images/wip_files_for_readme/how_pb_configuration_looks.png)

On left we have urls scanned from project.
On the right side there are urls that will be used in testing.

Between listboxes is arrow, which let user pass value from one listbox to another
and at the bottom there are buttons, which also allow user to include new urls into testing.

Overall working:
![how_pb_configuration_works.png](https://raw.githubusercontent.com/me3eh/PB_Testing/production/hosting_for_images/wip_files_for_readme/pb_configuration_working.gif)
<hr style="border:2px solid gray"/>

```bash
step_creator
```
This gui is responsible for creating tests, using scanning urls and 
## OK, application is fine, but how to do testing?

Testing in this application is based on BDD. This means

Invocing tests
Use command behave <name_of_feature_file> -D headless