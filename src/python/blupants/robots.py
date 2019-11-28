try:
    import robots_common
except:
    import blupants.robots_common as robots_common


class RobotFactory:

    def __init__(self):
        self._creators = {}

    def register_robot(self, platform, creator):
        self._creators[platform] = creator

    def get_robot(self, platform):
        creator = self._creators.get(platform)
        if not creator:
            return robots_common.RobotHollow("")
        return creator()


class Robot(robots_common.RobotHollow):
    def __init__(self, platform):
        self._robot = factory.get_robot(platform)

    def claw_toggle(self):
        return self._robot.claw_toggle()

    def claw_open(self):
        return self._robot.claw_open()

    def claw_close(self):
        return self._robot.claw_close()

    def read_distance(self):
        return self._robot.read_distance()

    def move_forward(self, blocks=1, speed=0.5):
        return self._robot.move_forward(blocks, speed)

    def move_backwards(self, blocks=1, speed=0.5):
        return self._robot.move_backwards(blocks, speed)

    def turn_right(self, angle=90):
        return self._robot.turn_right(angle)

    def turn_left(self, angle=90):
        return self._robot.turn_left(angle)

    def sleep(self, seconds=1.0):
        return self._robot.sleep(seconds)

    def shutdown(self, quiet=False):
        return self._robot.shutdown(quiet)

    def set_servo(self, i=1, angle=0.0):
        return self._robot.set_servo(i, angle)

    def set_motor(self, i=1, duty=0.5):
        return self._robot.set_motor(i, duty)

    def move(self, period=1, duty=1):
        return self._robot.move(period, duty)

    def camera_toggle(self):
        return self._robot.camera_toggle()

    def look_angle(self, angle=90):
        return self._robot.look_angle(angle)

    def say_yes(self):
        return self._robot.say_yes()

    def say_no(self):
        return self._robot.say_no()


global factory
factory = RobotFactory()

try:
    import beagleboneblue
except:
    try:
        import blupants.beagleboneblue as beagleboneblue
    except:
        pass
try:
    factory.register_robot("generic", beagleboneblue.BeagleBoneBlue)
except:
    pass
try:
    factory.register_robot("blupants_car", beagleboneblue.BluPantsCar)
except:
    pass
try:
    factory.register_robot("edumip", beagleboneblue.EduMIP)
except:
    pass

try:
    import ev3
except:
    try:
        import blupants.ev3
    except:
        pass
try:
    factory.register_robot("generic", ev3.ev3)
except:
    pass
try:
    factory.register_robot("smart_brick", ev3.smart_brick)
except:
    pass