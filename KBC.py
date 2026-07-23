print("-----welcome to kbc-----".upper())
player = input("your name: ").strip().lower()
print(f"okay so {player} lets start the game!!!")

question = [
    {
        "question": "What is the capital city of Rajasthan?",
        "options": ["a) bhilwara", "b) chittorgarh", "c) jaipur", "d) jodhpur"],
        "answer": "c",
        "prize": 5000,
        "50-50": "c) jaipur\nd) jodhpur",
        "safe_haven": False
    },
    {
        "question": "Who was the first woman to go into the Mariana Trench?",
        "options": ["a) Sally Ride", "b) Kathryn D. Sullivan", "c) Svetlana Savitskaya", "d) Valentina Tereshkova"],
        "answer": "b",
        "prize": 10000,
        "50-50": "a) Sally Ride\nb) Kathryn D. Sullivan",
        "safe_haven": False
    },
    {
        "question": "Where in Singapore did Netaji Subhash Chandra Bose make the first proclamation of an Azad Hind government?",
        "options": ["A) HMS Minden", "B) HMS Cornwallis", "C) HMS Trincomalee", "D) HMS Meanee"],
        "answer": "c",
        "prize": 15000,
        "50-50": "C) HMS Trincomalee\nA) HMS Minden",
        "safe_haven": True
    },
    {
        "question": "Milinda-Panha is a dialogue between King Menander (Milinda) and which Buddhist monk?",
        "options": ["A) Asanga", "B) Nagasena", "C) Mahadharmarakshita", "D) Dharmaraksita"],
        "answer": "b",
        "prize": 20000,
        "50-50": "B) Nagasena\nA) Asanga",
        "safe_haven": False
    },
]

total_amount = 0
safe_haven = 0
lifeline = True

for q in question:
    print("_"*40)
   
    if q == question[-1]:
        print("now, this is your final question!")
    print()
    print(f"for{q['prize']} : {q['question']}")
    print(f"your options are: ")
    for opt in q["options"]:
        print(opt)
    print()
    print("choose from option: a, b, c, d | quit to walk away | 50-50 lifeline")

    user_choice = input("your choice: ").strip().lower()
    if user_choice == "quit":
        print(f"you can leave, you won {total_amount}")
        break
    if user_choice == "lifeline":
        if lifeline:
            lifeline = False
            print("2 wrong options are removed")
            print("new options are: ")
            print(f"{q['50-50']}")
            user_choice = input("\nNow select your answer: ").strip().lower()
        else:
            print("You have already used your lifeline!")
            user_choice = input("Select your answer: ").strip().lower()

    if user_choice == q["answer"]:
        total_amount += q["prize"]
        print(f"you have won: {total_amount}")

        if q["safe_haven"]:
            safe_haven = q["prize"]
            print(f"safe haven reached! {safe_haven} is guaranteed")
    else:
        print(f"\nWrong answer! Game Over.")
        total_amount = safe_haven
        print(f"You drop down to your Safe Haven amount: ₹{safe_haven}")
        print("_"*40)
        break

print(f"thanks for playing kbc {player}, your total earning is: {total_amount}")
