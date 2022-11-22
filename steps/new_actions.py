from behave import *


@given('login as admin')
def step(context):
	context.execute_steps(u'''
		Given login
    ''')

# @given('login as admin')
# def step(context):
#     context.execute_steps(u'''
#         Given login
#     ''')