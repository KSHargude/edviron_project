from django.db import models

# Create your models here.
class FeeHead(models.Model):
    name=models.CharField(max_length=100)
    student_filtering_options=models.CharField(max_length=300)
    frequency_moths=models.IntegerField(max_length=200)
    amount=models.DecimalField()

class Due(models.Model):
    fee_head=models.ForeignKey(FeeHead,on_delete=models.CASCADE())
    start_date=models.DateField()
    frequency_month=models.IntegerField()

class Installment(models.Model):
    due=models.ManyToManyField(Due)

class Payment(models.Model):
    amount=models.DecimalField()
    due=models.ForeignKey(Due,on_delete=models.CASCADE())
    payment_date=models.DateField()

class Invoice(models.Model):
    due=models.ForeignKey(Due,on_delete=models.CASCADE())
    invoice_date=models.DateField()
    total_amount=models.DecimalField()

class Transaction(models.Model):
    payment=models.ForeignKey(Payment,on_delete=models.CASCADE())
    invoice=models.ForeignKey(Invoice,on_delete=models.CASCADE())
    transaction_date=models.DateField()


