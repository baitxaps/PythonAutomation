import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print(mo.group(0))
print(mo.group(2))
print(mo.group())
print(mo.groups())

heroRegex = re.compile (r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
print(mo1.group())
mo2 = heroRegex.search('Tina Fey and Batman.')
print(mo2.group())

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())
print(mo.group(1))

batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())

batRegex = re.compile(r'Bat(wo)*man') 
mo1 = batRegex.search('The Adventures of Batman')
mo1.group()
mo2 = batRegex.search('The Adventures of Batwoman')
mo2.group()
mo3 = batRegex.search('The Adventures of Batwowowowoman')
mo3.group()

haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
print(mo1.group())
mo2 = haRegex.search('Ha')
print(mo2)

greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())
nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
print(mo2.group())

# nogroupsRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups
# re =nogroupsRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
# print(re)
# groupsRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # has groups
# re=groupsRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
# print(re)

xmasRegex = re.compile(r'\d+\s\w+')
xmax =xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, \
7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
print(xmax)

vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('RoboCop eats baby food. BABY FOOD.'))
consonantRegex = re.compile(r'[^aeiouAEIOU]')
print(consonantRegex.findall('RoboCop eats baby food. BABY FOOD.'))

beginsWithHello = re.compile(r'^Hello')
print( beginsWithHello.search('Hello world!'))
print(beginsWithHello.search('He said hello.') == None)

atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat. tsat. td.'))

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo.group(1))

newlineRegex = re.compile('.*', re.DOTALL)
print(newlineRegex.search('Serve the public trust.\nProtect the innocent. \nUphold the law.').group())

'''
 ?匹配零次或一次前面的分组。
 *匹配零次或多次前面的分组。
 +匹配一次或多次前面的分组。
 {n}匹配 n 次前面的分组。
 {n,}匹配 n 次或更多前面的分组。
 {,m}匹配零次到 m 次前面的分组。
 {n,m}匹配至少 n 次、至多 m 次前面的分组。
 {n,m}?或*?或+?对前面的分组进行非贪心匹配。
 ^spam 意味着字符串必须以 spam 开始。
 spam$意味着字符串必须以 spam 结束。
 .匹配所有字符，换行符除外。
 \d、\w 和\s 分别匹配数字、单词和空格。
 \D、\W 和\S 分别匹配出数字、单词和空格外的所有字符。
 [abc]匹配方括号内的任意字符(诸如 a、b 或 c)。
 [^abc]匹配不在方括号内的任意字符。  
 
'''

robocop = re.compile(r'robocop', re.I)
print(robocop.search('RoboCop is part man, part machine, all cop.').group())
print(robocop.search('ROBOCOP protects the innocent.').group())
print(robocop.search('Al, why does your programming book talk about robocop so much?').group())


namesRegex = re.compile(r'Agent \w+')
print(namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.'))
agentNamesRegex = re.compile(r'Agent (\w)\w*')
print(agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'))

phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))?              # area code 
(\s|-|\.)?                      # separator 
\d{3}                           # first 3 digits
(\s|-|\.)                       # separator
\d{4}                           # last 4 digits
(\s*(ext|x|ext.)\s*\d{2,5})?    # extension
)''', re.VERBOSE)   

someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL)
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)


'''
project

'''

import pyperclip
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?
    (\s|-|\.)?
    (\d{3})
    (\s|-|\-)
    (\d{4})
    (\s*(ext|x|ext.)\s*(\d{2,5}))?                   
)''',re.VERBOSE)

# TODO: Create email regex.
emailRegex = re.compile(r'''(
  [a-zA-Z0-9._%+-]+ # username
  @                 # @symbol  
  [a-zA-Z0-9.-]+    # domain name
  (\.[a-zA-Z]{2,4}) # dot-something
  )''', re.VERBOSE)

# TODO: Find matches in clipboard text.
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
       phoneNum += ' x' + groups[8]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

# TODO: Copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')


# 16..*执行贪心匹配，.*?执行非贪心匹配。
# 17.[0-9a-z]或[a-z0-9]
# 18.'X drummers, X pipers, five rings, X hens'
# 19.re.VERBOSE 参数允许为传入 re.compile() 的字符串添加空格和注释。 
# 20.re.compile(r'^\d{1,3}(,{3})*$')将创建这个正则表达式，但其他正则表达式字符串可以生成类似的正则表达式。 
# 21.re.compile(r'[A-Z][a-z]*\sNakamoto')
# 22.re.compile(r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.',re.IGNORECASE)
# 
# 