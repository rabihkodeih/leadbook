from rest_framework import serializers
from api.models import Company, Secretary, Director, Subsidiary


class SecretarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Secretary
        fields = ('name',
                  'email',
                  'phone')


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ('name',
                  'position')


class SubsidiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subsidiary
        fields = ('name',
                  'type',
                  'total_asset',
                  'percentage')


class CompanySerializer(serializers.ModelSerializer):
    corporate_secretary = SecretarySerializer(many=True)
    director = DirectorSerializer(many=True)
    subsidiary = SubsidiarySerializer(many=True)

    class Meta:
        model = Company
        fields = ('company_name',
                  'security_code',
                  'office_address',
                  'email_address',
                  'country',
                  'phone',
                  'fax',
                  'npwp',
                  'company_website',
                  'ipo_date',
                  'board',
                  'sector',
                  'sub_sector',
                  'registrar',
                  'corporate_secretary',
                  'director',
                  'subsidiary')


# end of file
