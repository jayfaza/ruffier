def ruffier_index(P1, P2, P3):
    ''' возвращает значение индекса по трем показателям пульса для сверки с таблицей'''
    return (4 * (P1 + P2 + P3) - 200) / 10

def neud_level(age):
    ''' варианты с возрастом меньше 7 и взрослым надо обрабатывать отдельно, 
    здесь подбираем уровень "неуд" только внутри таблицы:
    в возрасте 7 лет "неуд" - это индекс 21, дальше каждые 2 года он понижается на 1.5 до значения 15 в 15-16 лет '''
    return 21 + int((7 - age) // 2) * 1.5 
    pass

def low_level(age):
    return (17 + int((7 - age) / 2) * 1.5, 21 + int((7 - age) / 2) * 1.5)

def medium_level(age):
    return (12 + int(7 - age) / 2) * 1.5, 17 + int((7 - age) / 2) * 1.5

def good_level(age):
    return (6.5 + int((7 - age) / 2) * 1.5, 12 + int((7 - age) / 2) * 1.5)

def ideal_level(age):
    return 6.5 + int((7 - age) / 2) * 1.5

    
def ruffier_result(r_index, age):
    ''' функция получает индекс Руфье и интерпретирует его, 
    возвращает уровень готовности: число от 0 до 4
    (чем выше уровень готовности, тем лучше).  '''

    if r_index >= neud_level(age):
        # return f"{txt_index}{r_index}\n{txt_workheart}\n{txt_res[0]}"
        return 0
    
    if r_index >= low_level(age)[0] and r_index < low_level(age)[1]:
        # return f"{txt_index}{r_index}\n{txt_workheart}\n{txt_res[1]}"
        return 1

    if r_index >= medium_level(age)[0] and r_index < medium_level(age)[1]:
        return 2

    if r_index >= good_level(age)[0] and r_index < good_level(age)[1]:
        return 3

    if r_index <= ideal_level(age):
        return 4

if __name__ == "__main__":
    r_index = 0.0
    age = 0
    tests_done = 0
    ideal_tests = 0
    while True:
        while r_index < 100.0:
            print(f"Возраст: {age}, Индекс: {r_index}, Оценка: {ruffier_result(r_index, age)}")
            r_index += 0.01
            tests_done += 1
        r_index = 0.0
        age += 1
        if age == 100:
            break

    print(f"Sucsess! tests done: {tests_done}")


