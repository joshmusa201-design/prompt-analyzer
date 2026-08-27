# VERSION OF THE PROMPT ANALYZER, TRYING TO TRAIN IT ON SOME WORDS THAT IS IT SEES IT JUDGES THE USER PROMPT. WITHOUT A MODEL

print("Enter your prompt")
user_prompt = input("").lower()
count = 1
split_1 = user_prompt.split(" ")
split_2 = user_prompt.split(".")



#v1, getting the word counts so i can use it to analyze the prompt
def get_user_word_count():
    me = len(user_prompt)
    print("Character count:", me)
    okay = len(split_1)
    print ("Word count:", okay)
    if split_1:
        print ("Sentence count:", len(split_2))

# GETTING THE NUMBERS OF WORDS IN THE PROMPT
def length():
    if len(split_1) > 10:
        strong = "Strong"
        return strong
    elif len(split_1) <= 10:
        weak = "Weak"
        return weak

length_word = length()



# GIVING IT WORDS THAT IS IT SEE IN A USER PROMPT THE GOAL IS DETECTED ELSE ITS NOT DETECTED
def prompt_analyzer(user_prompt):
    words = [ "build", "write", "explain", "analyze", "calculate", "generate", "create", "enumurate"]

    global_value = True

    for boss in words:
        
        if boss in split_1:
            me = "Goal: ✅ Detected"
            global_value == True
            return me

    if  not boss in split_1:
        goal = "Goal: ❌ Not detected"
        return goal

analyzer = prompt_analyzer(user_prompt)

 # IF 7 AND BEYOND WORDS IN THE PHRASES ARE FOUND IN THE USER PROMT, CONTEXT = DETECTED ELSE NOT DETECTED
def context_rules():
    phrases = ["i", "am", "i'm", "need", "want", "building", "working", "on", "creating", "developing", "for", "my",
    " a", "the", "because", "so", "that", "this", "is", "project", "user", "business", "company", "school"]
                    # IF AT LEAST 7 CONTEXT SIGNALS ARE DETECTED → CONTEXT = USEFUL.

    word_count = []
    for phrase in phrases:
        me = phrase in split_1
        if me:
            word_count.append(me)

            if len(word_count) >= 7:
                return "Context: ✅ detected"
                

    else:
        #print (analyzer)
        return "Context: ❌ Insufficient"

context = context_rules()
# PRINTING OUT THE SCORES FOR GOAL, CONTEXT AND SPECIFICITY/100 AND RUNNING ALL THE POSSIBLE OUTCOME THAT COULD HAPPEN
def calculate_score():

    score = 30
    num = 30
    non = 0
    specify = 40
    if analyzer == "Goal: ✅ Detected" :
        print(f"Goal: ✅ → {score} score ")
    elif analyzer == "Goal: ❌ Not detected":
        print(f"Goal: ❌ → {non} score")
    if context == "Context: ✅ detected" :
        print(f"Context: ✅ → {num} score")
    elif context ==  "Context: ❌ Insufficient":
        print(f"Context:❌ → {non} score")
    if length_word == "Strong":
        print(f"Specificity: ✅ → {specify} score")
    elif length_word == "Weak":
        print(f"Specificity: ❌ → {non} score")
    print("=========================")
    if analyzer == "Goal: ✅ Detected" and context == "Context: ✅ detected" and length_word == "Strong":
        print(f"Total → {score + num + specify}/100")
    elif analyzer == "Goal: ❌ Not detected" and context ==  "Context: ❌ Insufficient" and length_word == "Weak":
        print(f"Total → {non}/100")
    elif analyzer == "Goal: ✅ Detected" and length_word == "Strong" and context ==  "Context: ❌ Insufficient":
        print(f"Total → {score + specify}/100") 
    elif analyzer == "Goal: ❌ Not detected" and context == "Context: ✅ detected" and length_word == "Strong":
        print(f"Total → {specify + num}/100") 
    elif analyzer == "Goal: ✅ Detected" and context == "Context: ✅ detected" and length_word == "Weak":
        print(f"Total → {score + num}/100")
    elif analyzer == "Goal: ✅ Detected" and context ==  "Context: ❌ Insufficient" and length_word == "Weak":
        print(f"Total → {specify}/100")
    elif analyzer == "Goal: ❌ Not detected" and context == "Context: ✅ detected" and length_word == "Weak":
        print(f"Total → {num}/100")
    elif analyzer == "Goal: ❌ Not detected" and context ==  "Context: ❌ Insufficient" and length_word == "Strong":
        print(f"Total → {specify}/100")
calculate_score()