import socket as sk
import threading
import _thread

key = 'abcdefghijklmnopqrstuvwxyzASDFGHJKLQWERTYUIOPZXCVBNM1234567890!@#&'

ss = sk.socket(sk.AF_INET,sk.SOCK_STREAM)
ss.bind(('10.0.2.15',8025))

ss.listen(100)


connected_list = []

def encrypt(message):
	result = ''
	message2 = message[::-1]
	for i in message2:
		try:
			j = (key.index(i)+7)%len(key)
			result = result+key[j]
		except ValueError:
			result = result+i
	return result
	
def decrypt(message):
	result = ''
	for i in message:
		try:
			j=(key.index(i)-7)%len(key)
			result = result+key[j]
		except ValueError:
			result = result+i
	message2 = result[::-1]
	return message2		
	
def start_chat(conn,addr):
	test = str(threading.active_count())
	#print(test)
	welmsg = 'Welcome to Resource Requestor \nCurrently Active Members : ' + test + '\n***Please Do Not Send Blank Messages***'
	sendmsg = encrypt(welmsg)
	#print(sendmsg)
	#testmsg = decrypt(sendmsg)
	#print(testmsg)
	bytedmsg = bytes(sendmsg,'utf-8')
	conn.send(bytedmsg)
	
	notmsg = bytes(encrypt(addr[0] + ' Just Joined \nCurrently Active Members : ' + str(threading.active_count()-1)),'utf-8')
	broadcast(conn,notmsg)
	while True:
		try:
			bytemessage  = conn.recv(2048)
			message = str(bytemessage,'utf-8')
			realmsg = decrypt(message)
			if realmsg:
				sendtomsg = '<'+addr[0]+'> : '+realmsg
				print(sendtomsg)
				sendenc = encrypt(sendtomsg)
				sendbyte = bytes(sendenc,'utf-8')
				broadcast(conn,sendbyte)
			else:
				connected_list.remove(conn)
		except:
			continue		

def broadcast(conn,message):
	for connect in connected_list:
		if connect!=conn:
			try:
				connect.send(message)
			except:
				connect.close()
				connected_list.remove(connect)
		
def Main():
	while True:
		conn, addr = ss.accept()
		connected_list.append(conn)
		print(addr[0],' Connected')
		_thread.start_new_thread(start_chat,(conn,addr))
	conn.close()
	ss.close()

Main()
