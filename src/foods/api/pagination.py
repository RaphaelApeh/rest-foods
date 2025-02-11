from rest_framework import status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination


class RestPageNumberPagination(PageNumberPagination):
    page_size = 5
    page_query_param = "pages"


    def get_paginated_response(self, data):
        return Response({
            "status": "ok",
            "next_page": self.get_next_link(),
            "previous_page": self.get_previous_link(),
            "page": self.page.number,
            "restaurants": data,
            "user": self.request.user.username
        }, status=status.HTTP_200_OK)