'''#1
import re
def text_match(text):
        patterns = '^a(b*)$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')
a = input()
print(text_match(a))'''
'''#2
import re
def text_match(text):
        patterns = 'ab{2,3}'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')
a = input()
print(text_match(a))'''
'''#3
import re
def text_match(text):
        patterns = '^[a-z]+_[a-z]+$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

a = input()
print(text_match(a))'''
'''#4
import re
def text_match(text):
        patterns = '[A-Z]+[a-z]+$'
        if re.search(patterns, text):
                return 'Found a match!'
        else:
                return('Not matched!')
a = input()
print(text_match(a))'''
'''#5
import re
def text_match(text):
        patterns = 'a.*?b$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')
a = input()
print(text_match(a))'''
'''#6
import re
text = input()
print(re.sub("[ ,.]", ":", text))'''
'''#7
def snake_to_camel(word):
        import re
        return ''.join(x.capitalize() or '_' for x in word.split('_'))
a = input()
print(snake_to_camel(a))'''
'''#8
import re
text = input()
print(re.findall('[A-Z][^A-Z]*', text))'''
'''#9
import re
def capital_words_spaces(str1):
  return re.sub(r"(\w)([A-Z])", r"\1 \2", str1)
a = input()
print(capital_words_spaces(a))'''
'''#10
def camel_to_snake(text):
        import re
        str1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', str1).lower()
a = input()
print(camel_to_snake(a))
'''







