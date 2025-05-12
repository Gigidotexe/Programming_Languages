import socket

target = input("Enter the IP address to scan: ")
portRange = input("Enter the port range to scan (es. 5-200): ")

lowPort = int(portRange.split('-')[0])
highPort = int(portRange.split('-')[1])

print("scanning host", target, " from port ", lowPort, " to port ", highPort)

for port in range(lowPort, highPort):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	status = s.connect_ex((target, port))
	if(status == 0):
		print("*** Port ", port, " OPEN ***")
	else:
		 print("Port ", port, " Closed") 
