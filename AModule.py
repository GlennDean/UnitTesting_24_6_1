import pickle

corr_mat = pickle.load( open( "save_corr_mat.p", "rb" ) )
book_list = pickle.load( open( "save_book_list.p", "rb" ) )
book_names = pickle.load( open( "save_book_names.p", "rb" ) )

num_books_in_list = len(book_list)
max_books_to_display = 20

# sort a list of tuples on the 2nd element
def Sort_Tuple(tup): 
  
    # reverse = None (Sorts in Ascending order) 
    # key is set to sort using second element of 
    # sublist lambda has been used 
    tup.sort(key = lambda x: x[1],reverse = True) 
    return tup 

# book_name ==> index into book_names list
def get_index_for_book(book_name):
    for i in range(num_books_in_list):
        if book_names[i] == book_name:
            return i

    return -1

# book_name ==> index of a book in book_names that is closest
# to book_name
def get_first_index_closes_to_name(book_name):

    # IMPORTANT - search for names that match "the longest" (that is,
    # try to find a match on 7 characters, then 6, ...., then 1 character
    length = 7
    while length > 0:
        short = book_name[0:length].upper()
        for idx in range(len(book_names)):
            if book_names[idx][0:length].upper().find(short) >= 0:
                return idx
        # prepare for next loop
        length = length - 1

    return -1

# book_name ==> get list of 20 books that are before book_name and
# 20 books that are after book_name
def get_books_close_by_in_name(book_name):
    idx = get_first_index_closes_to_name(book_name)
    print(f"idx for {book_name} = ",idx)
    the_list = []
    if idx < 0:
        return the_list
    
    lower = idx - int(max_books_to_display/2)
    if lower < 0:
        lower = 0
    higher = idx + int(max_books_to_display/2)
    if higher >= num_books_in_list:
        higher = num_books_in_list - 1
    for i in range(lower,higher):
        the_list.append((book_names[i],0.00))

    return the_list

# book_name ==> ordered list of tuples, with descending
# values of cosine-similarity (each ordered tuple is of the form
# (book name,cos-sim value)
def get_ordered_list_for_book(book_name):
    ordered_list = []
    idx = get_index_for_book(book_name)
    if (idx < 0):
        return ordered_list
    unordered_list = [(book_names[i],corr_mat[idx,i]) for i in range(len(book_names))]
    
    ordered_list = Sort_Tuple(unordered_list)

    return ordered_list
