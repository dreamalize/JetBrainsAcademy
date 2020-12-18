import math
import argparse


def period(loan_, annuity_, interest_):
    a = annuity_
    p = loan_
    i = interest_ / (12 * 100)
    return math.log((a / (a - i * p)), 1 + i)


def annuity(loan_, period_, interest_):
    p = loan_
    n = period_
    i = interest_ / (12 * 100)
    return p * (i * (1 + i) ** n) / ((1 + i) ** n - 1)


def loan(annuity_, period_, interest_):
    a = annuity_
    n = period_
    i = interest_ / (12 * 100)
    return a / ((i * (1 + i) ** n) / ((1 + i) ** n - 1))


def diff(loan_, period_, interest_):
    p = loan_
    n = period_
    i = interest_ / (12 * 100)
    payments = []
    for mnth in range(1, period_ + 1):
        d = math.ceil(p / n + i * (p - p * (mnth - 1) / n))
        payments.append(d)
        mnth += 1
    sum_payments = 0
    for element in payments:
        sum_payments += element
    overpayment = sum_payments - loan_
    
    return payments, overpayment


def years_months(number_of_months):
    years_ = 0
    while number_of_months >= 12:
        years_ += 1
        number_of_months -= 12

    if years_ == 1:
        if number_of_months == 1:
            y_ = str(years_) + " year and "
            m_ = str(number_of_months) + " month"
        elif number_of_months > 1:
            y_ = str(years_) + " year and "
            m_ = str(number_of_months) + " month" + "s"
        else:
            y_ = str(years_) + " year"
            m_ = ""

    elif years_ > 1:
        if number_of_months == 1:
            y_ = str(years_) + " year" + "s and "
            m_ = str(number_of_months) + " month"
        elif number_of_months > 1:
            y_ = str(years_) + " year" + "s and "
            m_ = str(number_of_months) + " month" + "s"
        else:
            y_ = str(years_) + " year" + "s"
            m_ = ""

    else:
        if number_of_months == 1:
            y_ = ""
            m_ = str(number_of_months) + " month"
        elif number_of_months > 1:
            y_ = ""
            m_ = str(number_of_months) + " month" + "s"
        else:
            y_ = ""
            m_ = ""

    return y_, m_


parser = argparse.ArgumentParser()

parser.add_argument("--type", type=str)

parser.add_argument("--principal", type=int)

parser.add_argument("--periods", type=int)

parser.add_argument("--interest", type=float)

parser.add_argument("--payment", type=float)

args = parser.parse_args()


if args.type == "diff" and args.interest:
    if args.principal and args.periods:

        list_, int_ = diff(args.principal, args.periods, args.interest)
        for elem in list_:
            print("Month {}: payment is {}".format(list_.index(elem) + 1, elem))
        print()
        print(f"Overpayment = {int_}")

    else:
        print("Incorrect parameters")

elif args.type == "annuity" and args.interest:
    if args.principal and args.payment:

        result = period(args.principal, args.payment, args.interest)
        result = math.ceil(result)

        y, m = years_months(result)
        print(f"It will take {y}{m} to repay this loan!")
        print("Overpayment = {}".format(math.ceil(result) * args.payment - args.principal))

    elif args.principal and args.periods:

        result = annuity(args.principal, args.periods, args.interest)
        print(f"Your annuity payment = {math.ceil(result)}!")
        print("Overpayment = {}".format(math.ceil(result) * args.periods - args.principal))

    elif args.payment and args.periods:

        result = loan(args.payment, args.periods, args.interest)
        print(f"Your loan principal = {math.floor(result)}!")
        print("Overpayment = {}".format(int(args.periods * args.payment - math.floor(result))))

    else:
        print("Incorrect parameters")

else:
    print("Incorrect parameters")
