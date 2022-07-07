from resources.user import UserApi
from resources.product import ProductApi, ProductsApi

def initialize_routes(api):
    api.add_resource(ProductsApi, '/api/products')
    api.add_resource(ProductApi, '/api/product/<id>')

    api.add_resource(UserApi, '/api/user')