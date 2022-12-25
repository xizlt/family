from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from people.models import People
from people.serializers import PeopleSerializer, AncestorsSerializer


class PeopleViewSet(ModelViewSet):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer

    @action(methods=['get'], detail=True, url_path='ancestors', url_name='detail_ancestors')
    def detail_ancestors(self, request, pk=None):
        request = self.get_queryset().filter(id=pk)
        depth = int(self.request.query_params.get('depth', 0))
        serializer = AncestorsSerializer(request, many=True, context={"depth": depth})

        return Response(serializer.data)
