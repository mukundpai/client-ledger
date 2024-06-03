from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin
from flask_sqlalchemy import SQLAlchemy
from uuid import uuid4
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'd6d1877895e1ef9f78f3d8a77d5e6894'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new_db.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

class Employee(UserMixin, db.Model):
    emp_id = db.Column(db.String, primary_key=True, default=lambda: str(uuid4()))
    emp_name = db.Column(db.String, nullable=False)
    emp_designation = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    
    def set_password(self, password):
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def get_id(self):
        return self.emp_id

class Service(db.Model):
    service_id = db.Column(db.String, primary_key=True, default=lambda: str(uuid4()))
    service_title = db.Column(db.String, nullable=False)
    client_id = db.Column(db.String, db.ForeignKey('client.client_id'), nullable=False)
    category_id = db.Column(db.String, db.ForeignKey('category.category_id'), nullable=False)
    service_type_id = db.Column(db.String, db.ForeignKey('service_type.service_type_id'), nullable=False)
    created_by = db.Column(db.String, db.ForeignKey('employee.emp_id'), nullable=False)
    end_date = db.Column(db.Date)
    create_date = db.Column(db.Date)
    employees = db.relationship('Employee', secondary='service_associate', backref='services')

    def to_dict(self):
        return {
            'service_id': self.service_id,
            'service_title': self.service_title,
            'client_id': self.client_id,
            'category_id': self.category_id,
            'service_type_id': self.service_type_id,
            'created_by': self.created_by,
            'end_date': self.end_date,
            'create_date': self.create_date
        }

class Task(db.Model):
    task_id = db.Column(db.String, primary_key=True, default=lambda: str(uuid4()))
    task_name = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    service_id = db.Column(db.String, db.ForeignKey('service.service_id'), nullable=False)
    due_date = db.Column(db.Date)
    is_private = db.Column(db.Boolean, default=False)

class Subtask(db.Model):
    subtask_id = db.Column(db.String, primary_key=True, default=lambda: str(uuid4()))
    subtask_name = db.Column(db.String, nullable=False)
    task_id = db.Column(db.String, db.ForeignKey('task.task_id'), nullable=False)
    comment_text = db.Column(db.String)
    created_by = db.Column(db.String, db.ForeignKey('employee.emp_id'), nullable=False)
    create_date = db.Column(db.Date)

class Client(db.Model):
    client_id = db.Column(db.String, primary_key=True, default=lambda: str(uuid4()))
    client_name = db.Column(db.String, nullable=False)

class Category(db.Model):
    category_id = db.Column(db.String, primary_key=True, default=lambda: str(uuid4()))
    category_name = db.Column(db.String, nullable=False)

class ServiceType(db.Model):
    service_type_id = db.Column(db.String, primary_key=True, default=lambda: str(uuid4()))
    service_type_name = db.Column(db.String, nullable=False)

class ServiceAssociate(db.Model):
    service_associate_id = db.Column(db.String, primary_key=True, default=lambda: str(uuid4()))
    service_id = db.Column(db.String, db.ForeignKey('service.service_id'), nullable=False)
    emp_id = db.Column(db.String, db.ForeignKey('employee.emp_id'), nullable=False)
    employee_name = db.Column(db.String, nullable=False)

class Comment(db.Model):
    comment_id = db.Column(db.String, primary_key=True, default=lambda: str(uuid4()))
    task_type = db.Column(db.String, nullable=False)
    task_id = db.Column(db.String, nullable=False)
    comment_text = db.Column(db.String, nullable=False)
    created_by = db.Column(db.String, db.ForeignKey('employee.emp_id'), nullable=False)

class Attachment(db.Model):
    attachment_id = db.Column(db.String, primary_key=True, default=lambda: str(uuid4()))
    service_id = db.Column(db.String, db.ForeignKey('service.service_id'), nullable=False)
    attached_by = db.Column(db.String, db.ForeignKey('employee.emp_id'), nullable=False)

@login_manager.user_loader
def load_user(emp_id):
    return Employee.query.get(emp_id)