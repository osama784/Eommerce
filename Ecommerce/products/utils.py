from django.utils.text import slugify
import math

def get_prefix_id_product_attachment(instance, *args, **kwargs):
    return f'products/{instance.product.handle}/attachments'  

def get_prefix_id_product(instance, *args, **kwargs):
    return f'products/{instance.handle}' 

def get_display_name_product(instance, *args, **kwargs):
    return f'{instance.handle}'

def get_display_name_product_attachment(instance, *args, **kwargs):
    return f'{instance.product.handle}--attachments'

def custom_round(number):
    str_num = str(number)
    decimal_index = str_num.find('.')
    
    if decimal_index == -1:
        return number
    
    first_decimal_digit = int(str_num[decimal_index + 1])
    
    if first_decimal_digit >= 5:
        return math.ceil(number)
    else:
        return math.floor(number)
