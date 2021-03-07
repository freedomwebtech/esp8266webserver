import socket
from machine import Pin
led = machine.Pin(05, Pin.OUT)
led1 = machine.Pin(16, Pin.OUT)
led2 = machine.Pin(2, Pin.OUT)


led.value(1)
led1.value(1)
led2.value(1)


s = socket.socket()
s.bind(('0.0.0.0', 80))
s.listen(5)
html = """
        <html>  <h1> <center>"ESP8266 WEB SERVER" </center></h1>
                 <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">
                 <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/js/bootstrap.bundle.min.js" integrity="sha384-b5kHyXgcpbZJO/tY9Ul7kGkf1S0CWuKcCD38l8YkeH8z8QjE0GmW1gYU5S9FOnJ0" crossorigin="anonymous"></script>     
                <style>
                
                .center {
                 display: flex;
                  justify-content: center;
                 align-items: center;
                 padding:10px;
                 margin:10px;
     
}

}
                 </style>
                
                
                
                <div class="center"><span><a href="/?led=on"><button class="btn btn-primary">On</button></center></a></span><span><a href="/?led=off"><button class="btn btn-danger">Off</button></a></span></div>
                
                <div class="center"><span><a href="/?led1=on"><button class="btn btn-primary">On</button></center></a></span><span><a href="/?led1=off"><button class="btn btn-danger">Off</button></a></span></div>
                <div class="center"><span><a href="/?led2=on"><button class="btn btn-primary">On</button></center></a></span><span><a href="/?led2=off"><button class="btn btn-danger">Off</button></a></span></div>
                
  

            
              
              
                
        </html>
        """

while True:
    cs,addr=s.accept()
    response=cs.recv(1048)
    response=str(response)
    led_on = response.find('/?led=on')
    led_off = response.find('/?led=off')
    led1_on = response.find('/?led1=on')
    led1_off = response.find('/?led1=off')
    led2_on = response.find('/?led2=on')
    led2_off = response.find('/?led2=off')
    
    
    if led_on == 6:
       print('LED ON')
       led.value(0)
    if led_off == 6:
       print('LED OFF')
       led.value(1)
    if led1_on == 6:
       print('LED ON')
       led1.value(0)
    if led1_off == 6:
       print('LED OFF')
       led1.value(1)   
       
    if led2_on == 6:
       print('LED ON')
       led2.value(0)
    if led2_off == 6:
       print('LED OFF')
       led2.value(1)     
    cs.sendall(html)
    cs.close()
    
