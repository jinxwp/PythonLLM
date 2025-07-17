from functions.get_files_info import get_files_info
from functions.get_files_content import get_file_content
from functions.write_files import write_file

def main():

#    result = print(get_file_content("calculator", "lorem.txt"))
#    print(result)

    result = print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
#    print("Result for current directory:")
    print(result)
    print("")

    result = print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
#    print("Result for 'pkg' directory:")
    print(result)
    print("")

    result = print(write_file("calculator", "/tmp/temp.txt", "this should not be allowe"))
#    print("Result for '/bin' directory:")
    print(result)
    print("")

#    result = print(get_file_content("calculator", "pkg/does_not_exist.py"))
#    print("Result for '../' directory:")
#    print(result)
#    print("")
    

if __name__ == "__main__":
    main()
