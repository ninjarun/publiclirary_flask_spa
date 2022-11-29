
from flask import Blueprint, Flask, render_template, request
from publiclibrary import db
from publiclibrary.books.models import Books
from publiclibrary.core.util import del_func

books= Blueprint('books',__name__,template_folder="templates")

##############################################################################
########################## start of book functions ###########################
##############################################################################
@books.route("/addbook/", methods=['POST','GET'])
def add_book():
    #add book function
    if request.method=='POST':
            new_book=request.json
            newBook=Books(new_book['nm'], new_book['auth'], new_book['year'], new_book['type'])
            db.session.add(newBook)
            db.session.commit()
    return ['success']

@books.route("/findbook/", methods=['POST','GET'])
@books.route("/findbook/<ind>", methods=['DELETE','GET'])
def find_book(ind=-1):
    #find book by name - also can remove books once found
    msg=del_func(int(ind), Books,"Book") if int(ind)>0 else ["None","None"]
    list=[{"id":book.id,"name":book.name,"author":book.author,"year":book.year_published,"type":book.type} for book in db.session.query(Books).filter_by(name=request.json['nm']) if request.method=="POST"]
    return list
   
   
   
   
   
#    books=db.session.query(Books).filter_by(name=request.form.get('nm')).all() if request.method=="POST" else []
#     flag=True if len(books)>0 else False
#     render_info=del_func(ind,Books,"Book") if int(ind)>0 else ["None","None"]
#     return render_template('findbook.html', allbooks=Books.query.all(), books=books,flag=flag,msg=render_info[1],color=render_info[0])    

@books.route("/displayallbooks/", methods=['GET'])
@books.route("/displayallbooks/<ind>", methods=['DELETE','GET'])
def display_all_books(ind=-1):
    #displays all books in data base - books can also be removed with this function
    x=del_func(int(ind), Books,"book") if int(ind)>0 else ["None","None"]
    list=[]
    for book in Books.query.all():
        list.append({"id":book.id,"name":book.name,"author":book.author,"year":book.year_published,"type":book.type})
    return list




#    render_info=del_func(ind, Books,"Book") if int(ind)>0 else ["None","None"]
#     return render_template('displayallbooks.html',books=Books.query.all(),msg=render_info[1],color=render_info[0])
############################################################################
########################## end of book functions#########################
############################################################################
