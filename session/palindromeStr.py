def palindrome_str():
    s = str(input())
  

    i,j = 0, len(s) - 1  
    is_palindrome = True 
    while i < j:
        if s[i] != s[j]: 
            is_palindrome = False
        break
    i += 1
    j -= 1

    if is_palindrome:
     print("Yes") 
    else:
        print("No")