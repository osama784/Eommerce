import math

def product_attachment_download(instance, filename):
    return f'products/{instance.product.handle}/attachments/{filename}'  

def product_image_download(instance, filename):
    return f'products/{instance.handle}/{filename}' 

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
