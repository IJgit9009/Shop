from .models import Product
from modeltranslation.translator import register, TranslationOptions

@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('product_name', 'description')