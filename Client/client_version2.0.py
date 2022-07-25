# server.py first on
# client.py first off

from socket import*
from tkinter.tix import Tree
import serial



class socet_bridge(object):
	def __init__(self):
		port = "/dev/ttyUSB1"       
		self.serialPort = serial.Serial(port, baudrate = 38400, timeout = 0.5) #115200
        #self.ssock = socket(AF_INET, SOCK_STREAM)

	#def socket_open(self,):
	#	self.ssock.connect(("10.10.0.31", 9008))
	#def socket_close(self,):
	#	self.ssock.close()

	def parsing(self, event=None):
		ssock = socket(AF_INET, SOCK_STREAM)
		ssock.connect(("10.10.0.31", 9008))

		while True:
			RTK_NMEA = self.serialPort.readline() #Serial Data read
			#ssock.send(RTK_NMEA)
			
			rtk_mnea = RTK_NMEA.decode("utf-8", "ignore") #Transform bit data to string

			if 'GGA' in rtk_mnea: #GNGGA DATA 사용
				ssock.send(RTK_NMEA)
			
			if 'RMC' in rtk_mnea:
				split_rmc = rtk_mnea.split('$')
				#print(split_rmc[1])
				Split_rmc = '$' + split_rmc[1]
				ssock.send(Split_rmc.encode())
			else:
				pass
			print(rtk_mnea)
		ssock.close()




if __name__=='__main__':
	sb = socet_bridge()
	sb.parsing()
    
        
'''	
RTK_NMEA = self.serialPort.readline() #Serial Data read
ssock.send(RTK_NMEA)
ssock.close()
'''
