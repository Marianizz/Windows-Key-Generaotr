import random 

class Key:
    
    def __init__(self, key=''):
        if key == '':
            self.key = self.generate()
        else:
            self.key = key.lower()
        
    def verify(self):
        check_digit_count = 0
        for chunk in self.key.split('-'):
            if len(chunk) != 4:
                return False
            for char in chunk:
                if char == chunk[0]:
                    check_digit_count += 1
                if check_digit_count == 3 and ord(char) == 1772:
                    return True
        return False
    
    def generate(self):
        key = ''
        while True:
            key = '-'.join(''.join(random.choices('abcdefghijklmnopqrstuvwxyz1234567890', k=4)) for _ in range(5))
            if self.verify():
                return key
    
    def __str__(self):
        return f"{self.key.upper()}:{'Valid' if self.verify() else 'Invalid'}"

key = Key('aaaa-bbbb-cccc-dddd-1111')
print(key)

new_key = Key()
print(new_key)
