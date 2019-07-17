import pigpio

PWM = 0
INPUT1 = 1
INPUT2 = 2

class Motor():
    def __init__(self, port, rev = False):
        self.pi = pigpio.pi()
        self.port = port
        self.rev = rev
        self.duty = 0

        self.pi.write(self.port[INPUT1], 0)
        self.pi.write(self.port[INPUT2], 0)

    def setOutput(self, out):
        self.pi.write(self.port[INPUT1], out[0])
        self.pi.write(self.port[INPUT2], out[1])

    def setSpeed(self, d):
        self.duty = d

        if (d >= 0 and not self.rev) or (d < 0 and self.rev):
            self.setOutput([1, 0])
        else:
            self.setOutput([0, 1])

        self.pi.set_PWM_dutycycle(self.port[PWM], self.duty)

    def stop(self):
        self.pi.stop()

if __name__ == '__main__':
    pwm = input('PWM pin: ')
    in1 = input('Input 1: ')
    in2 = input('Input 2: ')

    motor = Motor(port = [pwm, in1, in2])
    