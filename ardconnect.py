def compile():
    import serial
    import time
    serialcomm = serial.Serial('COM7',9600)
    serialcomm.timeout  = 1
    f= open("dosage.txt",'r')
    i = f.readline()
    print(i)
        
    


        
        
        #if int(i) == 'done':
            #print("DONE")
            #break
    for _ in range(2):
        serialcomm.write(i.encode())
        time.sleep(1)
        print(serialcomm.readline().decode('ascii'))
    #serialcomm.close()
