from django.db import models

# giving tuple to choices var
class_name = {('math','math'),
              ('english','english'),
              ('science','science'),
              ('history','history'),
}

# created a class with the following attributes
class DjangoClasses(models.Model):
    title = models.CharField(max_length=60, choices=class_name)
    coursenumber = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    instructorname = models.TextField(max_length=300, default='', blank=True, null=False)
    duration = models.FloatField(null=True, blank=True, default=None)

    objects = models.Manager()

    def __str__(self):
        return self.title
