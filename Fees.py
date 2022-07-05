# A parent to payfees and it reflect on her end
# a parent can view fee balance 
# a payment plan can be suggested for them  
# input date time

class Fees:
    school_names=[{'name':'Lwak','code':200,'term_one':34000,'term_two':24000,'term_three':10000},
    {'name':'Asumbi','code':100,'term_one':36000,'term_two':25000,'term_three':12000}]
    def __init__(self,school_name,school_code):
        self.school_name=school_name
        self.school_code=school_code
        self.balance=0
        self.bank_alance=0
        self.mpesaBalance=0
       

    def school_term(self):
         # 'and', sub['code']
        # 'What school are you paying to',
        for sub  in self.school_names:
            res=sub['name']
            res_two=sub['code']
            query=input(res)
            querys=input(res_two)
        print(query)
        print(querys)
        # "What term do you want to pay for?",subs['term_one','term_two','term_three']
        for subs in self.school_names:
            if subs== subs['term_one'] or subs['term_two'] or subs['term_three']:
                user=input(subs)
        self.balance+=user
        print(self.balance)
    


fee=Fees('Lwak',200)
print(fee.school_term())