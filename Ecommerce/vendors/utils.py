def get_vendor_prefix_id(instance, *args, **kwargs):
    return f"vendors"

def get_vendor_display_name(instance, *args, **kwargs):
    return f'{instance.name}'