from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

TYPES = (
        ('T', 'Transportation'),
        ('F', 'Food and drinks'),
        ('L', 'Leisure'),
        ('H', 'Health'),
        ('O', 'Other'),
    )

CURRENCY_CHOICE = (
        ('E', 'EURO'),
        ('D', 'DOLLAR'),
    )

class Account(models.Model):

    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()

    class Meta:
        verbose_name = _('Account')
        verbose_name_plural = _('Accounts')

    def __unicode__(self):
        pass
    

class Income(models.Model):

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=1, choices=CURRENCY_CHOICE)
    date = models.DateField()
    description = models.TextField()
    expense_type = models.CharField(max_length=1, choices=TYPES)
    bank_account = models.ForeignKey(Account)
    user =  models.ForeignKey(User)

    class Meta:
        verbose_name = _('Income')
        verbose_name_plural = _('Incomes')

    def __unicode__(self):
        pass
    

class Expense(models.Model):

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=1, choices=CURRENCY_CHOICE)
    date = models.DateField()
    description = models.TextField()
    expense_type = models.CharField(max_length=1, choices=TYPES)
    bank_account = models.ForeignKey(Account)
    user =  models.ForeignKey(User)

    class Meta:
        verbose_name = _('Expense')
        verbose_name_plural = _('Expenses')

    def __unicode__(self):
        pass
