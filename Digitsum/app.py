from flask import Flask, render_template, request
app = Flask(__name__)
list=[]
@app.route("/")
@app.route("/home")
@app.route("/index")

def home():
    list.clear()
    return render_template("index.html")

@app.route("/result",methods=['POST','GET'])

def result():
    if (request.form['btn'] == '1'):
        list.append(1)
        return render_template("index.html",list=list[0:])
    if (request.form['btn'] == '2'):
        list.append(2)
        return render_template("index.html",list=list[0:])
    if (request.form['btn'] == '3'):
        list.append(3)
        return render_template("index.html",list=list[0:])
    if (request.form['btn'] == '4'):
        list.append(4)
        return render_template("index.html",list=list[0:])
    if (request.form['btn'] == '5'):
        list.append(5)
        return render_template("index.html",list=list[0:])
    if (request.form['btn'] == '6'):
        list.append(6)
        return render_template("index.html",list=list[0:])
    if (request.form['btn'] == '7'):
        list.append(7)
        return render_template("index.html",list=list[0:])
    if (request.form['btn'] == '8'):
        list.append(8)
        return render_template("index.html",list=list[0:])
    if (request.form['btn'] == '9'):
        list.append(9)
        return render_template("index.html",list=list[0:])
    if (request.form['btn'] == '0'):
        list.append(0)
        return render_template("index.html",list=list[0:])
    
    if (request.form['btn'] == 'ENTER'):
        sum = 0
        for i in range(0,len(list)):

            sum = sum + list[i] 
    return render_template("index.html",sum=sum)
    
if __name__ == '__main__':
    app.run(debug=True, port=4000)