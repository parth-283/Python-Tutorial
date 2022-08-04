clients = {1: "Parth", 2: "Chirag", 3: "Dishant"}
print(clients)
Choose_client = int(input("Choose one : "))

read_write = {1: "Read", 2: "Write"}
print(read_write)
user_choose_read_write = int(input("Choose one : "))

clients_activity = {1: "Diet", 2: "exercise"}
print(clients_activity)
Choose_client_activity = int(input("Choose one : "))
client_detail = {"Name": clients[Choose_client], "Activity": clients_activity[Choose_client_activity]}


# Date Function
def getdate():
    from datetime import datetime
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    return dt_string


Date_Time = getdate()


# List Convert into String Function
def listToString(s):
    # initialize an empty string
    str1 = " "

    # return string
    return (str1.join(s))


def HandleRead():
    if client_detail["Activity"] == "Diet":
        client_File_Name = [client_detail["Name"], '_', client_detail["Activity"], ".txt"]
        final_File_Name = listToString(client_File_Name).replace(" ", "")
        with open(final_File_Name) as f:
            a = f.read()
        f.close()

    else:
        client_File_Name = [client_detail["Name"], '_', client_detail["Activity"], ".txt"]
        final_File_Name = listToString(client_File_Name).replace(" ", "")
        with open(final_File_Name) as f:
            a = f.read()
        f.close()
    return a


def HandleWrite():
    if client_detail["Activity"] == "Diet":
        client_input_diet = input("Enter Your Diet...")
        client_detail.update({client_detail["Activity"]: client_input_diet, "Date_Time": Date_Time})

        client_File_Name = [client_detail["Name"], '_', client_detail["Activity"], ".txt"]
        final_File_Name = listToString(client_File_Name).replace(" ", "")
        with open(final_File_Name, 'a') as f:
            f.write(".................................\n")
            for key, value in client_detail.items():
                f.write('%s:%s\n' % (key, value))
            f.write(".................................\n")
        f.close()

    else:
        clients_exercise = input("Enter Your exercise...")
        client_detail.update({client_detail["Activity"]: clients_exercise, "Date_Time": Date_Time})
        print(client_detail)

        client_File_Name = [client_detail["Name"], '_', client_detail["Activity"], ".txt"]
        final_File_Name = listToString(client_File_Name).replace(" ", "")
        with open(final_File_Name, 'a') as f:
            f.write(".................................\n")
            for key, value in client_detail.items():
                f.write('%s:%s\n' % (key, value))
            f.write(".................................\n")
        f.close()
    return "Your Data Successfully Stored"


if read_write[user_choose_read_write] == "Read":
    print(HandleRead())
elif read_write[user_choose_read_write] == "Write":
    print(HandleWrite())
