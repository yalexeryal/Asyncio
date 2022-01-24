import requests
import time


def get_person(person_id: int) -> dict:
    return requests.get(f"https://swapi.dev/api/people/{person_id}").json()


def main():
    persens_list = []
    for person_id in range(1, 11):
        person = get_person(person_id)
        print(person)
        persens_list.append(person)
        #print(persens_list)

stat = time.time()
main()
print(f"Время работы {time.time() - stat}")
