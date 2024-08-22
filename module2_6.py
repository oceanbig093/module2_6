calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())

def is_contains(string, list_to_search):
    count_calls()
    string = string.lower()
    for item in list_to_search:
        if string == item.lower():
            return True
    return False

result1 = string_info("Education")
print(result1)

result2 = string_info("Concentration")
print(result2)

result3 = is_contains("Urban", ["UrbAN", "flower", "urban"])
print(result3)

result4 = is_contains("University", ["School", "univercity", "college"])
print(result4)

print(calls)