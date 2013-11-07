from mycarhistory.settings.base  import *

SECRET_KEY = 'fake'

TEST_DISCOVER_TOP_LEVEL = root('..')
TEST_DISCOVER_PATTERN = "test_*"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
    },
}
