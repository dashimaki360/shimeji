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
        GPIO.setmode(GPIO.BCM)

        #GPIO4を制御パルスの出力に設定
        self.gp_servo_out = 4
        self.gp_mist_out = 15
       
        GPIO.setup(self.gp_servo_out, GPIO.OUT)
        GPIO.setup(self.gp_mist_out, GPIO.OUT)
        
        #「GPIO4出力」でPWMインスタンスを作成する。
        #GPIO.PWM( [ピン番号] , [周波数Hz] )
        #SG92RはPWMサイクル:20ms(=50Hz), 制御パルス:0.5ms〜2.4ms, (=2.5%〜12%)。
        self.servo = GPIO.PWM(self.gp_servo_out, 50)
        
        #パルス出力開始。　servo.start( [デューティサイクル 0~100%] )
        #とりあえずゼロ指定だとサイクルが生まれないので特に動かないっぽい？
        #servo.start(0)
        
        GPIO.output(self.gp_mist_out, GPIO.LOW)

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
        GPIO.output(self.gp_mist_out, GPIO.HIGH)
        time.sleep(sec)
        GPIO.output(self.gp_mist_out, GPIO.LOW)
        

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
    print("get request")
    if request.method == "GET":
        return shimeji.to_json()
    elif request.method == "POST":
        print("post req")
        data = request.json
        shimeji.blow_mist(4)
        return "thank you"
        # return shimeji_controller(data["type"], data["param"])


@app.route('/')
def root():
    print("hoge")
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0')
