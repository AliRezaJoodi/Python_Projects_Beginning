# My GitHub:  		GitHub.com/AliRezaJoodi
# Source Link:		TheCleverProgrammer.com/2021/01/11/story-generator-with-python/
# Source Link:		GitHub.com/AmanKharwal/21-python-mini-projects/blob/main/story.py

import random

when = ['A few years ago', 'Yesterday', 'Last night', 'A long time ago','On 20th Jan']
name = ['Ali', 'Miriam','Daniel', 'Hoouk', 'Starwalker']
residence = ['Barcelona','India', 'Germany', 'Venice', 'England']
went = ['cinema', 'university','seminar', 'school', 'laundry']
happened = ['made a lot of friends','Eats a burger', 'found a secret key', 'solved a mistery', 'wrote a book']

print( \
    random.choice(when) + ', ' + \
    random.choice(name) + ' that lived in ' + \
    random.choice(residence) + ', went to the ' + \
    random.choice(went) + ' and ' + \
    random.choice(happened)\
)