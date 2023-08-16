from .serializers import *
from books.models import *
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

class CategoryView(APIView):

    def get(self, request):
        category = CategoryModel.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class BookView(APIView):

    def get(self, request):
        category = BookModel.objects.all()
        serializer = BookSerializer(category, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class UserView(APIView):
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['GET'])
def by_category_id(request, id):
    by_cate = BookModel.objects.filter(category_id=id)
    if by_cate:
        serializer = BookSerializer(by_cate, many=True)
        if serializer:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'message': 'Category information was not found'}, status=status.HTTP_404_NOT_FOUND)




class BookIDView(APIView):

    def get(self, request, pk):
        book = BookModel.objects.filter(pk=pk)
        if book:
            serializer = BookSerializer(book, many=True)
            if serializer:
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'Book Id not found'}, status=status.HTTP_404_NOT_FOUND)

    