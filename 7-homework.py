import json

# with open('anketa2.json', 'r+') as file:
#     candidates =[]
#     count_of_candidate = int(input("Nechta kandidat kiritamiz? "))
#     for candidate_id in range(1, count_of_candidate+1):
#         print(f"№ {candidate_id} ma'lumotlari")
#         ismi = input("Ismi: ")
#         yoshi = input("Yoshi: ")
#         qayerdan = input("Qayerdanligi: ")
#
#         current_candidate = {
#             'id': candidate_id,
#             'name': ismi,
#             'age': yoshi,
#             'place': qayerdan
#         }
#         candidates.append(current_candidate)
#     candidates_json = json.dumps(candidates, indent=4)
#     file.write(candidates_json)

with open('anketa2.json', 'r') as file:
    candidates = json.load(file)
    for candidate in candidates:
       print(f"{candidate['name']},{candidate['age']} yoshda, {candidate['place']}dan")

    print(f"Anketa bo'yicha {len(candidates)}ta nomzod qiziqish bildirdi")
    for candidate in candidates:
        if 18 > int(candidate['age']) > 29:
            print(f"{candidate['name']},{candidate['age']} yoshda, {candidate['place']}dan")
    for candidate in candidates:
        if candidate['place'] !='Buxoro':
            print(f"{candidate['name']},{candidate['age']} yoshda, {candidate['place']}dan")