from django.db import models


class People(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mother_id = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children_mother', blank=True, null=True)
    father_id = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children_father', blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
