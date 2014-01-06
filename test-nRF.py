#!/usr/bin/env python
import rPi_spi

'''
	This is a very simple script that uses the rPi SPI port to read out the various registers in a nRF24L01+ device
		connected to the rPI SPI port 0

	It should be pretty self-explanitory
'''
status = rPi_spi.openSPI(speed=1000000)

print "SPI configuration = ", status

print "Reading nRF24L01 status registers:"

for x in range(28):
	dat = rPi_spi.transferSPI((x, 0))

	print "nRF Register 0x%X: %X" % (x, dat[1])

rPi_spi.closeSPI()
