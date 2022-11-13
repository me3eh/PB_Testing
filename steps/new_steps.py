from behave import *

@when('i log in into site')
def step_impl(context):
    context.execute_steps(u'''
        when visiting url https://youshstg.myshopify.com
         and filling input with id password text lailtu
        and clicking submit button
        then it should have an url https://youshstg.myshopify.com/
    ''')

@given ('Something')
def step(context):
	context.execute_steps(u'''
		Then it should have an url Additional
		Then it should have an url Additional
		Given visiting site https://google.com
		Then it should have an url Additional
		Then it should have a title Additional
	''')
@given ('asdfasdf')
def step(context):
	context.execute_steps(u'''
		Then it should have an url Additional
		Given visiting site https://google.com
	''')
