from url_importer import django_importer
import sys
import io

def test_call():
    assert django_importer.call() == False
