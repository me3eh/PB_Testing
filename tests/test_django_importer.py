from url_importer import django
import sys
import io

def test_call():
    assert django.import_urls() == False
