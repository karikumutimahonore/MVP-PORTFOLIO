import mysql.connector


def get_all_products(connection):
    cursor = connection.cursor()

    query = ("select products.products_id, products.name, products.uom_id, products.price_per_unit, uom.uom_name from products inner join uom on products.uom_id = uom.uom_id")

    cursor.execute(query)

    responde = []

    for (products_id,name,uom_id,price_per_unit, uom_name) in cursor:
        responde.append(
            {
                'products_id': products_id,
                'name': name,
                'uom_id': uom_id,
                'price_per_unit': price_per_unit,
                'uom_name': uom_name
            }
        )

    return responde

if __name__ == '__main__':
    
    print(get_all_products(connection))