from rest_framework import serializers
from .models import Member

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model=Member
        fields=[
            'login_id',
            'apikey',
            'auth_type',
            'name',
            'password',
            'password_answer',
            'password_question']