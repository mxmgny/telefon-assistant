
def get_numbers(num: int = None, phone_data_base: list = None):
    if num is None or not phone_data_base:
        return "invalid database or input value"
    answer = []
    for number in phone_data_base:
        if str(number).startswith(str(num)) and len(answer) < 10 and type(number) is int:
            answer.append(number)
    return answer
