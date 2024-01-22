import os


def combining_files(list):
    line_count_files = {}
    for f in list:
        name = f
        file_path = os.path.join(os.getcwd(), 'task_3', f)
        with open(file_path) as file:
            data = file.read()
            line_count = data.count('\n') + 1
            line_count_files[name] = {'Count_lines': line_count, 'Data': data}
    line_count_files = dict(sorted(line_count_files.items(), key=lambda x: x[1]['Count_lines']))
    return line_count_files


def writing_to_new_file(dictionary):
    with open('new_file.txt', 'w') as new_file:
        for name, d in dictionary.items():
            new_file.write(name + "\n")
            new_file.write(str(d['Count_lines']) + "\n")
            new_file.write(d['Data'] + "\n")
    return "Запись прошла успешно!"


d = combining_files(['1.txt', '2.txt', '3.txt'])
print(writing_to_new_file(d))




