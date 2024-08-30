def product_attachment_download(instance, filename):
    return f'products/{instance.product.handle}/{filename}'  