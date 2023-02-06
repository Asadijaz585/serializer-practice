# from django.shortcuts import render
import django_filters.rest_framework
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from django.db.models import Q
from django.template import loader
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
from rest_framework import generics

@csrf_exempt
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def snippet_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)

class filter_list(generics.ListAPIView):
    serializer_class = SnippetSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        return Snippet.objects.filter(user=user)

class search(generics.ListAPIView):
    serializer_class = SnippetSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        slug = self.kwargs['pk']
        return Snippet.objects.filter(slug=slug)
    # queryset_list = Snippet.objects.all()
    # filter_set = ['id', 'title', 'code', 'linenos', 'language', 'style']