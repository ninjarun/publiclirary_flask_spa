import json
from flask_cors import CORS
from flask import Blueprint, Flask, render_template, request
from publiclibrary import db
from publiclibrary.core.util import del_func
from publiclibrary.customers.models import Customers

customers= Blueprint('customers',__name__,template_folder="templates") 
CORS(customers)

##############################################################################
##################### start of customer functions ###########################
##############################################################################
@customers.route("/addcustomer/", methods=['POST','GET'])
def add_customer():
    #add customer to database
    if request.method=='POST':
        new_customer=request.json
        newCustomer=Customers(new_customer['nm'],new_customer['ct'],new_customer['age'])
        db.session.add(newCustomer)
        db.session.commit()
    return 'success'
        # return render_template('addcustomer.html', msg="Customer Added Succsefully!")
    # return render_template('addcustomer.html')

@customers.route("/findcustomer/", methods=['POST'])
@customers.route("/findcustomer/<ind>", methods=['DELETE'])
def find_customer(ind=-1):
    #find customer by name - also customers can be removed once found
    msg=del_func(int(ind), Customers,"Customer") if int(ind)>0 else ["None","None"]
    list=[{"id":cust.id,"name":cust.name,"age":cust.age,"city":cust.city} for cust in db.session.query(Customers).filter_by(name=request.json['nm']) if request.method=="POST"]
    return list

@customers.route("/displayall/", methods=['GET'])
@customers.route("/displayall/<ind>", methods=['DELETE'])
def display_all(ind=-1):
    #display all customers - customers can also be removed with this function
    x=del_func(int(ind), Customers,"Customer") if int(ind)>0 else ["None","None"]
    list=[]
    for cust in Customers.query.all():
        list.append({"id":cust.id,"name":cust.name,"age":cust.age,"city":cust.city})
    print(list)
    return list
##############################################################################
######################### end of customer functions ##########################
##############################################################################