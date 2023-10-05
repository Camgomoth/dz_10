from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        self.value = value
   
   


class Phone(Field):     
    def __init__(self,value):
        if len(value) == 10 and value.isdigit():
            self.value = value
        else:
            raise ValueError       
    

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
    
    def add_phone(self,phone):
        self.phones.append(Phone(phone))
            
        return f'Phone has been added succesfully {self.phones}' 
    
    def remove_phone(self,phone):
        for i in self.phones:
            if str(phone) == str(i):
                self.phones.remove(i)
                return f'Phone has been removed succesfully {self.phones}'

       
        
        return f"It is impossible to remove a non-existing phone number, try command 'add_phone'"  

    def edit_phone(self, phone, new_phone):
        for i in self.phones:
            if str(phone) == str(i):
                 indx = self.phones.index(i)
                 self.phones.remove(i)
                 self.phones.insert(indx, Phone(new_phone))
     
                 return f'Phone has been edited succesfully {self.phones}'
        raise ValueError

    def find_phone(self, phone):
        for i in self.phones:
            if str(phone) == str(i):
                    return Phone(phone)
        return 

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
    
        self.data[record.name.value] = record

        return f'{self.data}'

    
    def find(self, name):
    
        return self.data.get(name)
    
      
    
    def delete(self, name):
        for i in self.data.keys():
            if str(i) == name:
                self.data.pop(i)
                return f'Contact has been removed succesfully {self.data}'

        return f"Something went wrong"
    










     


     
     
     
