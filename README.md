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

Testing in this application is based on BDD.
This means you need to write scenarios with them
If you generate plan of actions, you will have an implementation of that keyword,
but you also need to have scenario on which it will be executing tests.
Example:
scenario:
```gherkin
Feature: login as admin
  Scenario: with correct passes
    When logging in with username and password for admin
    Then user will be logged as admin and redirected to /admin
```
will be implemented by this code below, generated in app
```python
from behave import *

@when ('logging in with username and password for admin')
def step(context):
	context.execute_steps(u'''
		When visiting site http://localhost:8000/
		When filling input with xpath
		 //input[@class='form-control' and @id='user-name'
		 and @name='username' and @type='text']
		 with text jar
		When filling input with xpath
		 //input[@class='form-control' and @id='user-password'
		 and @name='password' and @type='password']
		 with text jarjarjar
		When clicking on element with xpath
		 //input[@class='btn btn-xs btn-primary' and
		 @type='submit' and @value='Zaloguj']
	''')

@then ('user will be logged as admin and redirected to /admin')
def step(context):
	context.execute_steps(u'''
		Then it should have an url http://localhost:8000/admin/
	''')
```

Little story of usage step_creator
![1.png](https://raw.githubusercontent.com/me3eh/PB_Testing/production/hosting_for_images/wip_files_for_readme/1.step_creator_visiting_url.png)
![2.png](https://raw.githubusercontent.com/me3eh/PB_Testing/production/hosting_for_images/wip_files_for_readme/2.step_creator_filling_inputs.png)
![3.png](https://raw.githubusercontent.com/me3eh/PB_Testing/production/hosting_for_images/wip_files_for_readme/3.step_creator_clicking_submit_input.png)
you can save and load plans in application for later usage
![4.png](https://raw.githubusercontent.com/me3eh/PB_Testing/production/hosting_for_images/wip_files_for_readme/4.step_creator_saving_plan_of_action_for_future_usage.png)
application give opportunity to generate plans and later use it in plan as normal action
![5.png](https://raw.githubusercontent.com/me3eh/PB_Testing/production/hosting_for_images/wip_files_for_readme/5.step_creator_generating_as_action_for_later_usage.png)
![6.png](https://raw.githubusercontent.com/me3eh/PB_Testing/production/hosting_for_images/wip_files_for_readme/6.step_creator_can_be_used_once_again.png)
![7.png](https://raw.githubusercontent.com/me3eh/PB_Testing/production/hosting_for_images/wip_files_for_readme/7.step_creator_creating_new_plan.png)
![8.png](https://raw.githubusercontent.com/me3eh/PB_Testing/production/hosting_for_images/wip_files_for_readme/8.step_creator_generating_action_then.png)
![9.png](https://raw.githubusercontent.com/me3eh/PB_Testing/production/hosting_for_images/wip_files_for_readme/9.pb_testing_execution_of_test_in_web_browser.png)
![10.png](https://raw.githubusercontent.com/me3eh/PB_Testing/production/hosting_for_images/wip_files_for_readme/10.step_creator_exectution_in_cli.png)


Invoking tests
Use command behave <name_of_feature_file>