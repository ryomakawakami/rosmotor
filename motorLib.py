import pigpio

PWM = 0
INPUT1 = 1
INPUT2 = 2

class Motor():
    # Initialization
    def __init__(self, port, rev = False):
        self.pi = pigpio.pi()
        self.port = port
        self.rev = rev
        self.duty = 0

        self.pi.write(self.port[INPUT1], 0)
        self.pi.write(self.port[INPUT2], 0)

    # Stop
    def stop(self):
        self.pi.stop()

    # Set input 1 and 2
    def setOutput(self, out):
        self.pi.write(self.port[INPUT1], out[0])
        self.pi.write(self.port[INPUT2], out[1])

    # Set RPM
    def setRPM(self, r):
        self.rpm = r
        self.duty = self.rpm2Duty(self.rpm)
        self.setDuty(self.duty)
        return abs(self.duty)

    # Set duty
    def setDuty(self, d):
        # Determine direction
        if (d >= 0 and not self.rev) or (d < 0 and self.rev):
            self.setOutput([1, 0])
        else:
            self.setOutput([0, 1])
            d *= -1
        # Set PWM
        self.pi.set_PWM_dutycycle(self.port[PWM], d)

    # Convert RPM to duty
    def rpm2Duty(self, rpm):
        duty = rpm * 2.55 / 2.38
        if abs(duty) > 100:
            if duty > 0: duty = 100
            else: duty = -100
        return duty

if __name__ == '__main__':
    pwm = input('PWM pin: ')
    in1 = input('Input 1: ')
    in2 = input('Input 2: ')

    motor = Motor(port = [pwm, in1, in2])
    
