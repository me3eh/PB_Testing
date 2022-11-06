from behave import *

@when('i log in into site')
def step_impl(context):
    context.execute_steps(u'''
        when visiting url https://youshstg.myshopify.com
         and filling input with id password text lailtu
        and clicking submit button
        then it should have an url https://youshstg.myshopify.com/
    ''')


@when ('something called')
def step(context):
	context.execute_steps(u'''
		Given visiting site youshstg.myshopify.com
		Given filling input with xpath //input[@type='password' and contains(@class, 'form-input') and @id='password' and @name='password' and @autocomplete='nope'] with text lailtu
		None
	''')
@Given ('Something')
def step(context):
	context.execute_steps(u'''
		Given visiting site https://youshstg.myshopify.com
		Given filling input with xpath //input[@type='password' and contains(@class, 'form-input') and @id='password' and @name='password' and @autocomplete='nope'] with text lailtu
		None
	''')
@Given ('Another')
def step(context):
	context.execute_steps(u'''
		Given visiting site https://youshstg.myshopify.com
		Given filling input with xpath //input[@type='password' and contains(@class, 'form-input') and @id='password' and @name='password' and @autocomplete='nope'] with text lailtu
		Given clicking on element with xpath //button[@type='submit']
	''')

@Given ('Moj_plan')
def step(context):
	context.execute_steps(u'''
		Given visiting site https://youshstg.myshopify.com
		Given filling input with xpath //input[@type='password' and contains(@class, 'form-input') and @id='password' and @name='password' and @autocomplete='nope'] with text lailtu
		Given clicking on element with xpath //button[@type='submit']
		
	''')
