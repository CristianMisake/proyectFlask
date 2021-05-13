from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculadora', methods =["GET", "POST"])
def calculadora():
    resp = ""
    numero1 = ""
    numero2 = ""
    operation = 1
    if request.method == "POST":
        numero1 = int(request.form.get("numero1"))
        numero2 = int(request.form.get("numero2"))
        operation = int(request.form.get("operation"))
        # Suma
        if operation == 1:
            resp = "Su resultado es:"+str(numero1 + numero2)
        # Resta
        elif operation == 2:
            resp = "Su resultado es:"+str(numero1 - numero2)
        # Multiplicación
        elif operation == 3:
            resp = "Su resultado es:"+str(numero1 * numero2)
        # Division
        elif operation == 4:
            resp = "Su resultado es:"+str(numero1 / numero2)
    return render_template("calculadora.html", resp=resp, numero1=numero1, numero2=numero2, operation=operation)

if __name__=='__main__':
   app.run()