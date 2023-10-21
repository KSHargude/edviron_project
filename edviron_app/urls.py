from django.contrib import admin
from django.urls import path

from edviron_app import views

urlpatterns = [
       path('fee_head/', views.fee_head_list, name='fee_head_list'),
       path('due/', views.due_list, name='due_list'),
       path('installment/', views.installment_list, name='installment_list'),
       path('payment/', views.payment_list, name='payment_list'),
       path('invoice/', views.invoice_list, name='invoice_list'),
       path('transaction/', views.transaction_list, name='transaction_list'),
   ]