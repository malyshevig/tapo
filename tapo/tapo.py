


def main():
    from PyP100 import PyL530

    l530 = PyL530.L530("192.168.100.8", "ilia.malishev", "Tarakan24")

    l530.handshake()  # Creates the cookies required for further methods
    l530.login()  # Sends credentials to the plug and creates AES Key and IV for further methods

    # All the bulbs have the same basic functions as the plugs and additionally allow for the following functions.
    l530.setBrightness(50)  # Sets the brightness of the connected bulb to 50% brightness
    l530.setColorTemp(2700)  # Sets the color temperature of the connected bulb to 2700 Kelvin (Warm White)
    l530.setColor(30, 80)  # Sets the color of the connected bulb to Hue: 30°, Saturation: 80% (Orange)

    pass


if __name__ == "__main__":
    print("Name")
    main()