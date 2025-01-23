from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import News
from .serializers import NewsSerializer
from .permissions import IsAuthorOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsAuthorOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['author', 'created_at']
    search_fields = ['title', 'content']
    ordering_fields = ['created_at', 'title']

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        news = self.get_object()
        user = request.user
        if user in news.likes.all():
            news.likes.remove(user)
            return Response({'status': 'unliked'})
        else:
            news.likes.add(user)
            return Response({'status': 'liked'})

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "index.html"