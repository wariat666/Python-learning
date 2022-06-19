commentUser = input("podaj komunikat: ")
rewerseCommentUser = ""
for i in range (len(commentUser)-1, -1, -1 ):
    rewerseCommentUser +=commentUser[i]
    
print (rewerseCommentUser)