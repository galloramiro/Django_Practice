
class Quotes():

    def __init__(self, *args, **kwargs):
        super(Quotes, self).__init__(*args, **kwargs)
    
    def ageSelector(self, age):
        if age == 'jr':
            return 'Junior (H25)'
        elif age == 'juv':
            return 'Juvenil (H35)'
        elif age == 'ind':
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


# ('-25', '-25'), ('26-35', '26-35'), ('35+', '35+')
# (0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)

# Ind. Junior
# Ind. Juvenil
# Individual

# Mat. Junior
# Mat. Juvenil
# Mat. Individual