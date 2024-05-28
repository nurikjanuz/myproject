#https://docs.python.org/

# file = open('test.txt', mode='r+')
# print(dir(file))
# print(file.read())
# file.write("Hello World!")
# file.write("Hello World!")
# file.write("Hello World!")
# file.write("Hello World!")
# file.close()
# print(file.closed)


# file = open('test.txt', mode='r+')
# for i in range(1, 101):
#     file.write(f"{i}\n")
# print(file.readlines()[12])

# with open('test.txt', mode='a') as file:
#     for i in range(1,101):
#         file.write(f"{i}\n")
# print(file.closed)

with open('anketa.txt', 'a') as file:
    count_of_candidate = int(input("Nechta kandidat kiritamiz? "))
    for candidate_id in range(1, count_of_candidate+1):
        file.write(f"# №{candidate_id} \n")
        print(f"№ {candidate_id} ma'lumotlari")
        for data in ['Ismi', 'Yoshi', 'Qayerdanligi']:
            file.write(f"{data}: "+ input(f"{data}: ")+ "\n")
        experience = int(input(f"Ish staji: "))
        file.write(f"'Ish staji': {experience} \n")
        file.write('***************************\n\n')

        if experience<=2:
            print(f"Sizga yana aloqaga chiqamiz")