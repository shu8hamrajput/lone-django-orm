import django; django.setup()

from orm.models import *

a = User.objects.all()
print(a)
