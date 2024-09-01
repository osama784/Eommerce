def product_attachment_download(instance, filename):
    # suffix = filename.split('.')[1]
    # filename = f"{instance.name.lower().replace("", "_")}.{suffix}"
    return f'products/{instance.product.handle}/{filename}'  

def product_image_download(instance, filename):
    return f'products/{instance.handle}/{filename}'  