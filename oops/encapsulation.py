class bank_account:
# publiclkihkgcfxcgvuhijok;jgf
    account_holder_name = "rahul"  
# protected
    _account_number = "12345"
# private 
    __account_balance = "10000000000"

    def first_scheme(self):
        print("this is beneficial sechem")
    
    def second_scheme(self):
        print("this is worst scheme")

class pan_detail(bank_account):
    pan_number = "54321"

    def pan_detailsss(self):
        print("here is the  informaion regarding pan details")


objectt = pan_detail()
print("started ---------------------------")

objectt.pan_detailsss()
print(objectt.account_holder_name)

print(objectt._account_number)

# print(objectt.__account_balance)


