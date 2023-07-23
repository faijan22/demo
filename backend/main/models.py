from django.db import models

# to store the names of city and capitals in one model
class StoreCityAndCapitals(models.Model):
    '''
        name : char
        capital : char
    '''
    name = models.CharField(max_length=300)
    capital = models.CharField(max_length=300)

    class Meta:
        verbose_name = 'Store City and Capitals'
        verbose_name_plural = 'Store City and Capitals'

    def __str__(self):
        return str(self.id)