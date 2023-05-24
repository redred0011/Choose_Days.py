import datetime
import calendar

def choose_language():
    print("1 - Polish")
    print("2 - English")
    choose = input("Choose Language: ")
    
    if choose == "1":
        speak_polish()
    elif choose == "2":
        speak_english()
    else:
        print("Invalid choice")
    return(choose_language())

def translate_to_polish(day_name):
    translation = {
        'Monday': 'Poniedziałek',
        'Tuesday': 'Wtorek',
        'Wednesday': 'Środa',
        'Thursday': 'Czwartek',
        'Friday': 'Piątek',
        'Saturday': 'Sobota',
        'Sunday': 'Niedziela'
    }
    return translation.get(day_name, "Unknown")

def speak_polish():
    date_of_birth = input("Podaj datę urodzin w formacie (dzień-miesiąc-rok): ")
    day, month, year = date_of_birth.split("-")
    date_of_birth = datetime.datetime(int(year), int(month), int(day))
    day_name = calendar.day_name[date_of_birth.weekday()]
    print(translate_to_polish(day_name))

def speak_english():
    date_of_birth = input("Enter date of birth (day-month-year): ")
    day, month, year = date_of_birth.split("-")
    date_of_birth = datetime.datetime(int(year), int(month), int(day))
    day_name = calendar.day_name[date_of_birth.weekday()]
    print(day_name)

choose_language()

