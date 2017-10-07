from flask import Flask, request


app = Flask(__name__)
app.config['DEBUG'] = True

form="""
<!doctype html>
<html>
    <body>
        <form action="/" method="post">
            <label for="username">Username:</label>
            <input type="text" name="username">
            
            <label for="password">Password:</label>
            <input type="text" name="password">


            <label for="verify_password">Verify Password:</label>
            <input type="text" name="verify_password">


            <label for="email">Email(optional):</label>
            <input type="text" name="email">
            <input type="submit">
        </form>
    </body>
</html>
"""
@app.route("/")

def index():

   return form



@app.route("/", methods=['POST'])
def hello():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']

app.run()