from behave import *


@then ('user will be logged as admin')
def step(context):
	context.execute_steps(u'''
		Then it should have an url http://localhost:8000/admin/
	''')