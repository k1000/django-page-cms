import os, sys
os.environ['DJANGO_SETTINGS_MODULE'] = 'example.settings'
from inspect import getmembers, ismodule

from django.conf import settings
from django.test.simple import run_tests as django_test_runner
from django.db.models import get_app, get_apps

test_dir = os.path.dirname(__file__)
sys.path.insert(0, test_dir)

def run_tests(test_labels=('pages',), verbosity=1, interactive=True,
        extra_tests=[]):
    results = django_test_runner(test_labels, verbosity, interactive,
        extra_tests)
    sys.exit(results)

if __name__ == '__main__':
    run_tests()