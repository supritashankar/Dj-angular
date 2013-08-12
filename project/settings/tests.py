from os import path
import sys

TEST_DISCOVER_TOP_LEVEL = path.dirname(path.dirname(__file__))
TEST_DISCOVER_ROOT = path.join(TEST_DISCOVER_TOP_LEVEL)
TEST_RUNNER = 'discover_runner.DiscoverRunner'

if 'test' in sys.argv:
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/tmp/book.db'
    }

TESTSERVER='http://testserver'
SERVERNAME='127.0.0.1:8000'
