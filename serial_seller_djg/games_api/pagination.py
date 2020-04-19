from rest_framework.pagination import PageNumberPagination

class GamePageNumberPagination(PageNumberPagination):
    page_size = 16