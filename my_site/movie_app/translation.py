from .models import (Category,Country,Director,Actor,
                     Genre,Movie,MovieLanguage)
from modeltranslation.translator import TranslationOptions,register

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name',)

@register(Country)
class CountryTranslationOptions(TranslationOptions):
    fields = ('country_name',)

@register(Director)
class DirectorTranslationOptions(TranslationOptions):
    fields = ('director_name','bio')

@register(Actor)
class ActorTranslationOptions(TranslationOptions):
    fields = ('actor_name','bio')

@register(Genre)
class GenreTranslationOptions(TranslationOptions):
    fields = ('genre_name',)

@register(Movie)
class MovieTranslationOptions(TranslationOptions):
    fields = ('actor','director','genre','country','movie_name', 'description', 'slogan')

@register(MovieLanguage)
class MovieLanguageTranslationOptions(TranslationOptions):
    fields = ('language',)