# My GitHub:  		GitHub.com/AliRezaJoodi

from Dispaly import dispaly
debug = False

# Source Link:      https://thecleverprogrammer.com/2022/05/26/group-anagrams-using-python/
def group_anagrams_v20(words_list):
    from collections import defaultdict
    dispaly("\n", "", debug)
    dispaly("Function:", "group_anagrams_v20", debug)  
    dispaly("Words (Orginal):", words_list, debug)
    
    anagrams = defaultdict(list)
    for word_str in words_list:
        word_sorted_str = "".join(sorted(word_str))
        anagrams[word_sorted_str].append(word_str)
        
    dispaly("anagrams:", anagrams, debug)
    anagrams_list =  list(anagrams.values())
    dispaly("anagrams_list:", anagrams_list, debug)  
    return list(anagrams.values())
  
# Source Link:      https://www.tutorialspoint.com/group-anagrams-in-python#
def group_anagrams_v10(words_list):
    dispaly("\n", "", debug)
    dispaly("Function:", "group_anagrams_v10", debug)  
    dispaly("Words (Orginal):", words_list, debug)
    
    anagrams_dict = {}
    for word_str in words_list:
        word_sorted_list =  sorted(word_str)
        word_sorted_str = "".join(word_sorted_list)
        if word_sorted_str in anagrams_dict:
            anagrams_dict[word_sorted_str].append(word_str)
        else:
            anagrams_dict[word_sorted_str] = [word_str]
    
    dispaly("anagrams_dict:", anagrams_dict, debug)  
    anagrams_list =  list(anagrams_dict.values())
    dispaly("anagrams_list:", anagrams_list, debug)      
    return anagrams_list
    
    
if __name__ == "__main__":
    debug = True
    group_anagrams_v20(["ant", "eat", "car", "ate", "tan", "tea", "nat"])
    group_anagrams_v10(["ant", "eat", "car", "ate", "tan", "tea", "nat"])