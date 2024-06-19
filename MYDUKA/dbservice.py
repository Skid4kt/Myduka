import psycopg2


conn=psycopg2.connect(
    dbname="myduka",
    user="postgres",
    host="localhost",
    password="armelNN23",
    port=5432


)

cur=conn.cursor()
#fetch products
#def get_products():
 #   query="select * from products"
  #  cur.execute(query)
   # products=cur.fetchall()
    #print(products)

#get_products()

#fetch sales
#def get_sales():
 #   query="select * from sales"
  #  cur.execute(query)
   # sales=cur.fetchall()
    #print(sales)

#get_sales()    

#def get_data(a,b):
 #   query="select * from a and b"
  #  cur.execute(query)
   # data=cur.fetchall()
    #print(data)

def get_data(table):
    query=f"select * from {table}"
    cur.execute(query)
    data=cur.fetchall()
    return data

# get_data("sales")

# #insert
# def insert_products():
#     query = "insert into products(id,name,buying_price,selling_price,stock_quantity)values(100,'ginger',100,200,10)"
#     cur.execute(query)
#     conn.commit()

# # insert_products()
# get_data("products")

# # make sale
# def insert_sales():
#     query = "insert into sales(id,pid,quantity,created_at)values(4,10,now())"
#     cur.execute(query)
#     conn.commit()



# 1
# def calc_sales_day():
#     query = "SELECT DATE(s.created_at) AS sale_date/
#     Sum(s.quantity * p.selling_price) AS total_sales"



def sales_product():
    query = "SELECT name,SUM(p.selling_price * s.quantity)\
        As totsales FROM sales as s JOIN products as p ON s.id = p.id\
            GROUP BY p.name;"
    cur.execute(query)
    data= cur.fetchall()
    
    return data




def profit():
    query = "SELECT p.name, SUM((p.selling_price - p.buying_price)\
        * s.quantity) AS profit FROM sales as s JOIN products as p ON s.product_id = p.id GROUP BY p.name"
    cur.execute(query)
    data= cur.fetchall()
    return data