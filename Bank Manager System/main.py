from manager import Manager

def main():
    
    ch = '0'
    while ch != '2':
        print('Login Page\n1.LOGIN\n2.EXIT')
        ch = input('Enter Choice: ')
        if ch == '1':
            u = 'admin'
            p = '1234'
            userid = input("Enter User Id: ")
            passw = input("Enter Password: ")
            if userid == u and passw == p:
                print("Login Successfully!!")
                mgr = Manager()          
                mgr.managerMenu()   
            else:
                print("Invalid Credientails!!")
        elif ch == '2':
            print("____EXIT FROM LOGIN PAGE____")

main()
