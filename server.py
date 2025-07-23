from flask import Flask, jsonify, request
from sql_connection import get_sql_connection
from products_dao import get_all_products, delete_product, insert_new_product

app = Flask(__name__)

connection = get_sql_connection()


@app.get("/get-product")
def get_all_product():
    products = get_all_products(connection)
    response = jsonify(products)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.post("/delete/product")
def delete_product_():
    product_id = request.json
    product_id = product_id['product_id']
    response = delete_product(connection, product_id=product_id)

    return response


@app.post("/add/product")
def add_product():
    request_body = request.json
    product_name = request_body['product_name']
    uom_id = request_body['uom_id']
    price_per_unit = request_body['price_per_unit']
    response = insert_new_product(connection, request_body)

    return response


if __name__ == "__main__":
    app.run(port=5000)
