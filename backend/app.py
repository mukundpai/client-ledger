from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, current_user, logout_user, login_required
from models import app, db, bcrypt, Employee, Task, Service, load_user
from flask import render_template, redirect, url_for
from flask_migrate import Migrate




@app.route('/api/hello')
def hello():
    return jsonify(message='Hello from Flask!')


login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(emp_id):
    return Employee.query.get(emp_id)

@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    employee = Employee(
        emp_name=data['emp_name'],
        emp_designation=data['emp_designation'],
        email=data['email']
    )
    employee.set_password(data['password'])
    db.session.add(employee)
    db.session.commit()
    return jsonify(message="User registered successfully"), 201

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    employee = Employee.query.filter_by(email=data['email']).first()
    if employee and employee.check_password(data['password']):
        login_user(employee)
        return jsonify(message="Login successful"), 200
    return jsonify(message="Invalid credentials"), 401

@app.route('/api/services', methods=['POST'])
@login_required
def create_service():
    data = request.get_json()
    service = Service(
        service_title=data['service_title'],
        client_id=data['client_id'],
        category_id=data['category_id'],
        service_type_id=data['service_type_id'],
        created_by=current_user.emp_id,
        end_date=data.get('end_date'),
        create_date=data.get('create_date')
    )
    db.session.add(service)
    db.session.commit()
    return jsonify(message='Service created successfully'), 201

@app.route('/api/tasks', methods=['POST'])
@login_required
def create_task():
    data = request.get_json()
    service_id = data.get('service_id')
    service = Service.query.get(service_id)
    if not service:
        return jsonify(message='Service not found'), 404
    task = Task(
        task_name=data['task_name'],
        description=data.get('description', ''),
        service_id=service_id,
        due_date=data.get('due_date'),
        is_private=data.get('is_private', False)
    )
    db.session.add(task)
    db.session.commit()
    return jsonify(message='Task created successfully'), 201

@app.route('/api/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify(message="Logged out successfully"), 200

@app.route('/home')
@login_required
def home():
    return render_template('home.html', user_name=current_user.emp_name)


@app.route('/api/services', methods=['GET'])
@login_required
def get_services():
    services = Service.query.filter_by(created_by=current_user.emp_id).all()
    return jsonify([service.to_dict() for service in services]), 200

@app.route('/api/services/<service_id>', methods=['PUT'])
@login_required
def update_service(service_id):
    data = request.get_json()
    service = Service.query.get(service_id)
    if not service:
        return jsonify(message="Service not found"), 404

    service.service_title = data.get('service_title', service.service_title)
    service.client_id = data.get('client_id', service.client_id)
    service.category_id = data.get('category_id', service.category_id)
    service.service_type_id = data.get('service_type_id', service.service_type_id)
    
    db.session.commit()
    return jsonify(message="Service updated successfully"), 200

@app.route('/api/services/<service_id>/tasks', methods=['POST'])
@login_required
def add_task_to_service(service_id):
    data = request.get_json()
    service = Service.query.get(service_id)
    if not service:
        return jsonify(message="Service not found"), 404
    
    task = Task(
        task_name=data['task_name'],
        description=data.get('description', ''),
        service_id=service_id,
        due_date=data.get('due_date'),
        is_private=data.get('is_private', False)
    )
    db.session.add(task)
    db.session.commit()
    return jsonify(message="Task added to service successfully"), 201






migrate = Migrate(app, db)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
