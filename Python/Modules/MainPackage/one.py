#One.py

def func():
    print("Func() in one.py")
    
print("Top Level in One.py")

if __name__ == '__main__':
    print("One Py is being run directly")
else:
    print("One.py has been imported")