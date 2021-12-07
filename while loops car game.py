command= ""
while True:
    command =input(">").lower()
    if command == "start":
        print("car started!")
    elif command == "stop":
         print ("car stopped")
    elif command == 'help':
            print (""" 
start-to start the car
stop- to stop the car
quit- to quit the game""")
    elif command == "quit":
        break
    else:
            print ("sorry, I don't understand")
