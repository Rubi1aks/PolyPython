pages = 100
lines_per_page = 50
symbols_per_line = 25
bytes_per_symbol = 4

book_size_bytes = pages * lines_per_page * symbols_per_line * bytes_per_symbol
disk_size_bytes = 1.44 * 1024 * 1024
books_on_disk = disk_size_bytes // book_size_bytes



print("Количество книг, помещающихся на дискету:", int(books_on_disk))
