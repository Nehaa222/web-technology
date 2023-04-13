def file_handling():
    '''
    This functions handels files, reads single line, multi line
    '''
    my_file = open("file.txt",'r')
    one_line = my_file.readline()
    multiple_lines = my_file.readlines()

    print(one_line)
    print("\n=========\n")
    print( multiple_lines)
    my_file.close()
file_handling()

with open("file.txt",'w') as write_to_file:
    write_to_file.write("Hello World")




