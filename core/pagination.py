from django.conf import settings
from rest_framework.pagination import PageNumberPagination


class PageNumberPaginationWithPageSize(PageNumberPagination):
    """
    Override PageNumberPagination to enable page_size query parameter.

    For more information please see following link:
    https://www.django-rest-framework.org/api-guide/pagination/#pagenumberpagination
    """

    page_size_query_param = 'page_size'
    max_page_size = settings.MAX_PAGE_SIZE
