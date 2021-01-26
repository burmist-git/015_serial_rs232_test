#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Date        : Tue Jan 26 21:20:26 CET 2021
Autor       : Leonid Burmistrov
Description : Simple reminder-training example
"""

import json
import os.path
import serial,sys,glob,select

def get_config_json(filename="./ect/config.json"):
    """
    Example to read json config file    
    """
    config = json.load(open(filename))
    return config

def print_config(config):
    """
    Print config
    """
    print(type(config))
    print(config.keys())
    print(config["par1"])
    print(config["par2"])
    print(config["par3"])
    
def main(filename="./ect/config.json"):
    """
    Definition of the main function (use for testing only)
    """
    config = get_config_json(filename=filename)
    print_config(config)
    
if __name__ == "__main__":
    """
    Run as main script (use for testing only)
    """
    #filename="./ect/config.json"
    #main(filename)

    '''
    dev  = "/dev/ttyACM*"
    scan = glob.glob(dev)
    rate = "9600"

    print('scan -- > ')
    print(scan)
    
    
    if (len(scan) == 0):
        dev  = '/dev/ttyUSB*'
        scan = glob.glob(dev)
        if (len(scan) == 0):
            print("Unable to find any ports scanning for /dev/[ttyACM*|ttyUSB*]" + dev) 
            sys.exit()
            
    serport = scan[0]

    print('serport',serport)
    '''
    
    ser = serial.Serial(port="/dev/ttyUSB0",baudrate="9600",parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=5)
    print("ser.portstr = ",ser.portstr)

    # D1=100
    ser.write(b'\x44\x31\x3D\x31\x30\x30\x0D\x0A')
    line = ser.readline()[:-2].decode('utf-8')
    line = ser.readline()[:-2].decode('utf-8')
    print("D1 =",line)
    # D1
    ser.write(b'\x44\x31\x0D\x0A')
    line = ser.readline()
    line = ser.readline()[:-2].decode('utf-8')
    print("D1 =",line)

    
    # #1 23 31
    # =  3D
    # U  55
    # I  49
    # P  50
    # D  44
    # 1  31
    # 2  32
    # 3  33
    # 4  34
    # 5  35
    # 6  36
    # 7  37
    # 8  38
    # 9  39
    '''
    # -> #1
    ser.write(b'\x23\x31\x0D\x0A')
    line = ser.readline()
    line = ser.readline()[:-2].decode('utf-8')
    print(line)
    # -> #2
    ser.write(b'\x23\x32\x0D\x0A')
    line = ser.readline()
    line = ser.readline()[:-2].decode('utf-8')
    print(line)

    # U1
    ser.write(b'\x55\x31\x0D\x0A')
    line = ser.readline()
    line = ser.readline()[:-2].decode('utf-8')
    print("U1 =",line)
    # U2
    ser.write(b'\x55\x32\x0D\x0A')
    line = ser.readline()
    line = ser.readline()[:-2].decode('utf-8')
    print("U2 =",line)

    # I1
    ser.write(b'\x49\x31\x0D\x0A')
    line = ser.readline()
    line = ser.readline()[:-2].decode('utf-8')
    print("I1 =",line)
    # I2
    ser.write(b'\x49\x32\x0D\x0A')
    line = ser.readline()
    line = ser.readline()[:-2].decode('utf-8')
    print("I2 =",line)

    # I1
    ser.write(b'\x50\x31\x0D\x0A')
    line = ser.readline()
    line = ser.readline()[:-2].decode('utf-8')
    print("I1 =",line)
    # I2
    ser.write(b'\x50\x32\x0D\x0A')
    line = ser.readline()
    line = ser.readline()[:-2].decode('utf-8')
    print("I2 =",line)

    # D1
    ser.write(b'\x44\x31\x0D\x0A')
    line = ser.readline()
    line = ser.readline()[:-2].decode('utf-8')
    print("D1 =",line)
    # D2
    ser.write(b'\x44\x32\x0D\x0A')
    line = ser.readline()
    line = ser.readline()[:-2].decode('utf-8')
    print("D2 =",line)

    # D1=100
    ser.write(b'\x44\x31\x3D\x31\x30\x30\x0D\x0A')
    line = ser.readline()
    line = ser.readline()[:-2].decode('utf-8')
    print("D1 =",line)
    # D2=100
    ser.write(b'\x44\x32\x3D\x31\x30\x30\x0D\x0A')
    line = ser.readline()
    line = ser.readline()[:-2].decode('utf-8')
    print("D2 =",line)
    '''

    '''
    while True:
        try:
            line = ser.readline()
            if line:
                # Uncomment the next line to display the input from the serial port in hex format
                #for x in line: print ("%s") % (x.encode('hex')),
                print('line',line)
                print('line.decode(utf-8)',line[:-2].decode('utf-8'))
                #print('type(line)',type(line))
                #print('len(line)',len(line))
                #for x in line: print(chr(x))
        except KeyboardInterrupt:
            sys.exit()
        except:
            pass
        #while sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
        #line = sys.stdin.readline()
        #print(line)
        #line = line.replace("\n","\r\n")
        # Uncomment the next two lines to display the typed in characters in hex format
        #for x in line: print ("%s") % (x.encode('hex')), print
        #ser.write(line)
    '''
    ser.close()
    #sys.exit()


    '''
    if (len(sys.argv) > 1):
        l = len(sys.argv) - 1
        while(l>0):
            if (sys.argv[l][0] == '/'): serport = sys.argv[l]
            else:                       rate    = sys.argv[l]
            l = l - 1

    ser = serial.Serial(port=serport,baudrate=rate,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=1)
    print("connected to: " + ser.portstr)

    while True:
        try:
            line = ser.readline()
            if line:
                # Uncomment the next line to display the input from the serial port in hex format
                #     for x in line: print ("%s") % (x.encode('hex')),
                print (line),
        except KeyboardInterrupt:
            sys.exit()
        except:
            pass
        while sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
            line = sys.stdin.readline()
            line = line.replace("\n","\r\n")
            # Uncomment the next two lines to display the typed in characters in hex format
            #    for x in line: print ("%s") % (x.encode('hex')),
            #    print
            ser.write(line)
            
    ser.close()
    sys.exit()
    '''
