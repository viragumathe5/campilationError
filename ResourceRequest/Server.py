import os
import socket
from pyftpdlib import servers
from pyftpdlib.handlers import FTPHandler, ThrottledDTPHandler
from pyftpdlib.authorizers import DummyAuthorizer
def Main():
	perm_list = ['elr','elrmw']
	while True:
		username = input('Please Enter Server Username : ')
		password = input('Please Enter Server Password : ')
		if username == 'servermaster' and password=='serverpass':
			directory = '/home/soserious/Test'

			authorizer = DummyAuthorizer()

			authorizer.add_user('ajinkya','ajinkya2012',directory,'elrdfmwM','Master_login_Succesful','Ending_Master_Session')

			authorizer.add_user('reader','reader123',directory,'elr','Reader_Session','Reader_Bye')

			authorizer.add_user('writer','writer123',directory,'elrmw','Writer_Session','Writer_Bye')
			
			name = input('Please Enter Username to Add: ')
			pass_word = input('Please Enter Passord to Add: ')
			permit = int(input('Please Enter User Type (1 for Read-Only-----2 For ReadnWrite) : '))
			permission = perm_list[permit-1]
			welmsg = input('Please Enter Welcome Message : ')
			exmsg = input('Please Enter Welcome Message : ')
			authorizer.add_user(name,pass_word,directory,permission,welmsg,exmsg)

			dtp_handle = ThrottledDTPHandler
			dtp_handle.read_limit = 102400
			dtp_handle.write_limit = 102400

			handler = FTPHandler
			handler.authorizer = authorizer

			address = ("10.0.2.15",8086)
			server = servers.MultiprocessFTPServer(address,handler)
			server.serve_forever()
			server.close()

			print('Closed')
			break
		else:
			print('Please Input Correct Password!!!!!')
#Main()
#python3 -m pyftpdlib -i localhost -p 8021 -d /home/soserious/Test-m

