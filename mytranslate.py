
#This dictionary (original dictionary) will be used for translations.
org_dict = {"name":"nom", "project":"projet", "newspaper":"journal", "trip":"voyage",
            "boss":"patron","very":"très","dad":"papa", "book":"livre", "bed":"lit", "cold":"froid","hot":"chaud",
            "hat":"chapeau","green":"vert", "red":"rouge", "blue":"bleu", "black":"noir", "purple":"violet",
            "white":"blanc", "wind":"vent", "favorite":"préféré","exam":"examen", "computer":"ordinateur",
            "happy":"content", "sad":"triste", "beautiful":"magnifique", "of":"du", "this":"ce", "with":"avec",
            "kid":"enfant", "skinny":"maigre", "fat":"gros", "i":"je", "of the":"du", "is":"est", "for":"pour", 
            "pencil":"crayon", "hello":"bonjour", "thanks":"merci", "sir":"monsieur", "professor":"professeur",
            "good":"bon", "perfect":"parfait", "my":"mon","big":"grand", "small":"petit", "homework":"devoirs",
            "student":"étudiant", "binder":"classeur", "also":"aussi","dictionary":"dictionnaire", "pen":"stylo",
            "the":"le", "closed":"fermé", "hotel":"hôtel", "am":"suis", "spanish":"espagnol", "married":"marié",
            "tall":"grand", "new":"nouveau", "work":"travaille", "read":"lis", "drink":"bois", 
            "go":"vais", "can":"peux", "do":"fais", "my":"mon", "to":"au", "one":"un", "Canada":"Canada",
            "Japan":"Japon", "Denmark":"Danemark", "Nigeria":"Nigéria", "a":"un"}



# this function reverses the original dictionary (from EtoF to FtoE).
def reverseDictionary(dictionary):
    # define a new dictionary
    FtoE_dict = {}
    # iterates through each item individually in the dictionary.
    for Eng, Fre in dictionary.items():
        # add french to english item to the new dictionary.
        FtoE_dict[Fre] = Eng
    return FtoE_dict


        
# this functions will simply translate each word based on the dictionary.
def translateWord(word, dictionary):
    # checks if the for is available in the dictionary
    if word in dictionary.keys() :
        return dictionary[word]
    # prints the word which is not available in the dictionary inside parenthesis.
    elif word != '' :
        return '(' + word + ')'
    return word

def translate(phrase, dicts, direction):
    UCletters=""
    # adding upercase letters to UCletters strings
    for c in range(65, 91): 
            UCletters+=chr(c)
    LCletters=""
    # adding lowercase letters to LCletters strings
    for c in range(97, 123): 
            LCletters+=chr(c)
    # adds up (merges) upercase and lowercase letters.
    letters = UCletters + LCletters
    # choose origial dictionary if directions is EtoF

    #splits the input phrase
    split_phrase = phrase.split()
    if direction == "E_to_F":
        dictionary = org_dict

        
    elif direction == "F_to_E":
        dictionary = reverseDictionary(org_dict)
        # when the english sentence hasn't been translated to french yet, this part 
        # doesn't let the program to translate "de" and "du" when it makes the translation wrong (by removing them).
        for i in split_phrase:
            if i == "du" or i == "de":
                split_phrase.remove(i)
        phrase = " ".join(split_phrase)
## main

    #converts the input to lower case
    phrase = phrase.lower()
    translation = ''
    word = ''
    
    for character in phrase :
        if character in letters :
            word += character
        else : 
            translation = translation + translateWord(word, dictionary) + character
            word = ''
    translation = translation + translateWord(word, dictionary)
    
    #additional changes after translation from english to french.
    if direction == "E_to_F":
        input_split = phrase.split()
        translated = translation.split()
        
        #for word in translated:
                #if word[0] in ['a','e','i','o','u','y','h','é']:
                    #word = 'l’'+word
                #translation = ' '.join(translated)



        # swaps the position of noun and color 
        eng_color =["green", "red", "blue", "black", "purple", "white"]      
        for word in input_split:
            if word in eng_color:
                selected_word = dictionary[word]
                current = translated.index(selected_word)
                translated[current], translated[current+1] = translated[current+1], translated[current]
                translation = ' '.join(translated)
    else:
        input_split = phrase.split()
        translated = translation.split()
        french_color = ["vert", "rouge", "bleu", "noir", "violet","blanc"]
        for word in input_split:
            # swaps the position of noun and color
            if word in french_color:
                selectedtwo = dictionary[word]
                current = translated.index(selectedtwo)
                translated[current-1], translated[current] = translated[current], translated[current+1]
                translation = ' '.join(translated)

        
        
    return translation
#where we write the inputs in order to be translated. If we want it to be translated from english to french after the second comma we write "E_to_F" 
# and when we want it to be translated from french to english after the second comma we write "F_to_E". the list of inputs are in eng_input and fr_input.
eng_input = ["my pen is very small","the book is purple!", "I am spanish.", "this black hat is beautiful.", "I am very sad.", "I read a blue book"]
# the program is supposed to put the word Sam in parenthesis because it's not in the dictionary.
fr_input = ["Je suis espagnol.", "Le professeur est grand.", "merci monsieur!", "Je lis le journal.", "mon nom est sam"]

for i in eng_input:
    print("Input:",i)
    print("Translation:",translate(i,org_dict,"E_to_F"))
    print("\n")

for i in fr_input:
    print("Input:",i)
    print("Translation:",translate(i,org_dict,"F_to_E"))
    print("\n")
   



