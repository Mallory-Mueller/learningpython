command= ""
started = False
while True:
    command =input(">").lower()
    if command == "start":
        if started:
            print("Car is already startred.")
        else:
            started = True
            print("Car started!")
    elif command == "stop":
        if not started:
            print("Car is already stopped.")
        else:
            started= False
            print("Car is stopped.")
    elif command == "help":
        print (""" 
start-to start the car
stop- to stop the car
quit- to quit the game""")
    elif command == "quit":
        break
    else:
        print("sorry, I don't understand")


