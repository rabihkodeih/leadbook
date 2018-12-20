from django.urls import path
from django.core.paginator import Paginator
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from common.decorators import handle_exceptions
from common.utils import query_string, eval_try_catch
from api.models import Company
from api.serializers import CompanySerializer


class CompanyListView(APIView):
    '''
    View to list all companies or companies filtered by their name.
    '''
    permission_classes = (IsAuthenticatedOrReadOnly,)
    renderer_classes = (JSONRenderer,)

    @handle_exceptions
    def get(self, request):
        page = query_string(request, 'page', int)
        length = query_string(request, 'length', int)
        company_name = query_string(request, 'company_name', str)
        prefetch_args = ('corporate_secretary', 'director', 'subsidiary')
        all_companies = Company.objects.prefetch_related(*prefetch_args).all()
        if company_name:
            all_companies = all_companies.filter(company_name__icontains=company_name)
        all_companies = all_companies.order_by('security_code')
        if page and length:
            paginator = Paginator(all_companies, length)
            companies = eval_try_catch(lambda: paginator.page(page), default_value=[])
        else:
            companies = all_companies
        serializer = CompanySerializer(companies, many=True)
        result = {'status_code': 200,
                  'message': 'successful',
                  'total_results': len(all_companies),
                  'page': page if page else 1,
                  'data': serializer.data}
        return Response(result)


class CompanyItemView(APIView):
    '''
    View to get single company using its security code / ticker symbol.
    '''
    permission_classes = (IsAuthenticatedOrReadOnly,)
    renderer_classes = (JSONRenderer,)

    @handle_exceptions
    def get(self, request, security_code):
        company = Company.objects.filter(security_code=security_code).first()
        if company:
            serializer = CompanySerializer(company)
            result = {'status_code': 200,
                      'message': 'successful',
                      'total_results': 1,
                      'data': serializer.data}
        else:
            result = {'status_code': 200,
                      'message': 'not found',
                      'total_results': 0}
        return Response(result)


urls = [
    path('companies/', CompanyListView.as_view(), name='url_companies'),
    path('company/<str:security_code>/', CompanyItemView.as_view(), name='url_company')
]


# end of file
