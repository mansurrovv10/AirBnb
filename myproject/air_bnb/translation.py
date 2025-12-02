from .models import City, Property, Country, Rules
from modeltranslation.translator import TranslationOptions,register

@register(City)
class CityTranslationOptions(TranslationOptions):
    fields = ('city_name',)




@register(Country)
class CountryTranslationOptions(TranslationOptions):
    fields = ('country_name',)


@register(Rules)
class RulesTranslationOptions(TranslationOptions):
    fields = ('rules_name',)


@register(Property)
class PropertyTranslationOptions(TranslationOptions):
    fields = ('title','description')


