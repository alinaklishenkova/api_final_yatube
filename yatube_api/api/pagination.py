from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class ConditionalPagination(PageNumberPagination):
    page_size_query_param = 'limit'
    page_query_param = 'offset'

    def paginate_queryset(self, queryset, request, view=None):
        if 'limit' in request.query_params or 'offset' in request.query_params:
            return super().paginate_queryset(queryset, request, view)
        return None

    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data
        })
