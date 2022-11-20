import asyncio

from plugp100 import TapoApiClient, TapoApiClientConfig, LightEffect
ip:str= "192.168.100.5"
email = "ilia.malishev@gmail.com"
passwd = "Tarakan24"

async def main():
    # create generic tapo api
    config = TapoApiClientConfig(ip, email, passwd)
    sw = TapoApiClient.from_config(config)
    await sw.login()
    await sw.on()
    await sw.set_brightness(10)
    state = await sw.get_state()
    print(state.get_unmapped_state())

    # light effect example
    await sw.set_light_effect(LightEffect.rainbow())
    state = await sw.get_state()
    print(state.get_unmapped_state())

    await sw.client.http.session.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.run_until_complete(asyncio.sleep(0.1))
loop.close()

