from behave import *

@then ('user will have greetings with their role in profile')
def step(context):
	context.execute_steps(u'''
		Then element with xpath //a[@class='no-hover cursor-default no-focus' and @href='#!'] contains text Witaj (Dziekan)
	''')

@then ('user will be logged as admin and redirected to /admin')
def step(context):
	context.execute_steps(u'''
		Then it should have an url http://localhost:8000/admin/
	''')

@when('logged as dean visiting question section')
def step(context):
	context.execute_steps(u'''
		Given logging as dean
		When clicking on element with xpath (//a[@class='dropdown-toggle' and @data-toggle='dropdown'and @href='#!' and @aria-expanded='false'])[3]
		When clicking on element with xpath //a[@href='/dean/questions/category/add']
		When filling input with xpath //input[@type='None' and @name='text' and @class='form-control' and @onchange='removeError(this)' and @maxlength='512' and @required='' and @id='id_text'] with text cos_nowego
		When selecting option Czas (2023-01-04 - 2023-01-27) from select with xpath //select[@class='form-control' and @id='id_requisition' and @name='requisition' and @onchange='addRequisition(this)']
		When filling input with xpath //input[@class='form-control' and @id='add_question' and @onchange='removeQuestionError(this)' and @type='text'] with text Ile kapie sie bobr?
		When clicking on element with xpath //button[@class='btn btn-xs btn-primary margin-left-6' and @onclick='addQuestion()' and @type='button']
		When waiting for amount of seconds 5
		When clicking on element with xpath //input[@class='btn btn-xs btn-primary' and @onclick='send()' and @type='button' and @value='Dodaj']
	''')

@then('question will be created')
def step(context):
	context.execute_steps(u'''
		Then element with xpath //tbody contains text cos_nowego
	''')

@when ('entering admin panel and trying to activate maintenance mode')
def step(context):
	context.execute_steps(u'''
		When visiting site http://localhost:8000/admin/
		When clicking on element with xpath //button[@onclick='toggleModal(1)']
		When clicking on element with xpath //input[@type='submit' and @value='Are you sure?']
	''')

@then ('maintenance mode will be on, based on displaying text')
def step(context):
	context.execute_steps(u'''
		Then element with xpath (//tr)[1] contains text Maintenance mode ACTIVATED
	''')

@then ('maintenance mode will be off, based on displaying text')
def step(context):
	context.execute_steps(u'''
		Then element with xpath (//tr)[1] contains text Maintenance mode Deactivated
	''')