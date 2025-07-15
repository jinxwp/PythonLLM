from functions.get_files_info import get_files_info
from functions.get_files_content import get_file_content

def main():

#    result = print(get_file_content("calculator", "lorem.txt"))
#    print(result)

    result = print(get_file_content("calculator", "main.py"))
#    print("Result for current directory:")
    print(result)
    print("")

    result = print(get_file_content("calculator", "pkg/calculator.py"))
#    print("Result for 'pkg' directory:")
    print(result)
    print("")

    result = print(get_file_content("calculator", "/bin/cat"))
#    print("Result for '/bin' directory:")
    print(result)
    print("")

    result = print(get_file_content("calculator", "pkg/does_not_exist.py"))
#    print("Result for '../' directory:")
    print(result)
    print("")
    

if __name__ == "__main__":
    main()
