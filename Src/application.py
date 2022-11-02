from flask import Flask
app = Flask(__name__)

@app.route('/hello/<name>')
def hello_name(name):
   return('Hello %s!' % name)

if __name__ == '__main__':
   app.run(host='13.250.9.177', port=8000)
