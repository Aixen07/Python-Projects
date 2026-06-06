questions = [
    ["Who is Shah Rukh Khan?", "WWE Wrestler", "Plumber", "Actor", "Astronaut", 3],
    ["What is the capital of France?", "Berlin", "Paris", "Rome", "London", 2],
    ["Which planet is known as the Red Planet?", "Earth", "Venus", "Mars", "Jupiter", 3],
    ["What is the largest mammal?", "Shark", "Blue Whale", "Elephant", "Giraffe", 2],
    ["Who wrote 'Romeo and Juliet'?", "William Shakespeare", "Jane Austen", "Charles Dickens", "Homer", 1],
    ["What is the square root of 64?", "8", "10", "6", "12", 1],
    ["Which country is known as the Land of the Rising Sun?", "India", "South Korea", "Japan", "China", 3],
    ["Who painted the Mona Lisa?", "Claude Monet", "Pablo Picasso", "Leonardo da Vinci", "Vincent van Gogh", 3],
    ["What is the fastest land animal?", "Horse", "Lion", "Cheetah", "Elephant", 3],
    ["Which ocean is the largest?", "Indian Ocean", "Pacific Ocean", "Atlantic Ocean", "Arctic Ocean", 2],
    ["What is the smallest country in the world?", "San Marino", "Vatican City", "Monaco", "Liechtenstein", 2]
]

prizes = [100000, 320000, 400000, 450000,  500000, 1000000, 2000000, 3000000, 4000000, 5000000, 6000000]
money = 0
i=0
try:
    for question in questions:
        print(question[0])
        print(f"Option A) {question[1]}")
        print(f"Option B) {question[2]}")
        print(f"Option C) {question[3]}")
        print(f"Option D) {question[4]}")

        a = int(input("Enter your Choice:1 for A 2 for B 3 for C 4 for D:\n"))
        if question[5]==a:
            print("Correct Answer!")
            money += prizes[i]
            print(f"You Have Won {money}")
            i=i+1
        else: 
            print(f"Sorry, You Have Not Answered the Question Correctly!, The Correct Answer was {question[5]}")
            print(f"Bad Luck!, you won {money}")
            break
except ValueError:
    print("Hey, Select a Valid Option!")
    
    
   

    