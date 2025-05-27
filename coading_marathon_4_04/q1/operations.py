def convert_uppercase(data:list[str]):
    new_data=[value.upper() for value in data]
    return new_data

def convert_lowercase(data:list[str]):
    new_data=[value.lower() for value in data]
    return new_data

def remove_vowels(data:list[str]):
    s=""
    new_data=[s.join(filter(lambda x:x not in "AEIOUaeiou",value)) for value in data]
    return new_data

def remove_special_characters(data:list[str]):
    s=""
    new_data=[s.join(filter(lambda x:x not in "!@#$%^&*()",value)) for value in data]
    return new_data

def count_string_length(data:list[str]):
    new_data=[len(value) for value in data ]
    return new_data

