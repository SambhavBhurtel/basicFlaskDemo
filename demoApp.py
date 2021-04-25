from flask import Flask
from flask import render_template_string,request

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template_string('''
    <h1>Hello There!</h1>
    <form action="/response/" method="get">
    <label for="FirstName">Enter Your Name: </label>
    <br><input name="FirstName" type="text"><br>
    <input type="submit" value="Submit">
    </form>
    ''')

@app.route('/response/',methods=['GET'])
def hello_name():
    arguments = request.args
    first_name = arguments.get("FirstName")
    res = f'''
    <h1>Hello {first_name}!</h1>
    '''
    return render_template_string(res)

if __name__=="__main__":
    app.run(host='0.0.0.0')
