from rest_framework import serializers
from books.models import *
from src.config import MYURL
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = "__all__"
        


class BookSerializer(serializers.ModelSerializer):
    book_img = serializers.SerializerMethodField()

    def get_book_img(self, obj):
        return f"{MYURL}{obj.book_img.url}"


    class Meta:
        model = BookModel
        fields = "__all__"




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiUserModel
        fields = ['telegram_id', 'lang']


    def validate(self, data):
        user_id = data.get('telegram_id')
        if not user_id.isdigit():
            raise serializers.ValidationError('Telegram id must consist of numbers')
        if ApiUserModel.objects.filter(telegram_id=user_id).exists():
            raise serializers.ValidationError('Telegram id with this id already exists.')
        return data
              


