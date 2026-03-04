from rest_framework import routers
from django.urls import include,path
from .views import (UserProfileListAPIView,UserProfileDetailAPIView ,HistoryViewSet, CategoryListAPIView, CategoryDetailAPIView,
                    GenreListAPIView, GenreDetailAPIView, ReviewViewSet, CountryListAPIView,CountryDetailAPIView, MovieListAPIView,
                    MovieLanguageViewSet, DirectorListAPIView, ActorListAPIView,DirectorDetailAPIView,ActorDetailAPIView,
                    MomentsViewSet, RatingViewSet, ReviewLikeViewSet, FavoriteViewSet,
                    FavoriteMovieViewSet, MovieDetailAPIView,LoginView,LogoutView,RegisterView)
router = routers.DefaultRouter()

router.register(r'history',HistoryViewSet)
router.register(r'review',ReviewViewSet)
router.register(r'movie_language',MovieLanguageViewSet)
router.register(r'moment',MomentsViewSet)
router.register(r'rating',RatingViewSet)
router.register(r'review_like',ReviewLikeViewSet)
router.register(r'favorite',FavoriteViewSet)
router.register(r'favorite_movie',FavoriteMovieViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user/',UserProfileListAPIView.as_view(),name='user_list'),
    path('user/<int:pk>',UserProfileDetailAPIView.as_view(),name='user_detail'),
    path('category/',CategoryListAPIView.as_view(),name='category_list'),
    path('category/<int:pk>',CategoryDetailAPIView.as_view(),name='category_detail'),
    path('genre/', GenreListAPIView.as_view(), name='genre_list'),
    path('genre/<int:pk>',GenreDetailAPIView.as_view(),name='genre_detail'),
    path('movie/',MovieListAPIView.as_view(),name='movie_list'),
    path('movie/<int:pk>',MovieDetailAPIView.as_view(),name='movie_detail'),
    path('country/',CountryListAPIView.as_view(),name='country_list'),
    path('country/<int:pk>',CountryDetailAPIView.as_view(),name='country_detail'),
    path('actor/',ActorListAPIView.as_view(),name='actor_list'),
    path('actor/<int:pk>',ActorDetailAPIView.as_view(),name='actor_detail'),
    path('director/',DirectorListAPIView.as_view(),name='director_list'),
    path('director/<int:pk>',DirectorDetailAPIView.as_view(),name='director_detail')
]
