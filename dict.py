#saving to a txt file
dict = {'Python' : '.py', 'C++' : '.cpp', 'Java' : '.java'}
f = open("dict.txt","w")
f.write( str(dict) )
f.close()



{
"customers_name": "John",
"customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
"customer_phone": "0789887334",
"courier": 2,
"status": "preparing"
}

class Person(object):
    def __init__(self):
        self.name = ""
        self.address = ""
        self.phone = ""
        self.age = ""
        self.whip = {}

#     def writing(self):
#         self.whip[p.name] = p.age, p.address, p.phone
#         target = open('deed.txt', 'a')
#         target.write(str(self.whip))
#         print self.whip

#     def reading(self):
#         self.whip = open('deed.txt', 'r').read()
#         name = raw_input("> ")
#         if name in self.whip:
#             print self.whip[name]

# p = Person()

# while True:
#     print "Type:\n\t*read to read data base\n\t*write to write to data base\n\t*exit to exit"
#     action = raw_input("\n> ")
#     if "write" in action:
#         p.name = raw_input("Name?\n> ")
#         p.phone = raw_input("Phone Number?\n> ")
#         p.age = raw_input("Age?\n> ")
#         p.address = raw_input("Address?\n>")
#         p.writing()
#     elif "read" in action:
#         p.reading()
#     elif "exit" in action:
#         exit(0)