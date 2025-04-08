from anagram_checker import AnagramChecker

def is_valid_input(word):
    if len(word.split()) > 1:
        print("Error: Only a single word is allowed.")
        return False
    
    if not word.isalpha():
        print("Error: Only alphabetic characters are allowed.")
        return False
    
    return True

def main():
    anagram_checker = AnagramChecker()

    while True:
        print("\n=== ANAGRAM CHECKER ===")
        print("1. Input a word")
        print("2. Exit")

        choice = input("Enter your choice (1 or 2):")
                       
        if choice == "2":
            print("Goodbye!")
            break
            
        elif choice == "1":
            word = input("Enter a word:").strip()

            if not is_valid_input(word):
                continue
                
            if anagram_checker.is_valid_word(word):
                print(f"\nYour Word: \"{word.upper()}\"")
                print("This is a valid English word.")

                anagrams = anagram_checker.get_anagrams(word)
                if anagrams:
                    print(f"Anagrams for your word: {', '.join(anagrams)}.")
                else:
                    print("There are no anagrams for your word.")
            else:
                print(f"\nYour Word: \"{word.upper()}\"")
                print("This is not a valid English word.")
        
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()

    
            
        
            
