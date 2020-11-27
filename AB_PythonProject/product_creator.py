from domain.product import Product
from domain.tshirt_product import TShirtProduct
from domain.sneakers_product import SneakersProduct
from domain.customizable_sneakers_product import CustomizableSneakersProduct

class ProductCreator():
    def create(self, type_product):
        if type_product == 'TShirtProduct':
            product = TShirtProduct()
        elif type_product == 'SneakersProduct':
            product = SneakersProduct()
        elif type_product == 'CustomizableSneakersProduct':
            product = CustomizableSneakersProduct()
        else:
            raise TypeError('Не удалось создать объект Product. Указан неверный тип продукта.')

        return product