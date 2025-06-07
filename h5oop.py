class Bankaccount:
    
    def __init__(self, account_name, balance = 0):
        self.account_name = account_name # banka hesabı adı
        self.balance = balance # hesap bakiyesi
        
    def deposit(self, amount): # hesaba para yatırma işlemi
        self.balance += amount # amount = yatırdığın para
        print(f"{amount} TL deposited")
        return self.balance
    
    def withdraw(self, amount): # para çekme, 
        if amount > self.balance:
            print('Insufficient balance')
        else:
            self.balance -= amount
            print(f"{amount} TL withdrawn")
        return self.balance
        
    def balance_view(self):
        print(f"{self.account_name} you have {self.balance} TL  in your account.")  # bakiye sorgulama
        

acc = Bankaccount("Samet Hoca", 0)
acc.deposit(int(input("Enter the amount you want to deposit: ")))
acc.withdraw(int(input("Enter the amount you want to withdraw: ")))
acc.balance_view()
    
    






