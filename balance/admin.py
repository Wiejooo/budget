from django.contrib import admin

from .models import Expense, ExpenseCategory

admin.site.register(Expense)
admin.site.register(ExpenseCategory)
admin.site.register(models.Income)
admin.site.register(models.IncomeCategory)
