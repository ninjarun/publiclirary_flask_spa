from flask import render_template, Blueprint, request
from publiclibrary.core.util import dummy
core= Blueprint('core',__name__,template_folder="templates")

@core.route("/", methods=['POST','GET'])
def index():
    """starting view"""
    if request.method=='POST':
        dummy()
        return 'succes'
    return 'welcome'
    



# from flask import render_template, Blueprint, request, session, redirect,url_for
# from publiclibrary.core.util import dummy
# core= Blueprint('core',__name__,template_folder="templates")
# from publiclibrary.core.model import User
# from publiclibrary import db,app



# @core.route("/", methods=['POST','GET'])
# def index():
#     # #starting view - post method is to insert the fake data 
#     # if session.get('logged_in') and session.get('user')=='admin':
#     #     print('here')
#     #     return 'admin'
#     # elif session.get('logged_in') and session.get('user')== 'regular':
#     #     return 'exists'
#     print(session.get('logged_in'))
#     if request.method=='POST':
#         new_user=request.json
#         print(new_user)
#         if new_user['action']=="addusr":
#             # print('here')
#             newUser=User(username=new_user['user'], password=new_user['password'])
#             db.session.add(newUser)
#             db.session.commit()
#             return 'useradded'
#         elif new_user['action']=="check":
#             if db.session.query(User).filter_by(username=new_user['user']).first().username == new_user['user'] and db.session.query(User).filter_by(username=new_user['user']).first().password == new_user['password']:
#                 print('here')
#                 session['logged_in'] = True
#                 session.modified=True
#                 print(session['logged_in'])
#                 print(session.get('logged_in'))
#                 session['user']='admin' if new_user['user']=='admin' else 'regular'
#                 # return redirect(url_for('core.index'))

#                 return  'admin' if new_user['user']=='admin' else 'exists'
#             else:
#                 return 'doesnt'
#     return 'test'
#             # if new_user['nm']
#         # dummy()
#     # return render_template('layout.html')

