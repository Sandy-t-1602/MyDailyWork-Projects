import random

def quiz_db():

    global questions

    questions = [ {"question" : "What is the capital city of India?", "options" : ["A) Mumbai", "B) Kolkata", "C) New Delhi", "D) Chennai"], "answer" : "C"},
                  {"question" : "Which river is considered the lifeline of India?", "options" : ["A) Yamuna", "B) Ganges", "C) Godavari", "D) Brahmaputra"], "answer" : "B"},
                  {"question" : "Who was the first Prime Minister of India?", "options" : ["A) Mahatma Gandhi", "B) Jawaharlal Nehru", "C) Indira Gandhi", "D) Rajendra Prasad"], "answer" : "B"},
                  {"question" : "Which famous monument in India was built by Emperor Shah Jahan?", "options" : ["A) Qutub Minar", "B) Red Fort", "C) Taj Mahal", "D) Humayun’s Tomb"], "answer" : "C"},
                  {"question" : "What is the national flower of India?", "options" : ["A) Rose", "B) Sunflower", "C) Lotus", "D) Jasmine"], "answer" : "C"},
                  {"question" : "Which festival is known as the “Festival of Lights” in India?", "options" : ["A) Holi", "B) Diwali", "C) Navratri", "D) Durga Puja"], "answer" : "B"},
                  {"question" : "The Indian national flag has three colors – saffron, white, and green. What do these colors represent?", "options" : ["A) Courage, peace, and fertility", "B) Sacrifice, purity, and prosperity", "C) Love, purity, and growth", "D) Power, truth, and harmony"], "answer" : "B"},
                  {"question" : "Which Indian state is famous for its backwaters and houseboats?", "options" : ["A) Goa", "B) Kerala", "C) Rajasthan", "D) Tamil Nadu"], "answer" : "B"},
                  {"question" : "Who is known as the “Father of the Indian Constitution”?", "options" : ["A) Mahatma Gandhi", "B) B. R. Ambedkar", "C) Jawaharlal Nehru", "D) Sardar Vallabhbhai Patel"], "answer" : "B"},
                  {"question" : "The Indian film industry based in Mumbai is popularly known as what?", "options" : ["A) Hollywood", "B) Tollywood", "C) Bollywood", "D) Nollywood"], "answer" : "C"},
                  {"question" : "Which Indian city is also known as the “Pink City”?", "options" : ["A) Jaipur", "B) Jodhpur", "C) Udaipur", "D) Bikaner"], "answer" : "A"},
                  {"question" : "What is the national game of India?", "options" : ["A) Cricket", "B) Field Hockey", "C) Football (Soccer)", "D) Badminton"], "answer" : "B"},
                  {"question" : "Who was the leader of the Indian independence movement and inspired the philosophy of non-violence (ahimsa)?", "options": ["A) Subhas Chandra Bose", "B) Bhagat Singh", "C) Mahatma Gandhi", "D) Jawaharlal Nehru"], "answer" : "C"},
                  {"question" : "What is India’s largest city by population?", "options" : ["A) Mumbai", "B) Delhi", "C) Bangalore", "D) Kolkata"], "answer" : "A"},
                  {"question" : "Which river flows through the city of Varanasi, a major religious hub in India?", "options" : ["A) Yamuna", "B) Ganges", "C) Brahmaputra", "D) Narmada"], "answer" : "B"},
                  {"question" : "What is the currency of India?", "options" : ["A) Rupee", "B) Yen", "C) Rupiah", "D) Euro"], "answer" : "A"},
                  {"question" : "India shares its borders with how many countries?", "options" : ["A) 5", "B) 6", "C) 7", "D) 8"], "answer" : "C"},
                  {"question" : "Which Indian state is known as the “Land of Five Rivers”?", "options" : ["A) Punjab", "B) Haryana", "C) Uttar Pradesh", "D) Bihar"], "answer" : "A"},
                  {"question" : "Who wrote the Indian national anthem?", "options" : ["A) Rabindranath Tagore", "B) Bankim Chandra Chatterjee", "C) Sarojini Naidu", "D) Subhas Chandra Bose"], "answer" : "A"},
                  {"question" : "Which Indian state is the largest by area?", "options" : ["A) Maharashtra", "B) Madhya Pradesh", "C) Rajasthan", "D) Uttar Pradesh"], "answer" : "C"},
                  {"question" : "What is the official language of the Indian state of Tamil Nadu?", "options" : ["A) Telugu", "B) Kannada", "C) Malayalam", "D) Tamil"], "answer" : "D"},
                  {"question" : "Which Indian state is known for the dance form Kathakali?", "options" : ["A) Kerala", "B) Karnataka", "C) Tamil Nadu", "D) Andhra Pradesh"], "answer" : "A"},
                  {"question" : "Who was the first President of India?", "options" : ["A) Rajendra Prasad", "B) S. Radhakrishnan", "C) Zakir Husain", "D) V. V. Giri"], "answer" : "A"},
                  {"question" : "Which Indian state is known as the “Spice Garden of India”?", "options" : ["A) Kerala", "B) Karnataka", "C) Tamil Nadu", "D) Andhra Pradesh"], "answer" : "A"},
                  {"question" : "What is the national animal of India?", "options" : ["A) Lion", "B) Elephant", "C) Tiger", "D) Peacock"], "answer" : "C"},
                  {"question" : "Which Indian state is famous for the festival of Bihu?", "options": ["A) Assam", "B) West Bengal", "C) Odisha", "D) Bihar"], "answer" : "A"},
                  {"question" : "Who is known as the “Iron Man of India”?", "options": ["A) Jawaharlal Nehru", "B) Sardar Vallabhbhai Patel", "C) Subhas Chandra Bose", "D) Bhagat Singh"], "answer" : "B"},
                  {"question" : "Which Indian state has the longest coastline?", "options": ["A) Maharashtra", "B) Tamil Nadu", "C) Gujarat", "D) Andhra Pradesh"], "answer" : "C"},
                  {"question" : "What is the national fruit of India?", "options": ["A) Apple", "B) Banana", "C) Mango", "D) Orange"], "answer" : "C"},
                  {"question" : "Which Indian state is known for the dance form Bharatanatyam?", "options": ["A) Kerala", "B) Karnataka", "C) Tamil Nadu", "D) Andhra Pradesh"], "answer" : "C"},
                  {"question" : "Who was the first woman Prime Minister of India?", "options": ["A) Indira Gandhi", "B) Pratibha Patil", "C) Sarojini Naidu", "D) Sushma Swaraj"], "answer" : "A"},
                  {"question" : "Which Indian state is known as the “Land of Rising Sun”?", "options": ["A) Arunachal Pradesh", "B) Assam", "C) Sikkim", "D) Nagaland"], "answer" : "A"},
                  {"question" : "What is the national bird of India?", "options": ["A) Peacock", "B) Sparrow", "C) Eagle", "D) Parrot"], "answer" : "A"},
                  {"question" : "Which Indian state is known for the festival of Pongal?", "options": ["A) Kerala", "B) Karnataka", "C) Tamil Nadu", "D) Andhra Pradesh"], "answer" : "C"},
                  {"question" : "Who is known as the “Missile Man of India”?", "options": ["A) Homi J. Bhabha", "B) Vikram Sarabhai", "C) A. P. J. Abdul Kalam", "D) Satish Dhawan"], "answer" : "C"},
                  {"question" : "Which Indian state is known for the dance form Kuchipudi?", "options": ["A) Kerala", "B) Karnataka", "C) Tamil Nadu", "D) Andhra Pradesh"], "answer" : "D"},
                  {"question" : "What is the national tree of India?", "options": ["A) Neem", "B) Banyan", "C) Peepal", "D) Mango"], "answer" : "B"},
                  {"question" : "Which Indian state is known for the festival of Onam?", "options": ["A) Tamil Nadu", "B) Karnataka", "C) Kerala", "D) Andhra Pradesh"], "answer" : "C"},
                  {"question" : "Who is known as the “Nightingale of India”?", "options": ["A) Lata Mangeshkar", "B) Sarojini Naidu", "C) Indira Gandhi", "D) M. S. Subbulakshmi"], "answer" : "B"},
                  {"question" : "Which Indian state is known for the dance form Odissi?", "options": ["A) West Bengal", "B) Odisha", "C) Bihar", "D) Jharkhand"], "answer" : "B"},
                  {"question" : "What is the national aquatic animal of India?", "options": ["A) Ganges River Dolphin", "B) Saltwater Crocodile", "C) Olive Ridley Turtle", "D) Dugong"], "answer" : "A"},
                  {"question" : "Which Indian state is known for the festival of Durga Puja?", "options": ["A) West Bengal", "B) Assam", "C) Odisha", "D) Bihar"], "answer" : "A"},
                  {"question" : "Who was the first Indian woman to win a Nobel Prize?", "options": ["A) Indira Gandhi", "B) Mother Teresa", "C) Sarojini Naidu", "D) Amartya Sen"], "answer" : "B"},
                  {"question" : "Which Indian state is known for the dance form Manipuri?", "options": ["A) Manipur", "B) Assam", "C) Tripura", "D) Meghalaya"], "answer" : "A"},
                  {"question" : "What is the national reptile of India?", "options": ["A) King Cobra", "B) Indian Python", "C) Monitor Lizard", "D) Gharial"], "answer" : "A"},
                  {"question" : "Which Indian state is known for the festival of Makar Sankranti?", "options": ["A) Gujarat", "B) Maharashtra", "C) Karnataka", "D) All of the above"], "answer" : "D"},
                  {"question" : "Who is known as the “Flying Sikh of India”?", "options": ["A) Milkha Singh", "B) P. T. Usha", "C) Sachin Tendulkar", "D) Kapil Dev"], "answer" : "A"},
                  {"question" : "Which Indian state is known for the dance form Mohiniyattam?", "options": ["A) Kerala", "B) Karnataka", "C) Tamil Nadu", "D) Andhra Pradesh"], "answer" : "A"},
                  {"question" : "What is the national heritage animal of India?", "options": ["A) Indian Elephant", "B) Bengal Tiger", "C) Asiatic Lion", "D) Indian Rhino"], "answer" : "A"},
                  {"question" : "Which Indian state is known for the festival of Ganesh Chaturthi?", "options": ["A) Maharashtra", "B) Gujarat", "C) Karnataka", "D) Tamil Nadu"], "answer" : "A"}]

def start_prog():

    print("************************")
    print("Quiz Program")
    print("************************")
    print("Version : 1.0")
    print("************************")
    print("Made by Santhosh T")
    print("************************")

    print("")

    SelectedQuestions = random.sample(questions, 10)

    score = 0

    for index, ques in enumerate(SelectedQuestions):
        print("Q", index+1, ":", ques['question'], "\n")
        for opt in ques['options']:
            print(opt)
        print("")
        ans = input("Enter the option: ").strip().upper()
        if ans == ques['answer']:
            score += 1
            print("\nCorrect Answer...!")
            print("")
        else:
            print("\nWrong Answer...!\n\nThe Correct Option is ", ques['answer'])
            print("")

    print("Your Overall Score is", score, "out of 10.")
    exit_prog()

def exit_prog():
    print("")
    AskAgain = str(input("Do you want to start over? (Y/N): "))
    UppercaseAA = AskAgain.upper()
    
    if UppercaseAA == 'Y':
        print("")
        print("Restarting the Quiz Program...\n")
        start_prog()
    elif UppercaseAA == 'N':
        print("\nApplication is Closed...!")
    else:
        print("\nWRONG INPUT!! PLEASE TRY AGAIN!!")
        exit_prog()

quiz_db()
start_prog()
