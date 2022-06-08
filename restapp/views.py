from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  MoringaMerch
from .serializer import MerchSerializer

class MerchList(APIView):
    def get(self, request, format=None):
        all_merch = MoringaMerch.objects.all()
        serializers = MerchSerializer(all_merch, many=True)
        return Response(serializers.data)

