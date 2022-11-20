from tplinkcloud import TPLinkDeviceManager

username='ilia.malishev@gmail.com'
password='Tarakan24'

device_manager = TPLinkDeviceManager(username, password, term_id="71649F14-556A-50AC-99F7-1DC346FAE046")

import asyncio
import json



async def fetch_all_devices_sys_info():
  devices = await device_manager.get_devices()
  fetch_tasks = []
  print(devices)
  for device in devices:
    async def get_info(device):
      print(f'Found {device.model_type.name} device: {device.get_alias()}')
      print("SYS INFO")
      print(json.dumps(device.device_info, indent=2, default=lambda x: vars(x)
                        if hasattr(x, "__dict__") else x.name if hasattr(x, "name") else None))
      print(json.dumps(await device.get_sys_info(), indent=2, default=lambda x: vars(x)
                        if hasattr(x, "__dict__") else x.name if hasattr(x, "name") else None))
    fetch_tasks.append(get_info(device))
  await asyncio.gather(*fetch_tasks)

asyncio.run(fetch_all_devices_sys_info())