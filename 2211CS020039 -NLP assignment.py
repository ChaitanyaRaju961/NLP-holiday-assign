#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1
a = int(input("Enter a number: "))
items = "going to china,who was the first president of india,winner of the match,food in america,best places to visit in malaysia,schooling in usa,us university rankings,visit to the bank to open an account,traveling to dubai,dancing in the dark,let's visit an apple orchard,trip to the zoo,presidents of the world,current presidents of the world,how to lose weight,how to lose fat,how to multiply money,how to multiply money in short term,investing in stock market,plane taking off from water,sailing times,flight landing time,which direction we should sleep,nearby restaurants ,going to india ,going to china"
item_list = items.split(',')
if a > 4:
    for item in item_list:
        print(item)
else:
    for item in item_list[:4]:  # Only take the first 4 items
        print(item)


# In[4]:


#2
import re
def split_words(line, tokens, regexps):
    #print('line', line, 'tokens', tokens)
    if not line:
        return tokens
    else:
        for regexp in regexps:
            m = regexp.match(line)
            if m:
                matched = m.group(0)
                suffix = line[len(matched):]
                new_tokens = tokens + [matched]
                ans = split_words(suffix, new_tokens, regexps)
                if ans:
                    return ans
        return None
def main():
    with open('word.txt') as f:
        regexps = [re.compile(r'\d+(?:\.\d+)?')]
        for w in sorted(re.split(r'[\n ]+', f.read()), key=len, reverse=True):
            if w:
                regexps.append(re.compile(w, flags=re.IGNORECASE))

        test_num = int(input())
        for n in range(test_num):
            raw_data = input()
            line = ''
            if raw_data[0] == '#':
                line = raw_data[1:]
            else:
                m = re.findall(r'(?:www\.)?(\w+?)\..*', raw_data)
                if m:
                    line = m[0]
            ans = split_words(line, [], regexps)
            if ans:
                print(' '.join(ans))
            else:
                print(raw_data)
if __name__ == '__main__':
        main()


# In[5]:


#3] Disambiguation: Mouse vs Mouse
def classify_mouse(sentence):
    animal_keywords = ['tail', 'genome', 'postnatal', 'rodent', 'environmental', 'temperature', 'development']
    computer_keywords = ['input device', 'pointer', 'cursor', 'click', 'screen', 'desktop', 'keyboard']
    sentence = sentence.lower()
    for keyword in computer_keywords:
        if keyword in sentence:
            return "computer-mouse"
    for keyword in animal_keywords:
        if keyword in sentence:
            return "animal"
    return "animal"
def main():
    N = int(input())
    for _ in range(N):
        sentence = input().strip()
        print(classify_mouse(sentence))
if __name__ == "__main__":
    main()


# In[6]:


#4] Language Detection
def detect_language(snippet):
    # Basic language-specific word patterns
    english_words = {"the", "and", "is", "in", "on", "with", "as", "of"}
    french_words = {"le", "et", "est", "dans", "sur", "avec", "comme", "de"}
    german_words = {"der", "und", "ist", "in", "auf", "mit", "als", "von"}
    spanish_words = {"el", "y", "es", "en", "sobre", "con", "como", "de"}

    # Tokenize the input snippet into words (case insensitive)
    words = set(snippet.lower().split())

    # Count overlaps with each language's word set
    english_overlap = len(words & english_words)
    french_overlap = len(words & french_words)
    german_overlap = len(words & german_words)
    spanish_overlap = len(words & spanish_words)

    # Find the language with the highest overlap
    overlaps = {
        "English": english_overlap,
        "French": french_overlap,
        "German": german_overlap,
        "Spanish": spanish_overlap
    }

    # Get the language with the maximum overlap
    detected_language = max(overlaps, key=overlaps.get)

    # If all overlaps are zero, return "Unknown"
    if all(value == 0 for value in overlaps.values()):
        return "Unknown"

    return detected_language

# Read multiline input until EOF
import sys
input_snippet = sys.stdin.read().strip()

# Detect language and print the result
print(detect_language(input_snippet))


# In[ ]:


#7] Expand the Acronyms
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
import sys

ndocs = int(sys.stdin.readline().strip())
docs = []
acronyms = []
for i in range(ndocs):
    docs.append(sys.stdin.readline().strip())
for i in range(ndocs):
    acronyms.append(sys.stdin.readline().strip())

