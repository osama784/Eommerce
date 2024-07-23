from django_components import component


@component.register("product")
class Product(component.Component):
    template_name = "product/template.html"

    def get_context_data(self, name, new_price, old_price, number_stars, image_url, company, category):
        return {
            "name": name,
            "new_price": new_price,
            "old_price": old_price,
            "number_stars": number_stars,
            "image_url": image_url,
            "company": company,
            "category": category

        }
