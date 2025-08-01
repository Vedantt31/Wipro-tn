# 1. Write  a program to find check if a string has only octal digits. Given string ['789','123','004']
strings = input().split()
for s in strings:
    if all(ch in '01234567' for ch in s):
        print(f"'{s}' is octal")
    else:
        print(f"'{s}' is not octal")


"""2. Extract the user id, domain name and suffix from the following email addresses.
emails  = zuck@facebook.com
sunder33@google.com
jeff42@amazon.com
"""
import re
emails = [
    "zuck@facebook.com",
    "sunder33@google.com",
    "jeff42@amazon.com"
]

for email in emails:
    match = re.match(r'([\w\d]+)@([\w\d]+)\.(\w+)', email)
    if match:
        print(match.groups())


"""
3. Split the following irregular sentence into proper words
sentence = "A, very   very; irregular_sentence"  ##  expected outout : A very very irregular sentence
"""
import re
sentence = "A, very   very; irregular_sentence"
words = re.findall(r'\w+', sentence)
new_sentence = ' '.join(words)
print(new_sentence)


"""
4. Clean up the following tweet so that it contains only the user’s message. That is, remove all URLs, hashtags, mentions, punctuations, RTs and CCs.
#tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''
#desired_output = 'Good advice What I would do differently if I was learning to code today'
"""
import re
tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''#Complete Statement
clean_tweet = re.sub(r"(RT|cc:)", "", tweet)  # Remove RT, cc:
clean_tweet = re.sub(r"(@\w+)|(#\w+)", "", clean_tweet)  # Remove mentions and hashtags
clean_tweet = re.sub(r"http\S+", "", clean_tweet)  # Remove URLs
clean_tweet = re.sub(r"[^\w\s]", "", clean_tweet)  # Remove punctuation
clean_tweet = re.sub(r"\s+", " ", clean_tweet).strip()  # Clean extra spaces
print(clean_tweet)


"""
5. Extract all the text portions between the tags from the following HTML page: https://raw.githubusercontent.com/selva86/datasets/master/sample.html
Code to retrieve the HTML page is given below:
import requests
r = requests.get("https://raw.githubusercontent.com/selva86/datasets/master/sample.html")
r.text  # html text is contained here
desired_output = ['Your Title Here', 'Link Name', 'This is a Header', 'This is a Medium Header', 'This is a new paragraph! ', 'This is a another paragraph!', 'This is a new sentence without a paragraph break, in bold italics.']
"""
import requests
import re
r = requests.get("https://raw.githubusercontent.com/selva86/datasets/master/sample.html")
items = re.findall(r'>([^<]+)<', r.text)
cleaned = [text.strip() for text in items if text.strip()]
print(cleaned)


"""
6. Given below list of words, identify the words that begin and end with the same character. 
civic
trust
widows
maximum
museums
aa
as
"""
words = ['civic', 'trust', 'widows', 'maximum', 'museums', 'aa', 'as']
matches = [word for word in words if word[0].lower() == word[-1].lower()]
print(matches)

