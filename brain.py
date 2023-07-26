import RPi.GPIO as GPIO
import pygame

class Car:
    def __init__(self, pin1, pin2, pin3, pin4, pin5, pin6, pin7, pin8,led_pin1,led_pin2):
        self.pin1 = pin1  # front right motor forward
        self.pin2 = pin2  # front right motor backward
        self.pin3 = pin3  # front left motor backward
        self.pin4 = pin4  # front left motor forward
        self.pin5 = pin5  # back left motor forward
        self.pin6 = pin6  # back right motor forward
        self.pin7 = pin7  # back right motor backward
        self.pin8 = pin8  # back left motor backward
        self.led1 = led_pin1 # 35 red
        self.led2 = led_pin2 # 31 green

        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        #led
        GPIO.setup(self.led1, GPIO.OUT)
        GPIO.setup(self.led2, GPIO.OUT)

        # front
        GPIO.setup(self.pin1, GPIO.OUT)  # 11 front
        GPIO.setup(self.pin2, GPIO.OUT)  # 13 back

        GPIO.setup(self.pin3, GPIO.OUT)  # 15 back
        GPIO.setup(self.pin4, GPIO.OUT)  # 37 front

        # back
        GPIO.setup(self.pin5, GPIO.OUT)  # 36 front

        GPIO.setup(self.pin6, GPIO.OUT)  # 16 front
        GPIO.setup(self.pin7, GPIO.OUT)  # 18 back

        GPIO.setup(self.pin8, GPIO.OUT)  # 22 back

        print('Initialization done')

    def forward(self):
        GPIO.output(self.pin1, GPIO.HIGH)
        GPIO.output(self.pin4, GPIO.HIGH)
        GPIO.output(self.pin5, GPIO.HIGH)
        GPIO.output(self.pin6, GPIO.HIGH)

        GPIO.output(self.pin2, GPIO.LOW)
        GPIO.output(self.pin3, GPIO.LOW)
        GPIO.output(self.pin7, GPIO.LOW)
        GPIO.output(self.pin8, GPIO.LOW)

        GPIO.output(self.led2, GPIO.HIGH)
        GPIO.output(self.led1, GPIO.LOW)

    def backward(self):
        GPIO.output(self.pin3, GPIO.HIGH)
        GPIO.output(self.pin2, GPIO.HIGH)
        GPIO.output(self.pin7, GPIO.HIGH)
        GPIO.output(self.pin8, GPIO.HIGH)

        GPIO.output(self.pin1, GPIO.LOW)
        GPIO.output(self.pin4, GPIO.LOW)
        GPIO.output(self.pin5, GPIO.LOW)
        GPIO.output(self.pin6, GPIO.LOW)

        GPIO.output(self.led2, GPIO.LOW)
        GPIO.output(self.led1, GPIO.HIGH)

    def right(self):
        GPIO.output(self.pin1, GPIO.LOW)
        GPIO.output(self.pin2, GPIO.LOW)
        GPIO.output(self.pin6, GPIO.LOW)
        GPIO.output(self.pin7, GPIO.LOW)

        GPIO.output(self.pin3, GPIO.LOW)
        GPIO.output(self.pin4, GPIO.HIGH)
        GPIO.output(self.pin5, GPIO.HIGH)
        GPIO.output(self.pin8, GPIO.LOW)

    def left(self):
        GPIO.output(self.pin1, GPIO.HIGH)
        GPIO.output(self.pin2, GPIO.LOW)
        GPIO.output(self.pin6, GPIO.HIGH)
        GPIO.output(self.pin7, GPIO.LOW)

        GPIO.output(self.pin3, GPIO.LOW)
        GPIO.output(self.pin4, GPIO.LOW)
        GPIO.output(self.pin5, GPIO.LOW)
        GPIO.output(self.pin8, GPIO.LOW)

    def stop(self):
        GPIO.output(self.pin1, GPIO.LOW)
        GPIO.output(self.pin2, GPIO.LOW)
        GPIO.output(self.pin4, GPIO.LOW)
        GPIO.output(self.pin3, GPIO.LOW)
        GPIO.output(self.pin5, GPIO.LOW)
        GPIO.output(self.pin6, GPIO.LOW)
        GPIO.output(self.pin7, GPIO.LOW)
        GPIO.output(self.pin8, GPIO.LOW)
        GPIO.output(self.led2, GPIO.LOW)
        GPIO.output(self.led1, GPIO.LOW)


def main():
    # Set up the GPIO and car instance
    cars = Car(11, 13, 15, 37, 36, 16, 18, 22 , 35, 31)

    # Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode((200, 200))
    clock = pygame.time.Clock()

    # Main loop
    while True:
        # Process events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cars.stop()
                GPIO.cleanup()
                pygame.quit()
                return

        # Get the state of all keys
        keys = pygame.key.get_pressed()


        # Process the key states for movement
        if keys[pygame.K_w] and keys[pygame.K_d]:
            cars.forward()
            cars.right()
        elif keys[pygame.K_w] and keys[pygame.K_a]:
            cars.forward()
            cars.left()
        elif keys[pygame.K_s] and keys[pygame.K_d]:
            cars.backward()
            cars.right()
        elif keys[pygame.K_s] and keys[pygame.K_a]:
            cars.backward()
            cars.left()
        elif keys[pygame.K_w]:
            cars.forward()
        elif keys[pygame.K_s]:
            cars.backward()
        elif keys[pygame.K_d]:
            cars.right()
        elif keys[pygame.K_a]:
            cars.left()
        else:
            cars.stop()

        # Limit the frame rate
        clock.tick(60)

if __name__ == "__main__":
    main()