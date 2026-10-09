# Змеиный регистр 🐍
def convert_to_python_case(text):
    summary=[]
    for i in text:
        if i.isupper():
            summary.append(' ')
            summary.append(i.lower())
        else:
            summary.append(i)
    summary=summary[1:len(summary)]
    summary=''.join(summary)
    summary=summary.replace(' ','_')
    return summary
text='HelloMyWorld'
convert_to_python_case(text)