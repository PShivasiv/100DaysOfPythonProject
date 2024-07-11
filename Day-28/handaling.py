#FileNotFound

# Exception Handaling
try:
    file = open("text.txt")
    dict = {"key":"value"}
    print(dict["hey"])
except FileNotFoundError:
    file = open("text.txt","w")
    file.write("this is the exception")
except KeyError as error_message:
    print(f"The key is {error_message} does not exist")
else:
    content = file.read()  # this will excuite when no error is found
    print(content)
finally:
    file.close()  # This will excuite no matter what happen if the error found or not its will excuite
    # raise KeyError  #This function rise the multiple type of error if the code have or not the error
