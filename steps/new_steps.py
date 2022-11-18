from behave import *

@when('i log in into site')
def step_impl(context):
    context.execute_steps(u'''
        when visiting url https://youshstg.myshopify.com
         and filling input with id password text lailtu
        and clicking submit button
        then it should have an url https://youshstg.myshopify.com/
    ''')

#
# @given ('sprawdzenie_strony_rails')
# def step(context):
# 	context.execute_steps(u'''
# 		Given visiting site http://localhost:3000
# 		Given selecting option joe from select with xpath //select[@id='id_created_by' and @name='created_by' and @required='']
# 		Given filling input with xpath //input[@name='lol'] with text cos fajnego
# 		Given waiting for amount of seconds 10
# 	''')
@given ('bawienie_sie_z_railsami')
def step(context):
	context.execute_steps(u'''
		Given visiting site http://localhost:3000
		Given selecting option maciek from select with xpath //select[@id='id_created_by' and @name='created_by' and @required='']
		Given filling input with xpath //input[@name='inpucik'] with text jakos to idzie
		Given waiting for amount of seconds 10
	''')

@given ('login')
def step(context):
	context.execute_steps(u'''
		Given login
    ''')
