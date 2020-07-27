from hashlib import md5


def generator_md5(file):
    with open(file, encoding='utf-8') as fo:
        for line in fo:
            cropped_line = line.strip()
            if cropped_line:
                yield md5(cropped_line.encode()).hexdigest()
            else:
                fo.readline()


for line in generator_md5('test.txt'):
    print(line)
