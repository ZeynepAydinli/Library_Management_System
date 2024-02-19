           
class Library:
    
    def __init__(self):
        try:
            self.file = open("books.txt", "a+")
            Library.initialize_file(self)
        except FileNotFoundError:
            print("File was not found")
        
    def __del__(self):
        self.file.close()  
        
    def initialize_file(self):
        if self.file.tell() == 0:
            books_columns = "book_title,author,release_date,number_of_pages\n"
            self.file.write(books_columns)

    # Check value type is int
    def check_int_type(value):
        try:
            is_int = int(value)
            return is_int
        except ValueError:
            print("Please enter a NUMERIC value.\n")
    
    # Check value range 1 until 4
    def check_value_range(value):
        if value<1 :
            return False
        elif value>4 :
            return False
        else :
            return True               
    
    def list_books(self):
                
        self.file.seek(0)  # Go to the beginning of the file
        lines = self.file.readlines()[1:]  # Skip the first line (column headers)
        if len(lines) <= 0:
            print("There is no book!")
        else:
            lines = lines[0:]  # Skip the first line (column headers)
            print("------------- List Of Books -------------")
            for line in lines:
                book_info = line.strip().split(',')
                book_name = book_info[0]
                author = book_info[1]
                print(f"Book: {book_name}, Author: {author}")
            
        
    def add_book(self):
        book_name = str(input("Enter the book name: ").strip().title())
        book_name = "_".join(book_name.split())
        book_name = book_name.replace(",", "_")
        
        author = str(input("Enter the author's name: ").strip().title())
        author = "_".join(author.split())
        author = author.replace(",", "_")
        
        while True:
            release_date = input("Enter the release year of the book: ")
            is_int = Library.check_int_type(release_date)
            if type(is_int) is int :
                break
            else :
                continue

        while True:
            number_of_pages = input("Enter the number of pages of the book: ")
            is_int = Library.check_int_type(number_of_pages)
            if type(is_int) is int :
                break
            else :
                continue
 
        book_info = f"{book_name},{author},{release_date},{number_of_pages}\n" 
        self.file.write(book_info)
        self.file.flush()
        
        print("")
        print(f"Book '{book_name}' by '{author}' added successfully!")
        print("")
    
    def remove_book(self):
        word = input("Enter the book title: ").title()
        try:
            with open("books.txt", "r+") as file:
                lines = file.readlines()
                file.seek(0)
                found = False
                for line in lines:
                    if word not in line:
                        file.write(line)
                    else:
                        found = True
                file.truncate()  
                if not found:
                    print("The book was not found!")
                else:
                    print("Book removed successfully!")
        except FileNotFoundError:
            print("File not found. Please add a book first.")
                

lib = Library()
lib.initialize_file()

while True:
    print("")
    print( "***MENU***\n1) List Books\n2) Add Book\n3) Remove Book\n4) Quit")
    choice = input("Enter your choice: ")
    print("")
    try:
        type_casting = Library.check_int_type(choice)

        if type(type_casting) is int  :

            range_value = Library.check_value_range(type_casting)
    
            if range_value == False :
                print("Please enter a value between 1 and 4 \n");

            else :
                if type_casting == 1 :
                    lib.list_books()

                elif type_casting == 2 :
                    lib.add_book()

                elif type_casting == 3 :
                    lib.remove_book()

                elif type_casting == 4:
                    del lib
                    break
                else:
                    print("Invalid choice. Please enter a valid option.")

    except ValueError :
        print("Invalid choice. Please enter a valid option.")