def main():
    book_source = "books/frankenstein.txt"
    with open(book_source) as f:
        file_contents = f.read()
        #print(file_contents)
        #counting_words(file_contents)
        count_letters_repeats(file_contents)

def counting_words(text):
    return len(text.split())

def count_letters_repeats(text):
    text_to_lower_case = text.lower()
    result = {}
    for character in text_to_lower_case:
        if character in result:
            result[character] += 1
        else:
            result[character] = 1 
   
    #print(result)
    dict_to_parsed(result)

def sort_on(dict):
    return dict["count"]

def dict_to_parsed(dict_to_parse):
    result = []
    for record in dict_to_parse:
        if record.isalpha():
            #print(f"----Checking:{record} and {dict_to_parse[record]}")
            to_add = {"character": record , "count": dict_to_parse[record]}
            result.append(to_add)
    result.sort(reverse=True, key=sort_on)
    nicely_print_this(result)
    #print(result)

def nicely_print_this(results):
    for r in results:
        #print(r)
        test1 = r["character"]
        test2 = r["count"]
        print(f"The '{test1}' character was found {test2} times")

main()