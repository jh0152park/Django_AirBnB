from django.shortcuts import render
from django.http import JsonResponse
from .models import Category


# Create your views here.
def all_categories(request):
    all_categories = Category.objects.all()
    return JsonResponse(
        {
            "status": "success",
        },
    )
