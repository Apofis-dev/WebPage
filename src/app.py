from flask import Flask , request , redirect, render_template , abort , url_for

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('home'))

@app.route('/home', methods=['GET','POST'])
def home():
    
    if request.remote_addr != '127.0.0.1':
        abort(403) 
    else:
        return render_template('index.html')

if __name__ =='__main__':
    
    app.run( debug=True , port = 5005 )