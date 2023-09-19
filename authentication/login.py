database = [["aakash","hello$11", 0],
            ["abhinav","abinav@11",0],
            ["prabhu","prabhu",0]]

def login(username , password) : 
    for user_detail in database : 
        if user_detail[0] == username and user_detail[1] == password :
            user_detail[2] = 1 
            print("Login successful") 

login("aakash","hello$11")