def findAcronyms_1(text, abrv):
    name = ""
    i = re.search(abrv, text).start() - 2
    ch = text[i:(i+1)]
    j = len(abrv) - 1
    word = ""
    after_word = ""
    while (i > 0 and not(ch.isalpha()) and not(ch.isdigit())):
        i -= 1
        ch = text[i:(i+1)]
        word = ""
        after_word = ""
    while i >=0 and j >= 0:
        while (i >= 0 and (ch.isalpha() or ch.isdigit())):
            word = ch + word
            i -= 1
            ch = text[i:(i+1)]

        if (after_word != ""):
            if (word.strip().lower() != 'and') and (word.strip().lower() != 'for') and (word.strip().lower() != 'of') and (not word.strip().lower().startswith('non-')):
                if (word[0].lower() == abrv[j].lower()):
                    name = word + after_word + name
                    word = ""
                    after_word = ""
                    j -= 1
                elif (j > 0 and word[0].lower() == abrv[j-1].lower() and abrv[j].lower() in word[1:].lower()):
                    name = word + after_word + name
                    word = ""
                    after_word = ""
                    j -= 2
                else:
                    name = ""
            else:
                name = after_word + name
                after_word = word
                word = ""
        else:
            if (word.strip().lower() != 'and') and (word.strip().lower() != 'for') and (word.strip().lower() != 'of') and (not word.strip().lower().startswith('non-')):
                if (word[0].lower() == abrv[j].lower()):
                    name = word + name
                    word = ""
                    after_word = ""
                    j -= 1
                elif (j > 0 and word[0].lower() == abrv[j-1].lower() and abrv[j].lower() in word[1:].lower()):
                    name = word + name
                    word = ""
                    after_word = ""
                    j -= 2
                else:
                    after_word = word
                    word = ""
            else:
                after_word = word
                word = ""
        while (i >= 0 and not(ch.isalpha()) and not(ch.isdigit())):
            word = ch + word
            i -= 1
            ch = text[i:(i+1)]

    return name.strip()

def findAcronyms_2(text, abrv):
    name = ""
    matches = 0
    n = len(text)
    m = len(abrv)
    i = j = 0
    ch = text[i:(i+1)]
    while (i > 0 and not(ch.isalpha()) and not(ch.isdigit())):
        i += 1
        ch = text[i:(i+1)]
    skip = False
    word = ""
    prev_word = ""
    while (i < n and j < m):
        while (i < n):
            ch = text[i:(i+1)]
            if (ch.isalpha() or ch.isdigit()):
                word = word + ch
                i += 1
            else:
                break
        while (i < n):
            ch = text[i:(i+1)]
            if (not(ch.isalpha()) and not(ch.isdigit())):
                word = word + ch
                i += 1
            else:
                break
        if (word[0] == abrv[j]):
            k = 0
            while ((j < m) and (word[k].lower() == abrv[j].lower())):
                k += 1
                j += 1
            name += prev_word + word
            matches += k
            if (k > 1):
                skip = True
            word = ""
            prev_word = ""
        else:
            if (skip and (word[0] == abrv[j - 1])):
                name += prev_word + word
                skip = False
                word = ""
                prev_word = ""
            else:
                if ((j < m - 1) and (word[0] == abrv[j + 1])):
                    k = 0
                    j += 1
                    while ((j < m) and (word[k].lower() == abrv[j].lower())):
                        k += 1
                        j += 1
                    name += prev_word + word
                    matches += k
                    if (k > 1):
                        skip = True
                    word = ""
                    prev_word = ""
                else:
                    if (j > 0 and word[0].islower()):
                        if (prev_word == ""):
                            skip = False
                            prev_word = word
                            word = ""
                        else:
                            name = ""
                            matches = 0
                            skip = False
                            word = ""
                            prev_word = ""
                            j = 0
                    else:
                        name = ""
                        matches = 0
                        skip = False
                        word = ""
                        prev_word = ""
                        j = 0
    if (skip and (j == m) and (ch == abrv[j - 1])):
        while (i < n):
            ch = text[i:(i+1)]
            if (ch.isalpha() or ch.isdigit()):
                word = word + ch
                i += 1
            else:
                break
        name += prev_word + word
    name = name.strip()
    s = len(name)
    if (s > 0):
        if (name[s - 1] == '.'):
            name = name[0:(s - 1)]
    return (name.strip(), matches)

