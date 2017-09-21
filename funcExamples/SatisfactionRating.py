def SatClass(rating):
    if rating>=90:
        grade = 'Excellent'
    elif rating>=80:
        grade = 'Good'
    elif rating>=65:
        grade = 'Fair'
    else:
        grade = 'Poor'
    return grade

