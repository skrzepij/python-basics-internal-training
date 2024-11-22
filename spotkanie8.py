# zaimportuj moduł obliczenia.py
from xml.etree.ElementTree import indent

import modul.obliczenia as obliczenia
from modul.obliczenia import * # importuje wszystko z modulu obliczenia

print(obliczenia.dodaj(2, 3)) # 5
print(dodaj(2, 3))  # 5

## INTEGRACJA Z API ATLASSIAN JIRA
from atlassian import Jira
from modul.token import jira_token
import json

jira_tst = Jira(url = 'https://jira-test.coi.gov.pl', token = jira_token)
projects = jira_tst.projects()

# print(projects)

## Zapisanie do pliku - dane w formacie JSON
json.dump(projects, open("projects.json", "wt", encoding='utf-8'), indent=4) # zapisanie do pliku - dane w formacie JSON - indent - wciecia
# wez tylko 10 projektow i wyswietl
for project in projects[:10]:
    print(project["key"], project["name"])

## Odczytanie konkretnego zadania
zadanie = jira_tst.issue('SWC-1505')
json.dump(zadanie, open("zadanie.json", "wt", encoding='utf-8'), indent=4) # zapisanie do pliku - dane w formacie JSON - indent - wciecia

## Wyswietlenie nazwy i opisu zadania
print(zadanie["fields"]["summary"])
wynik = jira_tst.jql('project = SWC AND status = "In Progress"')
print([x["key"] for x in wynik["issues"]])

## Dodanie komentarza do zadania
# jira_tst.issue_add_comment('SWC-1505', 'To jest komentarz dodany przez API')
print(jira_tst.issue_get_comments('SWC-1505'))

## TRY - EXCEPT - obsluga bledow
try:
    print(1)
    print(1/0)
    print(2)
except Exception as e: # Exception - klasy bazowej dla wszystkich wyjatkow
    print(e)
    print("Blad")
else:
    print("OK")
finally:
    print("Koniec")