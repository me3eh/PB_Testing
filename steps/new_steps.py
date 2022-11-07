from behave import *

@when('i log in into site')
def step_impl(context):
    context.execute_steps(u'''
        when visiting url https://youshstg.myshopify.com
         and filling input with id password text lailtu
        and clicking submit button
        then it should have an url https://youshstg.myshopify.com/
    ''')


@given('kekw')
def step(context):
	context.execute_steps(u'''
		Given visiting site https://gram.pl
		Given clicking on element with xpath //a[@href='https://forum.gram.pl/' and contains(@class, 'menu-link') and @target='_blank' and @rel='noopener noreferrer']
	''')

@given ('Something')
def step(context):
	context.execute_steps(u'''
		Given visiting site https://gram.pl
		Given clicking on element with xpath //button[@class='menu-link']
	''')
@given ('Something')
def step(context):
	context.execute_steps(u'''
		Given visiting site https://google.com
		None
	''')
@given ('Something')
def step(context):
	context.execute_steps(u'''
		Given visiting site https://google.com
		None
	''')
@given ('kekw')
def step(context):
	context.execute_steps(u'''
		Given visiting site https://google.com
		None
	''')
@given ('Something')
def step(context):
	context.execute_steps(u'''
		Given visiting site https://google.com
		Then clicking on element with xpath 
	''')
