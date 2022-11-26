from behave import *


@given ('visit localhost :D')
def step(context):
	context.execute_steps(u'''
		Given visiting site http://localhost:3000
	''')

@given ('Waiting for 3 seconds')
def step(context):
	context.execute_steps(u'''
		Given waiting for amount of seconds 3
	''')

@given ('logged in as admin')
def step(context):
	context.execute_steps(u'''
		Given visiting site http://127.0.0.1:8000/
		Given filling input with xpath //input[@class='form-control' and @name='username' and @id='user-name' and @type='text'] with text jar
		Given filling input with xpath //input[@class='form-control' and @id='user-password' and @name='password' and @type='password'] with text jarjarjar
		Given clicking on element with xpath //input[@class='btn btn-xs btn-primary' and @type='submit' and @value='Zaloguj']
		Given waiting for amount of seconds 6
		Then it should have an url http://127.0.0.1:8000/admin/
	''')

@given ('kkok')
def step(context):
	context.execute_steps(u'''
		Given visiting site https://google.com
		Given element with xpath (//h2[@class='title flex-left'])[1] should have text yes
	''')

@then ('Something')
def step(context):
	context.execute_steps(u'''
		Given visiting site http://127.0.0.1:8000/
		Then element with xpath //a[@href='/access'] should have text Deklaracja dostępności
	''')

@given ('Odwiedz strone oraz poczekaj 5 sekund')
def step(context):
	context.execute_steps(u'''
		Given visiting site http://127.0.0.1:8000/
		Given waiting for amount of seconds 5
	''')

@given ('Udowodnij, ze tekst sie zgadza')
def step(context):
	context.execute_steps(u'''
		Given visiting site http://127.0.0.1:8000/
		Then element with xpath //a[@href='/access'] should have text Deklaracja dostępności
	''')