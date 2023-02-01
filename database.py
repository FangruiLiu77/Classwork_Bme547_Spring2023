#database

def create_patient_entry(patient_name, patient_mrn, patient_age):
    new_patient = [patient_name, patient_mrn, patient_age,[]]
    return new_patient

def main_driver():
    db= []
    db.append(create_patient_entry("Ann Ables", 1, 34))
    db.append(create_patient_entry("Bob Boyles", 2, 45))
    db.append(create_patient_entry("Chris Chou", 3, 52))
    print(db)
    add_test_to_patient(db, 1, "HDL", 120)
    add_test_to_patient(db, 2, "LDL", 100)
    add_test_to_patient(db, 2, "HDL", 99)
    room_numbers = ["103", "232", "333"]
    print(db)
    print_directory(db, room_numbers)
    get_test_value(db, 2, "LDL")

def print_directory(db, room_numbers):
    for i, patient in enumerate(db):
        print("Patient {} is in room {}".format(patient[0], room_numbers[i]))
    for patient, rn in zip(db,room_numbers):
        print("Patient {} is in room {}".format(patient[0], rn))

def get_test_value(db, mrn_to_find, test_name):
    for patient in db:
        if patient[1] == mrn_to_find:
            for test in patient[3]:
                if test[0] == test_name:
                    print("The {} value of {} is {}".format(test_name, patient[0], test[1]))
                else:
                    continue


def get_patient_entry(mrn_to_find, db):
    for patient in db:
        if patient[1] == mrn_to_find:
            return patient
    return False

def add_test_to_patient(db, mrn_to_find, test_name, test_value):
    patient = get_patient_entry(mrn_to_find, db)
    if patient == False:
        print("Bad entry")
    else:
        patient[3].append([test_name, test_value])

if __name__ == "__main__":
    main_driver()