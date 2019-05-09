import program

db_1 = ['012031204121', 'abcdieerf', '120.48124']
db_2 = [380675674432, 380672832500, 380983567721]
db_3 = [380675674432, 380675674432, 380675674432,
        380675674432, 380675674432, 380675674432,
        380675674432, 380675674432, 380675674432,
        380675674432, 380675674432, 380675674242]
db_4 = [124.14, 0.124, 1827491.12, '11111111111']
db_5 = [365461896714, 382503376626, 375735953852,
        399788173510, 383414087535, 377265077922,
        377870325495, 304715520250, 350157669823,
        364310132367, 399966722194, 340354237873,
        389385394474, 386786703468, 376501480956,
        356399915032, 331267978404, 399095332093,
        309004384810, 305436093422]


def test_get_numbers_empty():
    answer = program.get_numbers()
    assert answer == "invalid database or input value"


def test_get_numbers_second_argument():
    answer = program.get_numbers(db_5)
    assert answer == "invalid database or input value"


def test_get_numbers_first_argument():
    answer = program.get_numbers(1)
    assert answer == "invalid database or input value"


def test_get_numbers1():
    answer = program.get_numbers(380675, db_1)
    assert answer == []


def test_get_numbers2():
    answer = program.get_numbers('380675', db_2)
    assert answer == [380675674432]


def test_get_numbers3():
    answer = program.get_numbers(38067567, db_3)
    assert answer == [380675674432, 380675674432, 380675674432, 380675674432,
                      380675674432, 380675674432, 380675674432, 380675674432,
                      380675674432, 380675674432]


def test_get_numbers4():
    answer = program.get_numbers(1, db_4)
    assert answer == []


def test_get_numbets5():
    answer = program.get_numbers(399, db_5)
    assert answer == [399788173510, 399966722194, 399095332093]