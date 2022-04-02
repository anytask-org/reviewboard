import sys
import os
import site

sys.path.extend(['', '/usr/local/lib/python27.zip', '/usr/local/lib/python2.7', '/usr/local/lib/python2.7/plat-linux2', '/usr/local/lib/python2.7/lib-tk', '/usr/local/lib/python2.7/lib-old', '/usr/local/lib/python2.7/lib-dynload', '/usr/local/lib/python2.7/site-packages', '/app', '/app/anytask_sync_extension'])
#os.environ["PYTHONPATH"] = ":".join(sys.path)
site.addsitedir('/usr/local/lib/python2.7/site-packages')

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
