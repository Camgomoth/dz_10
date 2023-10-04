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
        if len(value) == 10:
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
        if not self.phones:
            self.phones= AddressBook().data
            print(self.phones)
            for i in self.phones:
                for j in i.get(self.name):
                    if str(phone) == str(j):
                        indx =  i.get(self.name).index(j)
                        i.get(self.name).remove(j)
                        i.get(self.name).insert(indx, Phone(new_phone))
                        return f'Phone has been edited succesfully {self.phones}'
                    
        for i in self.phones:    
            if str(phone) == str(i):
                indx = self.phones.index(i)
                self.phones.remove(i)
                self.phones.insert(indx, Phone(new_phone))
     
                return f'Phone has been edited succesfully {self.phones}'
        return f"It is impossible to edit a non-existing phone number, try command 'add_phone'"

    def find_phone(self, phone):
        for i in self.phones:
            if str(phone) == str(i):
                    return Phone(phone)
        return f"It is impossible to find a non-existing phone number, try command 'add_phone'"

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
    
        self.data[str(record.name)] =  record.phones

        return f'{self.data}'

    
    def find(self, record):
       pass
        #  print(self.data)
        #  for i in self.data:
        #      if str(i) == record:
        #          Record(record).phones = self.data.get(i)
        #          return Record(record).phones
    
      
    
    def delete(self, name):
        for i in self.data.keys():
            if str(i) == name:
                self.data.pop(i)
                return f'Contact has been removed succesfully {self.data}'

        return f"Something went wrong"
    




# book = AddressBook()

# jane_record = Record("Jane")
# jane_record.add_phone("9876543210")
# jane_record.add_phone("1234567890")
# book.add_record(jane_record)

# john_record = Record("John")
# john_record.add_phone("1234567890")
# john_record.add_phone("5555555555")   

# book.add_record(john_record)
# print(book.find("Jane"))
# #print(jane.edit_phone("1234567890", "0000000000"))    


     
     
     
