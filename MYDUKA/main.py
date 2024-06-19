from flask import Flask,render_template
from dbservice import get_data,sales_product

#create the flask instance
app = Flask(__name__)

#first route 
@app.route('/')
def home():
    return render_template('home.html')



@app.route("/products")
def products():
    prods=get_data("products")
    return render_template("products.html",product=prods)


@app.route("/sales")
def sales():
    sal=get_data("sales")
    prod=get_data("products")
    return render_template("sales.html",sales=sal,products=prod)

@app.route("/dashboard")
def dashboard():
    sale_p=sales_product()
    p_name=[]
    p_sales=[]

    for i in sale_p:
        p_name.append(i[0])
        p_sales.append(float(i[1]))
    
    return render_template("dashboard.html",p_name=p_name,p_sales=p_sales)



  


# create 3 html files an ensure all are boot strap enabled
# create products,sales,dashboard
# render the html files
# create dashboard

app.run(debug=True)