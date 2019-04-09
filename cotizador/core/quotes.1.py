
class Quotes():

    def __init__(self, *args, **kwargs):
        super(Quotes, self).__init__(*args, **kwargs)
    

    def ageSelector(self, age):

        if age <= 35:
            if age <= 25:
                return 'Junior'
            else:
                return 'Juvenil'
        elif age >= 65:
            return ['Individual', 'Adic. 65']
        elif age >= 60:
            return ['Individual', 'Adic. 60']
        elif age >= 50:
            return ['Individual', 'Adic. 50']
        elif age >= 40:
            return ['Individual', 'Adic. 40']
        else:
            return 'Individual'

    def kidsSelector(self, kids, kids_age):
        kids_dict = {1:'1 Hijo', 2:'2 Hijos', 3:'3 Hijos', } 
        age_aditional = 0
        kids_aditional = 0
        kids_value = ''
        
        if kids <= 3:
            kids_value = kids_dict[kids]
        else:
            kids_value = kids_dict[3]
            kids_aditional = kids - 3
            
        for age in kids_age:
            if age <= 30 and age >= 21:
                age_aditional += 1

        return [kids_value, kids_aditional, age_aditional]




q = Quotes()




"""
kidsSelector Tries

print(q.kidsSelector(1, [5,]))
print(q.kidsSelector(2, [5, 21]))
print(q.kidsSelector(3, [5, 21, 30]))
print(q.kidsSelector(4, [5, 21, 30, 15]))
print(q.kidsSelector(5, [5, 21, 30, 15, 10]))
"""


"""
ageSelector Tries

print(q.ageSelector(20))
print(q.ageSelector(25))
print(q.ageSelector(26))
print(q.ageSelector(35))
print(q.ageSelector(36))
print(q.ageSelector(40))
print(q.ageSelector(41))
print(q.ageSelector(50))
print(q.ageSelector(51))
print(q.ageSelector(60))
print(q.ageSelector(61))
print(q.ageSelector(65))
print(q.ageSelector(66))
"""