# Medical priority system

people = [{
    "name": "John",
    "condition": "Critical"
},
{
    "name": "Liam",
    "condition": "Somewhat"
},
{
    "name": "Alice",
    "condition": "Very Low"
},
{
    "name": "Bob",
    "condition": "Low"
}]

{"name": "priority"}

priorityOrder = {
    "Critical": 0,
    "Somewhat": 1,
    "Low": 2,
    "Very Low": 3
}

treatedPatient = "{} was treated with condition of {}"


def treatPatients():
    priorityQueue = sorted(people, key=lambda patient: priorityOrder[patient["condition"]])
    for patient in priorityQueue:
        print(treatedPatient.format(*patient.values()))
    # and then... the garbage collector struck!
    # and the list technically counts as exhausted. It's not "removing from
    # the ADT" but it's pretty

treatPatients()
