has_high_income=True
has_good_credit=True

if has_high_income and has_good_credit:
    print ("Eligible for a loan")


has_high_income=True
has_good_credit=False

if has_good_credit or has_high_income:
    print ("Eligible for a loan")

has_good_credit=True
has_criminal_record= False

if has_good_credit and not has_criminal_record:
    print ("Eligible for a loan")
