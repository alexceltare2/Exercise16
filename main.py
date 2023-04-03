from customer import Account
from employee import Employee


def main():

    name = input("Enter name: ")
    gen = input("Enter gender(m/f): ")
    dep = input("Enter department name: ")
    idd = input("Enter id number: ")
    bal = input("Enter initial deposit(£): ")
    account_one = Employee(name, gen, dep, idd)
    print(account_one)
    account_one = Account(int(bal))
    print(account_one)
    print("\nCreating another account:...")
    account_two = Account(2000)
    print(f"Total number of created accounts: {Account.numCreated}")
    print("Comparing accounts:.....")
    if account_one == account_two:
        print(f"account_one has the same money as account_two!")
    else:
        print(f"No, the accounts, are different amounts")
    #account_one = Account(1000)
    #print(some_account.getbalance())

    #another = Account(0)
    #another.deposit(10)

    #eoghan = Account(234000)
    #eoghan.deposit(10000)

    #print(another.getbalance())
    #print(eoghan.getbalance())
    #print(Account.numCreated)

    #print("object another is class", another.__class__.__name__)
    #print(eoghan.__class__.__name__)
    #print(eoghan)
    #print(another)

    # Overriding operators
    #if eoghan > another:
    #    print(f"{eoghan} has more money than {another}!")
    #elif another < some_account:
    #    print(f"{another} has less money than {some_account}!")


# Using a class method
#print(Account.get_total_balance())

if __name__ == '__main__':
    main()
