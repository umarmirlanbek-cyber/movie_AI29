from dataclasses import fields

from rest_framework import serializers
from .models import (UserProfile,Category,Country,Director,Actor,
                     Genre,Movie,MovieLanguage,Moments,Review,
                     Rating,ReviewLike,FavoriteMovie,Favorite,History)
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password', 'first_name','last_name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }

class UserProfileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name','last_name']

class UserProfileDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class UserProfileNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['avatar','username']

class CountryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id','country_name']

class DirectorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['id','director_name']

class ActorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['id','actor_name']

class GenreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id','genre_name']

class MovieListSerializer(serializers.ModelSerializer):
    year = serializers.DateTimeField(format('%Y'))
    country = CountryListSerializer(many=True)
    genre = GenreListSerializer
    class Meta:
        model = Movie
        fields = ['id','movie_image','movie_name','year','country','genre']

class MovieLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieLanguage
        fields = ['language','video']

class ReviewSerializer(serializers.ModelSerializer):
    created_date = serializers.DateTimeField(format('%d-%m-%Y %H:%M'))
    user = UserProfileNameSerializer()
    count_like = serializers.SerializerMethodField()
    class Meta:
        model = Review
        fields = ['id','user','created_date','comment','parent','count_like']

    def get_count_like(self,obj):
        return obj.get_count_like()

class MomentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moments
        fields = ['movie_moments']

class MovieDetailSerializer(serializers.ModelSerializer):
    year = serializers.DateTimeField(format='%d-%m-%Y')
    country = CountryListSerializer(many=True)
    director = DirectorListSerializer(many=True)
    actor = ActorListSerializer(many=True)
    language_movie = MovieLanguageSerializer(read_only=True,many=True)
    avg_rating = serializers.SerializerMethodField()
    count_people = serializers.SerializerMethodField()
    movie_review = ReviewSerializer(read_only=True,many=True)
    moment_review = MomentsSerializer(read_only=True,many=True)
    class Meta:
        model = Movie
        fields = ['movie_image','movie_trailer','movie_name','year',
                  'country','genre','types','actor','language_movie','slogan',
                  'director','movie_time','description','avg_rating','count_people',
                  'movie_review','moment_review']
    def get_avg_rating(self,obj):
        return obj.get_avg_rating()
    def get_count_people(self,obj):
        return obj.get_count_people()

class CountryDetailSerializer(serializers.ModelSerializer):
    movies_country = MovieListSerializer(read_only=True, many=True)
    class Meta:
        model = Country
        fields = ['country_name','movies_country']

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'

class ReviewLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewLike
        fields = '__all__'

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'

class FavoriteMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteMovie
        fields = '__all__'

class GenreDetailSerializer(serializers.ModelSerializer):
    movies_list = MovieListSerializer(read_only=True,many=True)
    class Meta:
        model = Genre
        fields = ['genre_name','movies_list']

class CategoryListSerializer(serializers.ModelSerializer):
    genre_category = GenreListSerializer
    class Meta:
        model = Category
        fields = ['id','category_name','genre_category']

class CategoryDetailSerializer(serializers.ModelSerializer):
    genre_category = GenreDetailSerializer(read_only=True,many=True)
    class Meta:
        model = Category
        fields = ['category_name','genre_category']

class DirectorDetailSerializer(serializers.ModelSerializer):
    director_movie = MovieListSerializer(read_only=True,many=True)
    class Meta:
        model = Director
        fields = ['director_name','director_image','age','bio','director_movie']

class ActorDetailSerializer(serializers.ModelSerializer):
    actor_movie = MovieListSerializer(read_only=True,many=True)
    class Meta:
        model = Actor
        fields = ['actor_name','actor_image','age','bio','actor_movie']