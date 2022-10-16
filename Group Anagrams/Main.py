# My GitHub:  		GitHub.com/AliRezaJoodi

from Group_Anagrams import group_anagrams_v10
from Display import display

def main():
    words_list = ['cat', 'dog', 'fired', 'god', 'pat', 'tap', 'fried', 'tac']
    display("Word List:", words_list)
    anagrams_list = group_anagrams_v10(words_list)
    display("Group Anagrams:", anagrams_list)
    
    
if __name__ == "__main__":
    main()