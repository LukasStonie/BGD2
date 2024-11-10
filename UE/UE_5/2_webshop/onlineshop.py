from flask import Flask
from flask import request
from flask import jsonify

import redis
import os

REDIS_PRODUCT = "product"
REDIS_PRODUCTS = "products"
REDIS_CATEGORY  ="category"
REDIS_PRODUCT_RANK ="product_rank"

REDIS_PRICE_RANKED = "price_ranked"

PRODUCT_NAME = "name"
PRODUCT_PRICE="price"
PRODUCT_CATEGORY ="category"


app = Flask(__name__)

red = redis.Redis(host=os.environ['REDIS_HOST'], port=6379, decode_responses=True)

# route for creating a new product
@app.route('/products', methods=['POST'])
def create_product():
    # get the product data from the request body
    product_data = request.get_json(force=True)
    
    # parse needed information from body
    product_name = product_data[PRODUCT_NAME]
    product_price = product_data[PRODUCT_PRICE]
    product_category = product_data[PRODUCT_CATEGORY]
    
    # add product
    red.hset(REDIS_PRODUCT+product_name,mapping=product_data)
    
    # add product name into sorted set for later query of cheapest N products
    red.zadd(REDIS_PRICE_RANKED, {product_name: product_price}, nx=True)
    
    # add category of product to set
    red.sadd(REDIS_CATEGORY+product_category, product_name)
    
    # add product to set of all products
    red.sadd(REDIS_PRODUCTS, product_name)

    return f"Product {product_name} was succesfully created",200

# route for getting all products
@app.route('/products', methods=['GET'])
def get_products():
    # get all product name from product set
    product_names = red.smembers(REDIS_PRODUCTS)
    
    # iterate and resolve product name to full product
    products = [red.hgetall(REDIS_PRODUCT+x) for x in product_names]
    
    return jsonify(products)
        
# route for getting a specific product
@app.route('/products/<product_name>', methods=['GET'])
def product_details(product_name):
    # get the product that has the correct hash value
    details = red.hgetall(REDIS_PRODUCT+product_name)
    
    # increment a counter for this specific product for later rank queries
    red.incr(REDIS_PRODUCT_RANK+product_name)
    
    return jsonify(details)

#  route for getting all products of a certain category
@app.route('/categories/<category>', methods=['GET'])
def products_in_category(category):
    
    # get all product names for a certain category
    products_in_category = red.smembers(REDIS_CATEGORY+category)
    
    # iterate over all product names and resolve to full product
    product_list = []
    for p_name in products_in_category:
        product_list.append(red.hgetall(REDIS_PRODUCT+p_name))
        
    return jsonify(product_list)

# route for getting the cheapest N products
@app.route('/cheapest/<n>', methods=['GET'])
def cheapest(n):
    # check if N is a valid value (>0)
    n =  int(n)
    if n >0:
        # get the first N products from sorted set (N-1 because value is includes upper bound)
        p_names = red.zrange(REDIS_PRICE_RANKED, 0,int(n-1))

        # iterate and resolve product name to full product
        products = [red.hgetall(REDIS_PRODUCT+x) for x in p_names]
        return jsonify(products)
    else:
        return f"Cannot get cheapest products for N=0 or negative number"

#route for getting the rank (nr. of visits) of a product
@app.route('/productRank/<product_name>', methods=['GET'])
def product_rank(product_name):
    # check if the product name exists as a key
    exists = red.exists(REDIS_PRODUCT_RANK+product_name)
    if  exists == 1:
        # return the saved count as an integer
        return jsonify(int(red.get(REDIS_PRODUCT_RANK+product_name)))
    else:
        # return 0 as an integer
        return jsonify(0)
    
# route for clearing the redis db
@app.route('/deleteAll', methods=['DELETE'])
def flush_all():
    try:
        # flush the whole redis cache
        red.flushall()
        return f"Succesfully cleared all the data", 200
    except:
        return f"Something unexpected happend, please check the server logs", 500
    