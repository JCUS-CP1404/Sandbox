"""Input name and print odd characters"""
def main():

    name = get_name()#print odd characters in the name
    num=int(input("enter indexes to skip 1-continuous,2-alternate.."))
    print_name(name, num)
    #print odd characters in the name


def print_name(name, num):
    print(name[::num])


def get_name():
    name = input("Enter name:- ")
    # check that name is not blank
    while len(name) <= 0:
        print("Name is blank, enter again ")
        name = input("Enter name:- ")
    return name


main()