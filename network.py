import network
w = network.WLAN(network.STA_IF)
w.active()
print("Ip Address Is", w.ifconfig())
