from django.http import JsonResponse, request
from django.shortcuts import render
from dashboard.models import Order
from django.core import serializers

# Create your views here.
def dashboard_with_pivot(request):
    return render(request, 'dashboard_with_pivot.html', {})

def pivot_data(request):
    dataset = Order.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)