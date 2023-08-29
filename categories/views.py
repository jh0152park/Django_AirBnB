from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category


@api_view()
def all_categories(request):
    all_categories = Category.objects.all()
    return Response(
        {
            "status": "success",
            # "categories": serializers.serialize("json", all_categories),
        },
    )
