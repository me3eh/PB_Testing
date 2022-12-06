from behave import *


@when('i log in into site')
def step_impl(context):
    context.execute_steps(u'''
        when visiting url https://youshstg.myshopify.com
         and filling input with id password text lailtu
        and clicking submit button
        then it should have an url https://youshstg.myshopify.com/
    ''')

#@given ('sprawdzenie_strony_rails')
# def step(context):
# 	context.execute_steps(u'''
# 		Given visiting site http://localhost:3000
# 		Given selecting option joe from select with xpath //select[@id='id_created_by' and @name='created_by' and @required='']
# 		Given filling input with xpath //input[@name='lol'] with text cos fajnego
# 		Given waiting for amount of seconds 10
# 	''')

@given ('huhi')
def step(context):
	context.execute_steps(u'''
		Given visiting site http://localhost:3000
		Given clicking on element with xpath //input[@type='checkbox' and @id='vehicle3' and @name='vehicle3' and @value='Boat']
	''')

@given ('yieks')
def step(context):
	context.execute_steps(u'''
		Given visiting site https://google.com
	''')

@given ('looking if gonna go')
def step(context):
	context.execute_steps(u'''
		Given  visit site gram.pl
		Given  sleeping 6 seconds
	''')

@given ('Something')
def step(context):
	context.execute_steps(u'''
		Given visiting site https://google.com
		Then element with xpath //p should have text jkk
	''')

@given ('logging as admin with credentials jar pass')
def step(context):
	context.execute_steps(u'''
		Given visiting site http://127.0.0.1:8000/
		Given filling input with xpath //input[@class='form-control' and @name='username' and @id='user-name' and @type='text'] with text jar
		Given filling input with xpath //input[@class='form-control' and @name='password' and @id='user-password' and @type='password'] with text jarjarjar
		Given clicking on element with xpath //input[@class='btn btn-xs btn-primary' and @type='submit' and @value='Zaloguj']
		Then it should have an url http://127.0.0.1:8000/admin
	''')

@given ('something really')
def step(context):
	context.execute_steps(u'''
		Given  login as a dean
		Given clicking on element with xpath //a[@href='/dean/questions/category/add']
		Given waiting for amount of seconds 5
	''')