#Script to manage the functions
def getTipPerson(bill,tip,people):
    tipInDollars = float(bill*(tip/100)/people)
    print('TIP: $', round(tipInDollars,2))
    total = (bill/people) + tipInDollars
    print('TOTAL: $', round(total,2))

def getTipPeople(bill,tip,people):
    tipInDollars = float(bill*(tip/100)/people)
    print('TIP (per person): $', round(tipInDollars,2))
    total = (bill/people) + tipInDollars
    print('TOTAL (per person): $', round(total,2))

