from django.db import models

# Create your models here.
class Somas(models.Model):
    idSomas = models.AutoField(primary_key=True)
    valor1 = models.FloatField(verbose_name='Primeiro Valor:')
    valor2 = models.FloatField(verbose_name='Segundo Valor:')
    resultado = models.FloatField(verbose_name='resultado',null=True,blank=True)

    def __str__(self):
        return '{}'.format(self.resultado)


    def save(self):
        if not self.resultado:
            self.resultado = float(self.valor1) + float(self.valor2)
        super(Somas, self).save()
    
    class Meta:
        managed = True
        db_table = 'Somas'
