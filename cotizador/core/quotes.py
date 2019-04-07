
class Quotes():

    def __init__(self, *args, **kwargs):
        super(Quotes, self).__init__(*args, **kwargs)
    

    def ageSelector(self, age):
        age = int(age)
        if age < 25:
            return 'Junior (H25)'
        elif age < 35:
            return 'Juvenil (H35)'
        elif age < 40:
            return 'Individual (+35)'

    def kidsSelector(self,kids):
        kids = int(kids)
        if kids >= 0 and kids <= 3:
            if kids == 0:
                return ''
            elif kids == 1:
                return ' + 1 Hijo'
            elif kids == 2:
                return ' + 2 Hijos'
            elif kids == 3:
                return ' + 3 Hijos'
        else:
            aditional = str(kids - 3)
            return '3 Hijos + {} Adicionales'.format(aditional)
    

    def planSelector(self, couple, kids, age,):
        '''
        This function take the couple, kids and age values sendint by de form to retrive the correct health insurance quotes.
        '''
        age_f = self.ageSelector(age)
        kids_f = self.kidsSelector(kids)

        if couple == 'no':
            return age_f + kids_f
        elif age_f == 'Individual (+35)' and kids_f == '':
            return 'Matrimonio' 
        elif age_f == 'Individual (+35)':
            return 'Matrimonio' + kids_f
        elif kids_f == '':
            return 'Mat. ' + age_f
        else:
            return 'Mat. ' + age_f + kids_f


    def salaryDiscount(self, queryset, salary):
        '''
        This function apply the salary discount to all the values for this person. 
        '''
        salary = float(salary) * 0.03  # Take the salary, and aply the part that could be discounted

        for i in queryset:  # Get the object of the queryset
            i.smg01 = round(i.smg01  - salary, 2)    # Use the object edit the values on the fly
            i.smg02 = round(i.smg02  - salary, 2)
            i.smg10 = round(i.smg10  - salary, 2)
            i.smg20 = round(i.smg20  - salary, 2)
            i.smg30 = round(i.smg30  - salary, 2)
            i.smg40 = round(i.smg40  - salary, 2)
            i.smg50 = round(i.smg50  - salary, 2)
            i.smg60 = round(i.smg60  - salary, 2)
            i.smg70 = round(i.smg70  - salary, 2)

        return queryset   # Return the queryset edited. 
