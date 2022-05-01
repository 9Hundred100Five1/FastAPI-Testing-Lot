from pypresence import Presence
import time, psutil, platform

client_id = "933214976817119263"
rpc = Presence(client_id=client_id, pipe=0)
rpc.connect()
start_time = time.time() - time.monotonic()

os=platform.system()
image=None
text=None
if os=="Linux":
    image=None
    text="Ubuntu 20.04 LTS"
elif os=="Windows":
    image=None
    text="Windows Server 2022 Datacenter"

while True:
    mem = psutil.virtual_memory()
    rpc.update(
        # buttons=[{"label": "Watchdog", "url": "https://petcafe.xyz/invite"}, {"label": "Server", "url": "https://discord.gg/jVc3ByWVd3"}], 
        large_image=None, large_text="Intel Core i5 12600KF @3.7Ghz",
        small_image=None, small_text=text, 
        start=start_time, 
        
        details=f"CPU ㅣ{round(psutil.cpu_percent(interval=1), 1)}% {round(psutil.cpu_freq().current/1024, 2)}GHz", 
        state=f"RAMㅣ{round(mem.percent, 1)}% {round(mem.used/1024**3, 1)}GB/{round(mem.total/1024**3, 1)}GB",
    )
    time.sleep(1)