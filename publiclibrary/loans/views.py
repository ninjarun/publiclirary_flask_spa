import datetime
from flask import Flask, render_template, request, Blueprint
from publiclibrary.loans.models import Loans
from publiclibrary.books.models import Books
from publiclibrary.customers.models import Customers
from publiclibrary.core.util import del_func
from publiclibrary import db

loans= Blueprint('loans',__name__,template_folder="templates")

##########################################################################
############################ start of loan functions #####################
##########################################################################א
@loans.route("/newloan/", methods=['POST','GET'])
def new_loan():
    #add a new loan to database
    # msg="None"
    if request.method=='GET':
        bboks=[{"id":book.id,"name":book.name,"author":book.author,"year":book.year_published,"type":book.type} for book in db.session.query(Books)]
        custs=[]
        for cust in Customers.query.all():
            custs.append({"id":cust.id,"name":cust.name,"age":cust.age,"city":cust.city})
        full_list={"books":bboks,"customers":custs}
        return full_list



    if request.method=='POST':
        current_book=db.session.query(Books).filter_by(id=int(request.json['book'])).first()
        if db.session.query(Loans).filter_by(book_id=current_book.id).first():
            msg="Book is Lent, Not Available"
        else:
            if current_book.type==1:
                return_date=datetime.date.today()+datetime.timedelta(days=10)
            elif current_book.type==2:
                return_date=datetime.date.today()+datetime.timedelta(days=5)
            else:
                return_date=datetime.date.today()+datetime.timedelta(days=2)
            newLoan=Loans(request.json["customer"], request.json["book"],datetime.date.today(),return_date )
            db.session.add(newLoan)
            db.session.commit()
            msg="Loan Approved"
        return 'success'
    # return render_template('newloan.html',books=Books.query.all(),customers=Customers.query.all(),msg=msg)

@loans.route("/lateloans/", methods=['GET'])
@loans.route("/lateloans/<ind>", methods=['DELETE','GET'])
def late_loans(ind=-1):
    #displays all the late loans - books can be return with this function
    list=[]
    for loan in Loans.query.all():
        if str(datetime.date.today()) > loan.return_date:
            list.append({"id":loan.id,"customer":loan.Customers.name,"book":loan.Books.name, "loandate":loan.loan_date,"returndate":loan.return_date})

    print(list)
    return list       

    # render_info=del_func(ind, Loans,"Loan") if int(ind)>0 else ["None","None"]
    # return render_template('lateloans.html', lateloans=Loans.query.all(), today=str(datetime.date.today()),msg=render_info[1],color=render_info[0])

@loans.route("/displayallloans/", methods=['GET'])
@loans.route("/displayallloans/<ind>", methods=['DELETE'])
def display_all_loans(ind=-1):
    #displays all loans - books can be returned with this function
    if request.method=="GET":
        list=[]
        for loan in Loans.query.all():
            # print(loan.Customers.name)
            list.append({"id":loan.id,"customer":loan.Customers.name,"book":loan.Books.name, "loandate":loan.loan_date,"returndate":loan.return_date})
        return list
    render_info=del_func(ind, Loans,"Loan") if int(ind)>0 else ["None","None"]

    print(render_info)
    return 'succes'
    # render_info=del_func(ind, Loans,"Loan") if int(ind)>0 else ["None","None"]
    # return render_template    ('displayallloans.html',loans=Loans.query.all(), today=str(datetime.date.today()),msg=render_info[1],color=render_info[0])

############################################################################
####################### end of loan functions ###############################
############################################################################
