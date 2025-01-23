from time import sleep


class TrafficLights:
    def __init__(self, red, yellow, green):
        self.red = red
        self.yellow = yellow
        self.green = green

    def red_light(self):
        print(f"{self.red} light")
        sleep(5)

    def yellow_light(self):
        print(f"{self.yellow} light")
        sleep(2)

    def green_light(self):
        print(f"{self.green} light")
        sleep(7)

traffic = TrafficLights(red = "Red", yellow = "Yellow", green = "Green")

traffic.green_light()
traffic.yellow_light()
traffic.red_light()
traffic.yellow_light()
traffic.green_light()