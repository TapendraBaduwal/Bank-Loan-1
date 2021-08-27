#Loan classification as per NRB bank according to the overdue of credit period time and book provision for classified loans.
def loan_class(t):
    if t<=1:
        return "Pass_loan::Make 1% provision"
    elif 1<t<=3:
        return "Watchlist_loan::Make 5% provision"
    elif 3<t<=6:
        return "Sub-standard_loan::Make 25% provision"
    elif 6<t<=12:
        return "Doubtful_loan::Make 50% provision"
    else:
        return "Loss_loan::Make 100% provision"


