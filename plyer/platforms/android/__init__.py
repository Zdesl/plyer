from os import environ
from jnius import autoclass

ANDROID_VERSION = autoclass('android.os.Build$VERSION')
SDK_INT = ANDROID_VERSION.SDK_INT

try:
    from android import config
    ns = config.JAVA_NAMESPACE
except (ImportError, AttributeError):
    ns = 'org.renpy.android'

if 'PYTHON_SERVICE_ARGUMENT' in environ:
    PythonActivity = autoclass(ns + '.PythonActivity')
    activity = PythonActivity.mActivity
else:
    PythonActivity = autoclass(ns + '.PythonActivity')
    activity = PythonActivity.mActivity
