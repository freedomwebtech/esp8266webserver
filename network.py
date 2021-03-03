import network
w = network.WLAN(network.STA_IF)
w.active()
w.connect("mention your router ssid","mention your router password")
print("Ip Address Is", w.ifconfig())
