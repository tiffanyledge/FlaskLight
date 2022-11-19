from flask import Flask, render_template, request
from gpiozero import LED
from time import sleep

led = LED(17)
led_on = False
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/message', methods=['POST'])
def action():
    user_input = request.form['message']
    if user_input == "blink":
        led.on()
        sleep(1)
        led.off()
        sleep(1)
    elif user_input == "on":
        led.on()
    elif user_input == "off":
        led.off()
        sleep(1)
       
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
