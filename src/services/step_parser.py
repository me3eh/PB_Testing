import pdb
import re

def something():
    with open("steps/new_steps.py", "r") as f:
        c = f.read()
    # pdb.set_trace()
    a = re.findall('@given.*|@when.*|@then.*', c)
    # a = re.split('@given|@when|@then', c)
    print(len(a))
    text = 'sprawdzenie_strony_rails'
    b = re.findall(f'@given.*{text}', a[1])
    if len(b) != 0:
        print("dupsko")
    print(b)
    print(a)
something()
