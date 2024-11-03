class SuperStr(str):
    def is_repeatance(self):
        for i in self.lower():
            if i not in {'s',' '}:
                return False
        else:
            return True

    def is_palindrom(self):
            print(self[::1],self[::-1])
            if self[::1] != self[::-1]:
                return False
            else:
                return True

str1 = SuperStr
print(str1.is_repeatance('sSSss sss'))
print(str1.is_palindrom(''))