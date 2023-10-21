from django.shortcuts import render
from .models import FeeHead, Due, Installment, Payment, Invoice, Transaction


# Create your views here.
def fee_head_list(request):
    fee_heads = FeeHead.objects.all()
    return render(request, 'your_app/fee_head_list.html', {'fee_heads': fee_heads})

def due_list(request):
    dues = Due.objects.all()
    return render(request, 'your_app/due_list.html', {'dues': dues})

def installment_list(request):
    installments = Installment.objects.all()
    return render(request, 'your_app/installment_list.html', {'installments': installments})

def payment_list(request):
    payments = Payment.objects.all()
    return render(request, 'your_app/payment_list.html', {'payments': payments})

def invoice_list(request):
    invoices = Invoice.objects.all()
    return render(request, 'your_app/invoice_list.html', {'invoices': invoices})

def transaction_list(request):
    transactions = Transaction.objects.all()
    return render(request, 'your_app/transaction_list.html', {'transactions': transactions})

