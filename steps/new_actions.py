from behave import *


@then ('user will be logged as dean')
def step(context):
	context.execute_steps(u'''
		Given waiting for amount of seconds 5
		Then it should have an url http://127.0.0.1:8000/dean/panel
	''')

@given ('login as a dean')
def step(context):
	context.execute_steps(u'''
		Given visiting site http://127.0.0.1:8000/
		Given filling input with xpath //input[@class='form-control' and @name='username' and @id='user-name' and @type='text'] with text huhi
		Given filling input with xpath //input[@class='form-control' and @id='user-password' and @name='password' and @type='password'] with text huhihuhi
		Given clicking on element with xpath //input[@class='btn btn-xs btn-primary' and @type='submit' and @value='Zaloguj']
	''')

@given ('testing adding question')
def step(context):
	context.execute_steps(u'''
		Given  login as a dean
	''')

@when ('something really')
def step(context):
	context.execute_steps(u'''
		Given  login as a dean
		Given clicking on element with xpath //a[@aria-expanded='false' and @class='dropdown-toggle' and @data-toggle='dropdown' and @href='#!']
		Given clicking on element with xpath //a[@href='/dean/questions/category/add']
		Given waiting for amount of seconds 5
	''')