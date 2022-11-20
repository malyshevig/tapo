import asyncio

from plugp100 import TapoApiClient, TapoApiClientConfig, LightEffect, TapoDeviceState


#ip:str= "192.168.100.7"
#ip:str= "192.168.100.5"
ip:str= "192.168.100.11"

email = "ilia.malishev@gmail.com"
passwd = "Tarakan24"

import logging

logging.basicConfig(level = logging.DEBUG, format='%(process)d-%(levelname)s-%(message)s')
logging.warning('This is a Warning')
logging.debug('This is a Debug')

config = None

sw = None

async def init():
    global sw, config

    if sw is None:
        config = TapoApiClientConfig(ip, email, passwd)
        sw = TapoApiClient.from_config(config)
        await sw.login()
        asyncio.sleep(0.5)


async def turn(val:bool):
    # create generic tapo api
    global sw


    if val:
        await sw.on()
    else:
        await sw.off()

#    await sw.set_brightness(100)
    state = await sw.get_state()
    print(state.get_unmapped_state())


    # light effect example
#    await sw.set_light_effect(LightEffect.rainbow())
#    state = await sw.get_state()
#    print(state.get_unmapped_state())

async def __close__():
    global sw
    await sw.client.http.session.close()



async def brightness(val:bool):
    # create generic tapo api






    state: TapoDeviceState = await sw.get_state()
    print(f"brighthness = {state.brightness}")
    if state.brightness:
        if val:
            await sw.set_brightness(min(100,state.brightness+25 ))
            asyncio.sleep(0.1)
        else:
            await sw.set_brightness(max(5, state.brightness - 25))
            asyncio.sleep(0.1)




#    await sw.set_brightness(100)
    state = await sw.get_state()
    print(state.get_unmapped_state())

    # light effect example
#    await sw.set_light_effect(LightEffect.rainbow())
#    state = await sw.get_state()
#    print(state.get_unmapped_state())


def turn_on ():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(init())
    loop.run_until_complete(turn(True))
#    loop.run_until_complete(close())
    loop.run_until_complete(asyncio.sleep(0.1))





def turn_off ():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(init())
    loop.run_until_complete(turn(False))
#    loop.run_until_complete(close())
    loop.run_until_complete(asyncio.sleep(0.1))


def bright ():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(init())
    loop.run_until_complete(brightness(True))
    loop.run_until_complete(asyncio.sleep(0.1))

def dark():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(init())
    loop.run_until_complete(brightness(False))
    loop.run_until_complete(asyncio.sleep(0.1))


def close ():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(__close__())

#turn_off()