from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_library.sqlite3'
app.config['SECRET_KEY'] = "random_string"

db = SQLAlchemy(app)


from publiclibrary.core.views import core
from publiclibrary.customers.views import customers
from publiclibrary.books.views import books
from publiclibrary.loans.views import loans

app.register_blueprint(core)
app.register_blueprint(customers)
app.register_blueprint(books)
app.register_blueprint(loans)








# from flask import Flask
# from flask_cors import CORS
# from flask_sqlalchemy import SQLAlchemy
# from flask_session import Session
# from flask_login import (
#     LoginManager,
#     UserMixin,
#     current_user,
#     login_required,
#     login_user,
#     logout_user,
# )
# from flask_wtf.csrf import CSRFProtect, generate_csrf


# app = Flask(__name__)
# app.config['DEBUG']=True,
# app.config['SECRET_KEY']="secret_sauce",
# app.config['SESSION_COOKIE_HTTPONLY']=True,
# app.config['REMEMBER_COOKIE_HTTPONLY']=True,
# app.config['SESSION_COOKIE_SAMESITE']="Lax"


# # login_manager = LoginManager()

# # login_manager.init_app(app)

# # login_manager.session_protection = "strong"

# # csrf = CSRFProtect(app)

# CORS(app, supports_credentials=True)
# #     resources={r"*": {"origins": "http://localhost:52330"}},
# #     expose_headers=["Content-Type", "X-CSRFToken"],
# #     supports_credentials=True)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_library.sqlite3'
# # app.secret_key = 'supersecretkey'
# # app.config['SESSION_TYPE'] = 'filesystem'
# db = SQLAlchemy(app)

# from publiclibrary.books.views import books
# from publiclibrary.core.views import core
# from publiclibrary.customers.views import customers
# from publiclibrary.loans.views import loans

# app.register_blueprint(core)
# app.register_blueprint(customers)
# app.register_blueprint(books)
# app.register_blueprint(loans)

