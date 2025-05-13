import http.client

host = input("IP target: ")
port = input("Port target (default. 80): ")

metods= ["GET", "POST", "PUT", "OPTIONS", "HEAD"]
accepteds = []
counter = 0

if(port == ""):
	port =80
	
try: 
	connection = http.client.HTTPConnection(host, port)
	for metod in metods:
		connection.request(metod, '/')
		response = connection.getresponse()
		print(metod, "response: ", response.status)
		connection.close()
		if(response.status==200):
			accepteds.append(metod)
			counter+=1
	if(counter == 0):
		print("\nAccepted metods for", host,":", "NOONE")
	else:
		print("\nAccepted metods for", host,":", ", ".join(accepteds))
except ConnectionRefusedError:
	print("Failed Connection")
