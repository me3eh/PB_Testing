from behave import *


@given ('logging as dean')
def step(context):
	context.execute_steps(u'''
		Given visiting site http://localhost:8000/
		When filling input with xpath //input[@class='form-control' and @id='user-name' and @name='username' and @type='text'] with text huhi
		When filling input with xpath //input[@class='form-control' and @id='user-password' and @name='password' and @type='password'] with text huhihuhi
		When clicking on element with xpath //input[@class='btn btn-xs btn-primary' and @type='submit' and @value='Zaloguj']
	''')

@when ('logging in with username and password for admin')
def step(context):
	context.execute_steps(u'''
		When visiting site http://localhost:8000/
		When filling input with xpath //input[@class='form-control' and @id='user-name' and @name='username' and @type='text'] with text jar
		When filling input with xpath //input[@class='form-control' and @id='user-password' and @name='password' and @type='password'] with text jarjarjar
		When clicking on element with xpath //input[@class='btn btn-xs btn-primary' and @type='submit' and @value='Zaloguj']
	''')