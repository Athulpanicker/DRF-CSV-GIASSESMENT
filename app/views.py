from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from .models import user
from .serializers import CSVSerializer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from io import TextIOWrapper
import csv
import sys
@api_view(['POST'])
def postcsv(request):
    uploadedfile = request.FILES.get('file')
    if not uploadedfile:
        return JsonResponse({"error": "please upload a CSV file."}, status=status.HTTP_400_BAD_REQUEST)
    if not uploadedfile.name.endswith('.csv'):
        return JsonResponse({"error": "only CSV files are allowed."}, status=status.HTTP_400_BAD_REQUEST)
    try:
        wrapped_file = TextIOWrapper(uploadedfile, encoding='utf-8')
        csvfile = csv.DictReader(wrapped_file)
    except:
        return JsonResponse({"error": f"Failed to read CSV file: {sys.exc_info()[1]}"}, status=status.HTTP_400_BAD_REQUEST)
    saved = 0
    rejected = 0
    error = []
    for i, row in enumerate(csvfile, start=2):
        serializer = CSVSerializer(data=row)
        if serializer.is_valid():
            serializer.save()
            saved += 1
        else:
            rejected += 1
            error.append({"row": i, "errors": serializer.errors})

    return JsonResponse({"saved": saved,"rejected": rejected,"errors": error}, status=status.HTTP_200_OK)

