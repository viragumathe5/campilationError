import socket
from ftplib import FTP
import os
import sys
fp = FTP()
def Connector():
	try:
		fp.connect('10.0.2.15',8086)
	except:
		print("FTP Server Not Ready")
		sys.exit()
def login(username,password):
	try:
		print(fp.login(username,password))
		return True
	except:
		print("Please Enter Proper Login")
		return False
def ShowDirectory():
	print('\n\n')
	print('Directory : ')
	print('\n\n')
	fp.dir()
	print('\n\n')
def ChangeIt(path):
	try:
		fp.cwd(path)
		return True
	except:
		return False

def GetFile(name):
	out = "/home/soserious/FTPClient/"+name
	try:
		with open(out,"wb") as f:
			print('Getting.....')
			fp.retrbinary('RETR ' + name,f.write)
		print('Completed')
		return True
	except:
		return False

def SaveFile(name):
	out2 = '/home/soserious/FTPClient/'+name
	try:
		with open(out2,"rb") as f:
			print('Sending.....')
			fp.storbinary('STOR '+name,f)
		print('Completed')
		return True
	except:
		return False
	
	
	


def LoginPrompt():
	while True:
		print("Enter the Login Credential(Anonymous Login Not Allowed)")
		username = input("Enter the Username : ")
		password = input("Enter the Password : ")
		
		test_bool = login(username,password)
		
		if test_bool==True:
			break
		else:
			print("Please Enter Proper Credentials")
			continue
	

def ChoosenOne():
	while True:
		print("1.Show Directory\n2.Change Directory\n3.Rertieve File\n4.Store File\n5.Exit")
		choice = int(input("Choose Right Option : "))
		if choice == 1:
			ShowDirectory()
		elif choice == 2:
			folder_name = input("Enter The Folder Name : ")
			test_cwd = ChangeIt(folder_name)
			if test_cwd == True:
				print("Path Changed!!!")
			else:
				print("Enter Proper Folder Name!!!")
		elif choice == 3:
			file_name = input("Enter The File Name : ")
			test_ret = GetFile(file_name)
			if test_ret == True:
				print("Succes!!!")
			else:
				print("Enter Proper File Name!!!")
		elif choice == 4:
			file_name = input("Enter The File Name : ")
			test_ret = SaveFile(file_name)
			if test_ret == True:
				print("Succes!!!\n")
			else:
				print("Enter Proper File Name!!!\n")
		elif choice == 5:
			return True
			break
		else:
			print("Enter The Right Choice!!!")
def Main():
	Connector()
	while True:
		LoginPrompt()
		
		test_final = ChoosenOne()
		if test_final == True:
			print(fp.quit())
			break		
	
#Main()
