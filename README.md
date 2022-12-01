# PB TESTING
Library for testing using Page Object Pattern and Behaviour Driven Development.

## Usage
This application is experimental and is used mainly for Engineer's Thesis.

It will be maintained for errors and probably in near future might get some new features.
## Before using
You will need Geckodriver for running tests using behave (which is based on selenium)
https://github.com/mozilla/geckodriver/releases - link for geckodriver browsing.

Probably you will need also to put it into /usr/local/bin/ (as for linux)
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