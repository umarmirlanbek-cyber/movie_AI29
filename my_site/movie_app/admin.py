from django.contrib import admin
from .models import UserProfile,Category,Review,Favorite,FavoriteMovie,History,ReviewLike,Rating,Moments,MovieLanguage,Movie,Genre,Actor,Director,Country
from modeltranslation.admin import TranslationAdmin,TranslationInlineModelAdmin

class GenreInLine(admin.TabularInline,TranslationInlineModelAdmin):
    model = Genre
    extra = 1

@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    inlines = [GenreInLine]
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

class MovieLanguageInLine(admin.TabularInline,TranslationInlineModelAdmin):
    model = MovieLanguage
    extra = 1

class MomentsInLine(admin.TabularInline):
    model = Moments
    extra = 1

@admin.register(Movie)
class MovieAdmin(TranslationAdmin):
    inlines = [MovieLanguageInLine,MomentsInLine]
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

@admin.register(Actor,Country,Director)
class AllAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

class ReviewLikeInLine(admin.TabularInline):
    model = ReviewLike
    extra = 1

class ReviewAdmin(admin.ModelAdmin):
    inlines = [ReviewLikeInLine]

admin.site.register(UserProfile)
admin.site.register(Review,ReviewAdmin)
admin.site.register(Rating)
admin.site.register(Favorite)
admin.site.register(FavoriteMovie)
admin.site.register(History)