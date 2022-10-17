# My GitHub:  		GitHub.com/AliRezaJoodi

from group_anagrams import group_anagrams_v10 as group_anagrams
from display import *

def main():
    words_list = ['cat', 'dog', 'fired', 'god', 'pat', 'tap', 'fried', 'tac']
    display("Word List:", words_list)
    anagrams_list = group_anagrams(words_list)
    display("Group Anagrams:", anagrams_list)
    
    
if __name__ == "__main__":
    main()