# Inventory management system

### This is a prototype inventory management system.

## features
 - add products and warehouses
 - add/draw products to/from warehouses

## Run
    $ cp .env.example .env 

    $ docker compose up


## Usage

### products

#### create product
    url ap1/v1/products 
    method post
    body : 
        {"code":<product code>,
        "name":<product name>,
        "description":<product description>,
        "price":<price>}

#### list products 
    url ap1/v1/products 
    method get

#### show product
    url ap1/v1/products/<id>
    method get

#### update product
    url ap1/v1/products/<id>
    method patch


### Warehouses

#### create warehouse
    url ap1/v1/warehouses 
    method post
    body : 
        {   
            "name":<warehouse name>,
            "longtude" : <warehouse's location's longtude>,
            "latitude" : <warehouse's location's latitude>,
        }

#### list warehouses

    url ap1/v1/warehouses 
    method get

#### show warehouse

    url ap1/v1/warehouses/id 
    method get
        
#### update warehouse

    url ap1/v1/warehouses/id 
    method patch

#### list products in a warehouse
    url ap1/v1/warehouses/id/products
    method get

#### show product in a warehouse
    url ap1/v1/warehouses/warehouse_id/products/product_id
    method get

#### add product to a warehouse
    url ap1/v1/warehouses/id/products/add
    method post
    body : 
        {
            product : <product id>
            quantity : <quantity to add>
        }

#### draw from warehouse 
    url ap1/v1/warehouses/id/products/draw
    method post
    body :
        {
            product : <product id>
            quantity : <quantity to draw>
        }



    