from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self,validated_date):
        user = User.objects.create_user(**validated_date)
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only= True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"


class UserProfileSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["id", "first_name", "last_name"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["category_name"]


class ProductPhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPhotos
        fields = ["image"]


class RatingsSerializer(serializers.ModelSerializer):
    user = UserProfileSimpleSerializer()
    class Meta:
        model = Ratings
        fields = ["user", "stars"]


class ReviewSerializer(serializers.ModelSerializer):
    author = UserProfileSimpleSerializer()
    created_date = serializers.DateTimeField(format="%d-%m-%Y %H:%M")
    class Meta:
        model = Reviews
        fields = ["id", "author", "text", "parent_review", "created_date"]



class ProductListSerializer(serializers.ModelSerializer):
    product = ProductPhotosSerializer(read_only=True, many=True)
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = ["id", "product_name", "product", "category", "price", "date"]


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    ratings = RatingsSerializer(read_only=True, many=True)
    review = ReviewSerializer(read_only=True, many=True)
    product = ProductPhotosSerializer(read_only=True, many=True)
    date = serializers.DateField(format="%d-%m-%Y")
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ["product_name", "category", "description", "price", "product",
                  "product_video", "active", "date", "average_rating", "ratings", "review"]


    def get_average_rating(self, obj):
        return obj.get_average_rating()