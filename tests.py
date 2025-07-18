from functions.get_files_info import get_files_info
from functions.get_files_content import get_file_content
from functions.write_files import write_file
from functions.run_python import run_python_file

def main():

#    result = print(get_file_content("calculator", "lorem.txt"))
#    print(result)

    result = print(run_python_file("calculator", "main.py"))
#    print("Result for current directory:")
    print(result)
    print("")

    result = print(run_python_file("calculator", "main.py", ["3 + 5"]))
#    print("Result for 'pkg' directory:")
    print(result)
    print("")

    result = print(run_python_file("calculator", "tests.py"))
#    print("Result for '/bin' directory:")
    print(result)
    print("")

    result = print(run_python_file("calculator", "../main.py"))
#    print("Result for '/bin' directory:")
    print(result)
    print("")
  
    result = print(run_python_file("calculator", "nonexistent.py"))
#    print("Result for '/bin' directory:")
    print(result)
    print("")

# 
# 
#  result = print(get_file_content("calculator", "pkg/does_not_exist.py"))
#    print("Result for '../' directory:")
#    print(result)
#    print("")
    

if __name__ == "__main__":
    main()
