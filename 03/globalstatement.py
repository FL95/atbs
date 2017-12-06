def spam():
    global eggs 
    '''When you want a function to pull a variable
    from the global scope despite there being a variable of the 
    the same name within the local scope you must use a "global 
    statement" which consists of the word global followed by the
    variable name you want from the global scope'''
    eggs = 'Hello'
    print(eggs)   

eggs = 42
spam()
print(eggs)