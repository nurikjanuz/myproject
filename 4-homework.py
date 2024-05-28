questions = [
    {
        'question_text': "O'zbekiston poytaxtini aniqlang?",
        'answers':{
            'a': 'Samarqand',
            'b': 'Toshkent',
            'c': 'Buxoro'
        },
        'true_answer':'b'
    },
    {
        'question_text': "O'zbekiston mustaqil bo'lgan yilni aniqlang?",
        'answers': {
            'a': '1992',
            'b': '1990',
            'c': '1991'
        },
        'true_answer': 'c'
    }
]
print('Testni yechish')
count_of_correct_answers = 0
for question in questions:
    print(f"Savol: {question['question_text']}")
    for answer in question['answers'].items():
        print(f"{answer[0]}) {answer[1]}")
    user_answer = input('Javoni belgilang: ')
    if question['true_answer'] == user_answer:
        print("to'g'ri")
        count_of_correct_answers+=1
    else:
        print("noto'g'ri")

print(f"{len(questions)} savoldan {count_of_correct_answers}tasiga to'g'ri javob berdingiz")