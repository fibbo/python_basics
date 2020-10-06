def reverse_text(text):
    n=len(text)-1
    i=0
    list_1=[]
    reverse =''
    while n > -1:
        list_1.append(text[n])
        reverse = reverse + list_1[i]
        n = n - 1
        i=i+1
        print(reverse)


reverse_text('text')