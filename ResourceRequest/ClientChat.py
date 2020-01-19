import socket as sk
import select
import sys

key = 'abcdefghijklmnopqrstuvwxyzASDFGHJKLQWERTYUIOPZXCVBNM1234567890!@#&'

tester = ['exit','EXIT','Exit']

sc = sk.socket(sk.AF_INET,sk.SOCK_STREAM)
try:
	sc.connect(('10.0.2.15',8025))
except:
	print('Server Not Ready')

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

def Main():

	while True:
		socket_list = [sys.stdin,sc]
		read_sockets,write_socket,error_socket = select.select(socket_list,[],[])
		
		for i in read_sockets:
			if i==sc:
				message = sc.recv(2048)
				strmsg = str(message,'utf-8')
				realmsg = decrypt(strmsg)
				if realmsg:
					print(realmsg)
				else:
					sc.close()
			else:
				message = input()
				#print(message)
				if message in tester:
					try:	
						sc.close()
						sys.exit()
					except ValueError:
						print("ERROR!!!!")
				else:
					encmsg = encrypt(message)
					bytemsg = bytes(encmsg,'utf-8')
					sc.send(bytemsg)
					print('<You> ',end = " : ")
					print(message)
					sys.stdout.flush()
	#sc.close()
Main()
