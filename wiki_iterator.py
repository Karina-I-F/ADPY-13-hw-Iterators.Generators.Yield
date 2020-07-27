import json

URL = 'https://en.wikipedia.org/wiki/'


def get_country(json_file):
    with open(json_file, encoding='utf-8') as file:
        data = json.load(file)
        country_list = []
        for item in data:
            country_list.append(item['name']['common'])
    return country_list


class WikiIterator:
    def __init__(self, list, file):
        self.list = list
        self.file = file
        self.count = 0
        self.limit = len(list)

    def __iter__(self):
        return self

    def __next__(self):
        index = self.count
        self.count += 1
        if self.count < self.limit:
            with open(self.file, 'a', encoding='utf8') as file:
                file.write(f'{self.list[index]}: {URL + self.list[index]}\n')
        else:
            raise StopIteration
        return self.list[index]


for country in WikiIterator(get_country('countries.json'), 'result.txt'):
    print(f'Найдена страница из Википедии для {country}')
