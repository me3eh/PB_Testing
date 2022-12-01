from behave import *


# @given('haha')
# def step(context, xpath, text):
#    context.execute_steps(u'''
# 		Given visiting site https://google.com
# 	''')

@when ('Something')
def step(context):
	context.execute_steps(u'''
		Given visiting site https://google.com
	''')

@given ('haha2')
def step(context):
	context.execute_steps(u'''
		Given visiting site https://gram.pl
	''')