from django.db import models

class Advertisement(models.Model):
    title = models.CharField('название', max_length=128 )
    des = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits = 10, decimal_places=2)
    auction = models.BooleanField('Торг', help_text='Отметить, если торг уместен')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Advertisement: Advertisement(id={self.id}, title={self.title}, price={self.price})'

    class Meta:
        db_table ='advertisements'