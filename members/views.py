from django.shortcuts               import render
from rest_framework.decorators      import api_view
from django.http                    import HttpResponse
from .serializers                   import MemberSerializer
from .models                        import Member
# Create your views here.


@api_view(['GET'])
def index(reqeust):
    member = Member.objects.all();
    serializers = MemberSerializer(member,many=True)
    return HttpResponse(serializers.data)