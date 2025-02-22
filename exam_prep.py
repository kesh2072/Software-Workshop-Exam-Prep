import csv
from datetime import datetime

def csv_to_dict(csv_file):
    """
    Reads from a csv file and returns a list of dictionaries
    Example output:
    [{'key1': 'smith1', 'key2': 'henry smith', 'key3': '22', 'key4': 'Birmingham'},
     {'key1': 'jones1', 'key2': 'miriam jones', 'key3': '30', 'key4': 'York'}]
    """
    keys = ["key1", "key2", "key3", "key4", "key5"] # Change key names accordingly
    list_of_dictionaries = []

    with open(csv_file, "r") as csv_file:
        file = csv.reader(csv_file, delimiter=";")
        for line in file:
            dictionary = {}
            for i, value in enumerate(line):
                dictionary.update({keys[i]: value})
            list_of_dictionaries.append(dictionary)

    return list_of_dictionaries

def csv_dict_reader(csv_file):
    """
    Same as csv_to_dict(), but using in-built DictReader method
    If the csv file has a header row, you can get rid of 'headers' and the fieldnames parameter in .DictReader(),
    and it functions the same
    Returns a list of dictionaries in this format:
    [{'id': 'smith1', 'name': 'henry smith', 'age': '22', 'location': 'Birmingham'},
    {'id': 'jones1', 'name': 'miriam jones', 'age': '30', 'location': 'York'}]
    """
    headers = ["id", "name", "age", "location"]
    list_of_dictionaries = []
    with open(csv_file, "r") as csv_file:
        file = csv.DictReader(csv_file, delimiter=";", fieldnames=headers)
        for row in file:
            list_of_dictionaries.append(row)

    return list_of_dictionaries


def dict_to_csv(csv_file):
    """
    Writes list of dictionaries into a csv file
    """
    list_of_dictionaries = csv_to_dict(csv_file)
    with open("../test.csv", "w") as csv_file:
        file = csv.writer(csv_file, delimiter=";")
        for dictionary in list_of_dictionaries:
            file.writerow(dictionary.values())
    return


def search_dict(list_of_dictionaries):
    """
    Function to retrieve a specific dictionary from a list of dictionaries
    It asks you for a value in the dictionary (for example, if the first pair in your dictionary is an id like
    {"username": "my_username", ...}, enter in "my_username" in the ID, and it searches through every dictionary
    and if it finds that username, prints out that specific dictionary.
    If no username (or other kind of value you're looking for) is found, it returns False
    """
    input_id = input("Input the ID for the dictionary whose information you want to retrieve: ")

    for dictionary in list_of_dictionaries:
        associated_value = dictionary.get("key1") # Change "key1" to the actual 'key' in your dictionary that you're searching for
        if associated_value == input_id:
            print(f"Here is the information requested: {dictionary}")
            return dictionary

    print("No one with that ID was found")
    return False

def generate_summary_of_csv_file(csv_file):
    """
    Reads a csv file and prints out all the items in a readable way
    :return:
    """
    with open(csv_file, "r") as csv_file:
        file = csv.reader(csv_file, delimiter=";")
        for row in file:
            for element in row:
                print(element)
    return

def generate_summary_of_dictionaries(list_of_dictionaries):
    for dictionary in list_of_dictionaries:
        for key, value in dictionary.items():
            print(f"Key: {key} - Value: {value}")
    return

def extract_nums_from_nested_dictionary():
    """
    Searches through either a dictionary where the value is a list of numbers, or where the value is a nested
    dictionary of which one of the key:value pairs contains a list of numbers
    :return:
    """
    student_grades_one = {"student1": [1, 2, 3], "student2": [4, 5, 6]}
    student_grades_two = {"student1": {"grades": [1, 2, 3], "attendace": 78},
                          "student2": {"grades": [4, 5, 6], "attendance": 95}}

    #user_input = input("Which student would you like to view? ")
    #print(student_grades_two[user_input])

    # Extract the list of grades and find the average for the specified student
    grade_average = 0
    grades = student_grades_two["student2"].get("grades")
    for grade in grades:
        print(grade)
        grade_average += grade
    grade_average /= len(student_grades_two["student2"]["grades"])
    print(grade_average)

def search_nested_dictionary():
    """
    Searches a dictionary with nested dictionaries, and unpacks the desired values
    :return:
    """
    nested_dictionaries = {"key1": {"nested_key1": "nested_value1"}, "key2": {"nested_key2": "nested_value2"}}
    print(nested_dictionaries.get("key1")) # Returns the nested dictionary key and value
    nested_dictionary = nested_dictionaries.get("key1")
    print(nested_dictionary.get("nested_key1")) # Returns the nested value
    return

def validate_datetime():
    """
    Gets the user to input a time in HH:MM:SS format (e.g. 09:30:00) then validates whether it was inputted correctly
    If it's not in valid datetime format, it prompts the user again to input it correctly
    Once it's validated, it returns itself in two objects: one as datetime and one as a string
    The datetime objects can be used in calculate_time_difference() to find the difference between two times
    The string object can be used to be written to a csv file
    """
    datetime_format = "%H:%M:%S"
    while True:
        user_time = str(input("Please input a time (HH:MM:SS): "))
        try:
            formatted_user_time_datetime = datetime.strptime(user_time, datetime_format)
            formatted_user_time_string = formatted_user_time_datetime.strftime(datetime_format)
            # If you only want to return a string, just 'return formatted_user_time_datetime.strftime(datetime_format)
            return formatted_user_time_datetime, formatted_user_time_string
        except ValueError:
            print("Please enter a time in the datetime format")


def calculate_time_difference(time_1, time_2):
    """
    Calculates the difference between two datetime objects (can't use strings)
    Returns the difference in hours and minutes (both as type integer)
    If we use this to track what time someone comes to work,
    time_1 (when they came to work) = 09:30:00
    time_2 (when they were supposed to come to work) = 08:00:00
    It would return that they came to work an hour and 30 minutes late
    If this was reversed, it would just return 0,0 and print that the user came to work early
    """
    if time_1 > time_2:
        time_difference = time_1 - time_2
        seconds = time_difference.seconds
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        return hours, minutes
    else:
        print("User came to work early")
        return 0, 0  # returns a default value otherwise it causes issues when you return None


def main():
    """
    Framework of a menu application that uses a 'while True' loop, and 'match case'
    :return:
    """
    while True:
        choice = int(input("What would you like to do? 1, 2, 3, 4, 5: "))
        match choice:
            case 1:
                continue # Insert functions etc here
            case 2:
                continue
            case 3:
                continue
            case 4:
                continue
            case 5:
                print("Program exited")
                exit()
            case _:
                print("Please enter a valid input")
                continue
