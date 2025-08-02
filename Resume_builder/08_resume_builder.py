class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

# This resume is more accurate for engineering students.
class resume:
   
    def __init__(self,name,address,contact,educ,university,cgpa_1,field,experience,certifications,father,birth,gender,language,date,place,signature):
        self.name = name
        self.address = address
        self.contact = contact
        self.educ = educ
        self.university = university
        self.cgpa_1 = cgpa_1
        self.field = field    
        self.exp = experience
        self.certi = certifications
        self.father = father
        self.birth = birth
        self.gender = gender
        self.lang = language
        self.date = date
        self.place = place
        self.sign = signature

    def info(self):
        print(color.BOLD+"\nDid you study further after your Graduation?"+color.END)
        print(color.BOLD+"(a) for Yes and (b) for No"+color.END)
        anuj1 = input(color.BOLD+'Enter - ')
        if anuj1 == 'a':
            s = input(color.BOLD+'Enter name of further degree like (M.tech in CS) - ')
            p = input(color.BOLD+'Enter name of college/university - ')
            b2 = input(color.BOLD+'Enter your CGPA - ')
        else:
            pass
        print(color.BOLD+'\nHave you done internship anywhere?'+color.END)
        print(color.BOLD+"Type - (a) for Yes and (b) for No"+color.END)
        anuj2 = input(color.BOLD+'Enter - ')
        if anuj2 == 'a':
            q = input(color.BOLD+'Enter the name of company you have done internship in - ')  
            print(color.BOLD+'Type - (a) for months (b) for a year and (c) for years'+color.END)
            m = input(color.BOLD+"Enter here - ")
            if m == 'a' or m == 'c':
                w = input(color.BOLD+'Enter number of years/months in numbers - ')
            else:
                pass  
        
        print(color.PURPLE+color.BOLD+'\n\n\n\n\n\n\t\t\tResume Builder\n'+color.END) 
        print(color.BOLD+'--------------------------------------------------------------------'+color.END)
        print(color.BOLD+color.DARKCYAN+'Name - '+color.END+ color.BOLD+ f'{self.name}'+color.END)
        print(color.BOLD+color.DARKCYAN+'Address - \n'+color.END+ color.BOLD+ f'{self.address}'+color.END)
        print(color.BOLD+color.DARKCYAN+'Contact No. - '+color.END+ color.BOLD+ f'{self.contact}'+color.END)
        print(color.BOLD+'--------------------------------------------------------------------\n'+color.END)
        print(color.PURPLE+color.BOLD+'Carrier Goal :'+color.END)
        print(color.BOLD+'      ➢  To pursue a carrier in reputed organization which will give\n\t me an opportunity to learn and enhance my knowledge at the\n\t same time contributes my effort in growth of organization.\n')
        print(color.PURPLE+color.BOLD+'Education :'+color.END)
        print(color.BOLD+f'      ➢  {color.DARKCYAN+self.educ+color.END}'+color.BOLD+ ' from ' f'{color.DARKCYAN+color.BOLD+self.university+color.END}'+color.BOLD+ ' with '+color.DARKCYAN+ 'CGPA of ' f'{color.DARKCYAN+color.BOLD+str(self.cgpa_1)+color.END}.'+color.END)
        if anuj1 == 'a':
            print(color.BOLD+f'      ➢  {color.DARKCYAN+s+color.END}'+color.BOLD+ ' from ' f'{color.DARKCYAN+color.BOLD+p+color.END}'+color.BOLD+' with '+color.DARKCYAN+ 'CGPA of ' f'{color.BOLD+color.DARKCYAN+str(b2)+color.END}.'+color.END)  
        else:
            pass
        print(color.BOLD+f'      ➢  Member of Student association of {color.DARKCYAN+color.BOLD+self.field+color.END}.'+color.END)    
        print(color.BOLD+f'      ➢  '+color.DARKCYAN+color.BOLD+'Managed a student project'+color.END+color.BOLD+ ' to organize a conference for 50+\n\t professionals.\n'+color.END)
        print(color.PURPLE+color.BOLD+'Experience :'+color.END)
        print(color.BOLD+f'      ➢  {color.DARKCYAN+self.exp+color.END}'+color.BOLD+'.'+color.END) 
        if anuj2 == 'a':
            if m == 'a':
                print(color.BOLD+f'      ➢  I have done Internship in {color.DARKCYAN+color.BOLD+(q)+color.END}'+color.BOLD+f' for {color.DARKCYAN+color.BOLD+str(w)+" months"+color.END}. '+color.END)  
            elif m == 'b':
                print(color.BOLD+f'      ➢  I have done Internship in {color.DARKCYAN+color.BOLD+(q)+color.END}'+color.BOLD+f' for '+color.DARKCYAN+color.BOLD+'a year. '+color.END)
            elif m == 'c':
                print(color.BOLD+f'      ➢  I have done Internship in {color.DARKCYAN+color.BOLD+(q)+color.END}'+color.BOLD+f' for {color.DARKCYAN+color.BOLD+str(w)+" years"+color.END}. '+color.END)
            else:
                pass
        
        print(color.PURPLE+color.BOLD+'\nCertifications :'+color.END)
        print(color.BOLD+f"      ➢  I have a Certification in {color.DARKCYAN+color.BOLD+self.certi+color.END}"+color.BOLD+".\n"+color.END)
        print(color.PURPLE+color.BOLD+'Personal Profile :'+color.END)
        print(color.BOLD+f"      ➢  Father's Name : {color.DARKCYAN+self.father+color.END}"+color.BOLD+ f"\n      ➢  Date of Birth : {color.DARKCYAN+color.BOLD+self.birth+color.END}"+color.BOLD+ f"\n      ➢  Gender : {color.DARKCYAN+color.BOLD+self.gender+color.END}"+color.BOLD+ f"\n      ➢  Known languages : {color.DARKCYAN+color.BOLD+self.lang+color.END}\n")
        print(color.BOLD+f'\nDate : {color.DARKCYAN+self.date+color.END}'+color.BOLD+f'\t\t\t Signature : {color.DARKCYAN+self.sign+color.END}')
        print(color.BOLD+f"Place : {color.DARKCYAN+self.place+color.END}\n")
        print(color.BOLD+'--------------------------------------------------------------------\n'+color.END)
     
a1 = input(color.BOLD+'\nEnter your first and last name like (Anuj Pisal) - ')
a2 = input('\nEnter your address - ')
a3 = input("\nEnter your Contact No - ")
a4 = input("\nEnter name of your degree like (B.tech in Civil) - ")
a5 = input('\nEnter name of your college/university - ')
b1 = input('\nEnter your CGPA - ')
a6 = input("\nEnter name of your field like (Civil Engineering) - ")

print("\nType accordingly - (a) for Fresher or (b) for Experienced")
a = input('Type here - ')
if a == 'a':
    a7 = 'Fresher'
elif a == 'b':
    b1 = int(input('Enter number of years - '))
    a7 = f'{b1} years of experience'
else:
    a7 = 'Fresher'

a8 = input('\nEnter name of subject in which you have certificate -  ')
a9 = input('\nEnter full name of your father - ')
a10 = input("\nEnter your Date of Birth like (10th May 2000) - ")
a11 = input("\nEnter your gender - ")
a12 = input('\nEnter name of languages you know - ')
a13 = input("\nEnter today's date like (10th May 2020) - " ) 
a15 = input("\nType your signature like (A.S.Pisal) - "+color.END)
sample = resume(a1,a2,a3,a4,a5,b1,a6,a7,a8,a9,a10,a11,a12,a13,'Pune',a15)
sample.info()
