import json

from flask import Flask, render_template, request
import RPi.GPIO as GPIO
import time

app = Flask(__name__)


class Shimeji():

    def __init__(self):
        self.is_blowing_mist = False
        self.is_open = False
        self.is_lighting_up = False
        self.initialize()

    def initialize(self):
        pass

    def to_json(self):
        json_dict = {
                "is_blowing_mist": self.is_blowing_mist,
                "is_open": self.is_open,
                "is_lighting_up": self.is_lighting_up
                }
        return json.dumps(json_dict)

    def blow_mist(self, sec):
        # TODO
        # blow mist during sec(sec), after passed sec time turn off light.
        # if sec = 0, No mist.
        pass

    def light_up(self, sec=0):
        # light up during sec(sec), after passed sec time turn off light.
        # if sec = 0, never turn off. please call light_down function.
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(11, GPIO.OUT)
        if sec<=0:
            GPIO.output(11, True)
            return
        else:
            GPIO.output(11, True)
            time.sleep(sec)
            GPIO.output(11, False)
            return

    def light_down(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(11, GPIO.OUT)
        GPIO.output(11, False)
        return

    def open(self):
        # TODO
        # open top
        pass

    def close(self):
        # TODO
        # close top
        pass

shimeji = Shimeji()

def shimeji_controller(action_type, param):
    if action_type == "light_up":
        shimeji.is_lighting_up(param["sec"])


@app.route('/action', methods=["GET", "POST"])
def action():
    if request.method == "GET":
        return shimeji.to_json()
    elif request.method == "POST":
        data = request.json
        return shimeji_controller(data["type"], data["param"])


@app.route('/')
def root():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
