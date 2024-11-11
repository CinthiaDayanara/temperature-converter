from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    celsius = request.form.get('celsius')
    if celsius:
        try:
            celsius = float(celsius)
            fahrenheit = (celsius * 9/5) + 32
            return render_template('index.html', result=f"{fahrenheit} °F")
        except ValueError:
            return render_template('index.html', result="Por favor, ingresa un número válido.")
    return render_template('index.html', result="Por favor, ingresa un valor.")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
