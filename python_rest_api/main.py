from app import app
from config import mysql
from flask import jsonify
from flask import flash, request
import pymysql

"""

status code 

200 - PROPER STATUS CODE
400 - BAD REQUEST
401 - UNAUTHORIZED
404 - NOT FOUND

"""
        
@app.route('/employee_details')
def employee_details():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT id, name, email, phone, address FROM employee_details")
        empRows = cursor.fetchall()
        respone = jsonify(empRows)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    cursor.close() 
    conn.close()
        
@app.route('/employee_details/<int:id>')
def individual_employee_details(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT id, name, email, phone, address FROM employee_details WHERE id =%s", id)
        empRow = cursor.fetchone()
        respone = jsonify(empRow)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    cursor.close()
    conn.close()

@app.route('/add_employee_details', methods=['POST'])
def add_employee_details():
    try:
        _json = request.json
        _name = _json['name']
        _email = _json['email']
        _phone = _json['phone']
        _address = _json['address']        
        if _name and _email and _phone and _address and request.method == 'POST':            
            sqlQuery = "INSERT INTO employee_details(name, email, phone, address) VALUES(%s, %s, %s, %s, %s)"
            bindData = (_name, _email, _phone, _address)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            respone = jsonify('Employee added successfully!')
            respone.status_code = 200
            return respone
        else:
            return not_found()
    except Exception as e:
        print(e)
    cursor.close() 
    conn.close()

@app.route('/update_employee_details', methods=['PUT'])
def update_employee_details():
    try:
        _json = request.json
        _id = _json['id']
        _name = _json['name']
        _email = _json['email']
        _phone = _json['phone']
        _address = _json['address']
        if _name and _email and _phone and _address and _id and request.method == 'PUT':            
            sqlQuery = "UPDATE employee_details SET name=%s, email=%s, phone=%s, address=%s WHERE id=%s"
            bindData = (_name, _email, _phone, _address, _id,)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            respone = jsonify('Employee updated successfully!')
            respone.status_code = 200
            return respone
        else:
            return not_found()    
    except Exception as e:
        print(e)
    cursor.close() 
    conn.close()

@app.route('/delete_employee_details/<int:id>', methods=['DELETE'])
def delete_employee_details(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM employee_details WHERE id =%s", (id,))
        conn.commit()
        respone = jsonify('Employee deleted successfully!')
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    cursor.close() 
    conn.close()
        
@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url,
    }
    respone = jsonify(message)
    respone.status_code = 404
    return respone

#code starts here        
app.run()