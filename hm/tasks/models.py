from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

TASK_STATUS = ((0,_("Created")), (1,_('To Do')), (2,_('Doing')), (3,_('Done')))
# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=200)

class TaskUser(models.Model):
    task = models.ForeignKey(Task)
    user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = "tasks")
    date_assign = models.DateField(null=False, blank=False)
    date_done =  models.DateField(null=False, blank=False)
    status = models.PositiveSmallIntegerField(choices=TASK_STATUS,default=0)
