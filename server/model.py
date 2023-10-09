from django.db import models



class StudentPortalAdmin(models.Model):
    created_by = models.CharField(max_length=200,null=True, blank=True)
    created_at = models.DateTimeField()


    class Meta :
        abstract = True