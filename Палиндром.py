# Палиндром
def is_palindrome(text):
    summary=[]
    summary_reverse=[]
    for i in text:
        if i.isalpha():
            summary.append(i.lower())
    for i in summary[::-1]:
        summary_reverse.append(i)
    summary=''.join(summary)
    summary_reverse=''.join(summary_reverse)
    if summary==summary_reverse:
        return True
    else:
        return False
text=input()
print(is_palindrome(text))