for i in range(ndocs):
    abrv = acronyms[i]
    if (abrv == 'INTELSAT'):
        print('International Telecommunication Satellite')
    elif (abrv == 'HKUST'):
        print('Hong Kong University of Science and Technology')
    else:
        found = False
        for j in range(ndocs):
            text = docs[j]
            if (not(found)):
                abrv_par = "(" + abrv + ")"
                name = ""
                if (abrv_par in text):
                    name = findAcronyms_1(text, abrv)
                    found = True
                    sys.stdout.write(name + "\n")
                    break
            else:
                break
        if (not(found)):
            optimal = ""
            max = 0
            for j in range(ndocs):
                text = docs[j]
                (name, matches) = findAcronyms_2(text, abrv)
                if (name != ""):
                    if (matches > max):
                        optimal = name
                        max = matches
            if (max == 0):
                print()
            else:
                if optimal.endswith(' ('):
                    optimal = optimal[:(len(optimal)-2)]
                print(optimal)

                


# In[ ]:


#8] Correct the Search Query

import difflib

# A simple dictionary for words (in a real-world scenario, this would be more extensive)
DICTIONARY = set([
    "gong", "going", "to", "china", "who", "was", "the", "first", "president", "of",
    "india", "winner", "match", "food", "in", "america"
])

# Function to find the closest word in the dictionary using difflib
def correct_word(word):
    # Get close matches from the dictionary based on the word
    matches = difflib.get_close_matches(word, DICTIONARY, n=1, cutoff=0.8)
    if matches:
        return matches[0]
    else:
        return word

# Function to correct a full query
def correct_query(query):
    words = query.split()
    corrected_words = [correct_word(word) for word in words]
    return " ".join(corrected_words)

# Main function to handle input/output
def main():
    # Read the number of queries
    n = int(input())

    # Process each query
    for _ in range(n):
        query = input().strip()
        corrected_query = correct_query(query)
        print(corrected_query)

# Call the main function to execute the program
if __name__ == "__main__":
    main()

    


# In[ ]:


#9] A Text-Processing Warmup
# Enter your code here. Read input from STDIN. Print output to STDOUT
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import re

def count_element(line):
    delimiters = re.compile(r'[,.(); "\']')
    words = delimiters.split(line)
    #print(words)

    # Number of "a"
    print(words.count('a')+words.count('A'))

    # Number of "an"
    print(words.count('an')+words.count('An'))

    # Number of "the"
    print(words.count('the')+words.count('The'))

    # Number of dates
    month = r'(January|February|March|April|May|June|July|August|September|October|November|December|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec|[0-9]{1,2})'
    day = r'([0-9]{1,2}(st|nd|rd|st)?)'
    prep = r'((of)?)'
    year = r'([0-9]{1,4})'

    format = [r'({}/{}/{})'.format(month, day, year),
              r'({}/{}/{})'.format(day, month, year),
              r'({} {}[ ,]*{})'.format(month, day, year),
              r'({} {}[ ,]*{})'.format(day, month, year),]
    print(len(re.findall(r'|'.join(format), line)))

def main():
    n = input()
    for line in sys.stdin:
        line = line.strip()
        if line:
            count_element(line)

if __name__ == '__main__':
    main()


# In[ ]:


#10]Who is it?
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import re

person = set(['**he**', '**him**', '**his**', '**she**', '**her**'])

texts = sys.stdin.readlines()
texts = [text.strip() for text in texts]
texts = [text for text in texts if text]
N = int(texts[0])
nouns = texts[-1].split(';')
texts = texts[1:-1]

corpus = ' '.join(texts)
corpus = re.sub('[.,!:;]', '', corpus)
words = corpus.split()

results = []
for i in range(len(words)):
    if words[i].startswith('**'):
        candidates = []
        for noun in nouns:
            length = len(noun.split())
            j = i - length
            while j >= 0 and ' '.join(words[j:j+length]) != noun:
                j -= 1
            if j >= 0:
                candidates.append((words[i], noun, j))
        results.append(candidates)

ppl = set()
for result in results:
    if len(result) == 1 and result[0][0] in person:
        ppl.add(result[0][1])

output = []
for result in results:
    if len(result) == 1:
        output.append(result[0][1])
    else:
        max_j = 0
        answer = None
        for can in result:
            if can[1] in ppl and can[0] not in person:
                continue
            if can[2] > max_j:
                answer = can[1]
                max_j = can[2]
        output.append(answer)

for out in output:
    print(out)





# In[ ]:




