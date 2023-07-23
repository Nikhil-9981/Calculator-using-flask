from flask import Flask,render_template , request , jsonify


app = Flask(__name__)


@app.route("/", methods = ['GET' , 'POST'])
def home_page():
    return render_template("index.html")

 

@app.route('/postman_data' , methods = ['POST'])
def math_operation():
    if (request.method == 'POST'):
        try :
            operator = request.json['operator']
            num1 = int(request.json['num1'])
            num2 = int(request.json['num2'])
            if operator == 'add':
                result = num1 + num2
            elif operator == 'subtract':
                result = num1 - num2
            elif operator == 'multiply':
                result = num1 * num2
            elif operator == 'divide':
               result = num1 / num2
            else:
               raise ValueError("Invalid operator")
        
            return jsonify(result)

        except Exception as e:
            return jsonify("Error is " + str(e))


@app.route("/math" , methods = ['GET' , 'POST'])
def math_operation1():
    if (request.method == 'POST'):
        try :
            operator = request.form['operator']
            num1 = int(request.form['num1'])
            num2 = int(request.form['num2'])
            if operator == 'add':
                result = num1 + num2
            elif operator == 'subtract':
                result = num1 - num2
            elif operator == 'multiply':
                result = num1 * num2
            elif operator == 'divide':
               result = num1 / num2
            else:
               raise ValueError("Invalid operator")
        
            return render_template('results.html' , result = result)

        except Exception as e:
            return render_template("Error is : " + str(e))


if __name__=="__main__":
    app.debug = True
    app.run(host="0.0.0.0")




















