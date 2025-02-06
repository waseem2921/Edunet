"""print("Hello World")
age = 20
name="Waseem"
department="CSE"
Roll_Number= "22FH1A0528"
print("The name of  Student is",name ,"of age",age ,"from department", department,"of Roll Number" ,Roll_Number)

#Invalid Variables 
#1_name="john"
#def = name
#a==10
#@user = name
#first name = khan
#Using comma Separeted Method 
a=10
b=20
c=30
print(a,b,c)
#using f-String Function
print(f"value of a {a}, value of b {b},value of c {c}")

#Using Input values 
x=int(input("Enter x Value"))
y=int(input("Enter y value"))
z=int(input("Eneter z Value"))
print(f"value of a {x}, value of b {y},value of c {z}")

#add of two numbers 
print(f"the sum of X and y are {x+y}")

#finding out the class type of a variable 
print(type(x)) 

s=float(input("Enter s value"))
t=float(input("enter t value"))
print(f"Multiple of two numbers {round(s*t,5)}")

a="its a wonderful session" #String by using Single Quotes
b=Yes ! It was great while playing with python
Yep ! We leaarnt lots of things today""#String by using Double Quotes 
#print(a)
#print(b)
print(len(a))
print(b.lower())
print(a.upper())
print(b.swapcase())
print(a.capitalize())
print(b.replace("leaarnt","learnt"))
print(a.center(20, "o"))
print(b.count("!"))
print(b.index("a"))
print(b.isalpha())

a="python "
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[5])
print(a.find('o'))
print(a.strip())
print(a.title())
print(a.split())
a="Hello"
b="am Good"
print(a[2:5]) #Slicing in python
print(a[1:4])
print(a[0:5:2])
print(a[1:4:2])
print(b[::3])

#Using Operaters 
a = int(input("Enter a number"))
b= int(input("Enter b Value"))
print("Addition",a+b)
print("Subraction",a-b)
print("Multi",a*b)
print("Division",a/b)
print("modulo",a%b)
print("Floor division",a//b)


a=int(input("Enter a value"))
b=int(input("Enter b value"))
c=int(input("enter c Value"))
if(a>b and a>c):
    print("A is Greater")
elif(b>a and b>c):
    print("B is Greater ")
elif(c>a and c>b):
    print("C is greater")
else:
    print("All are Equal")

a = int(input("Enter a Number"))
LSB = a//100
MSB = a%100
if (MSB > LSB):
    print("MSb is greater than LSB")
else:
    print("LSB is greater than MSB")

mylist=[1,2,3,4,5,6,6.5,4,9,'HI',"HELLO"]
print(mylist[1:3])
mylist.append(100)
mylist.insert(3,0)
print(mylist)

list=[2.44,9.99,4.98,1,78,'dog','apple','wrong']
#list.sort()
#list.sort(reverse=True)
#print(list)
#for i in range(len(list)):
 #   print(i)
int_list=[]
float_list=[]
str_list=[]
for val in list:
    if type(val)==int:
        int_list.append(val)
    elif type(val)==float:
        float_list.append(val)
    else:
        str_list.append(val)
print(int_list)
print(float_list)
print(str_list)


mylist=[1,19,0.8,9.6,'Hi',10,'Python','10.99']
int_mylist=[]
float_mylist=[]
str_mylist=[]
for val in mylist:
    if type(val)==int:
        int_mylist.append(val)
    elif type(val)==float:
        float_mylist.append(val)
    else:
        str_mylist.append(val)

int_mylist.sort()
float_mylist.sort()
str_mylist.sort()
total_list=int_mylist +float_mylist + str_mylist
print(total_list)

dict={"name":"Waseem" , "email":"Waseemkhan@gmail.com" , "Phone":93828283010}
dict["address"]="Kurnool"
dict["Phone"]=3343435645
print(dict)

for i in range(100,200,9):
    print(i)
dict={ }
while(True):
    data = int(input(""Enter
    0:Create
    1:Read
    2:Update
    3:delete
    4:Quit""))
    if data==4:
        break
    elif data==0:
        print
        key = input("Enter key: ")
        value = input("Enter value: ")
        dict[key] = value
        print("Entry added.")
    elif data == 1:
        key = input("Enter key to read: ")
        if key in dict:
            print(f"{key}: {dict[key]}")
        else:
            print("Key not found.")
    elif data == 2:
        key = input("Enter key to update: ")
        if key in dict:
            value = input("Enter new value: ")
            dict[key] = value
            print("Entry updated.")
        else:
            print("Key not found.")
    elif data == 3:
        key = input("Enter key to d3elete: ")
        if key in dict:
            del dict[key]
            print("Entry deleted.")
        else:
            print("Key not found.")

#Using Functions
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def mod(a,b):
    return a%b

a=int(input("Enter a value"))
b=int(input("Enter b value"))
print("Addition",add(a,b))
print("Subraction",sub(a,b))
print("Multiplication",mul(a,b))
print("Division",div(a,b))
print("Modulo",mod(a,b))

def addition(a,b):
    print(a+b)
addition(10,20)

#key args method
def addition(**num):
    for key,val in num.items():
        print(key,val)
addition(name="Khan",email="khan@gmail.com")

# Define a class named Person
class Person:
    # Constructor method to initialize the object
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method to display the person's details
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Create an instance of the Person class

import pandas as pd 
data = pd.read_csv("data.csv")
#print(data.head)  #Prints the first 5 rows of the data
#print(data.head(10)) #Prints the first 10 rows of the data
#print(data.tail) #Prints the last 5 rows of the data
#print(data.tail(10)) #Prints the last 10 rows of the data
print(data.info()) #Prints the information about the data
print(data.describe()) #Prints the statistical summary of the data
print(data.isnull().sum()) #Prints the number of missing values in each column
#with open("text.txt","r") as file:
 #   data = file.read()
  #  print(data)
#with open("text.txt","r") as file:
 #   data = file.readlines()
  #  print(data)

#with open("text.txt","w") as file:
 #   file.write("Hello, I am writing to a file")
change_content = ""
#with open("text.txt","+r") as file:
 #   data = file.readlines()
   # print(data)
    #for line in data:
 #       change_content += line.replace("\n","\t")
#
#with open("text.txt","+w") as file:
 #   file.write(change_content)
  #  print("Content Changed Successfully")
with open("text.txt", "r") as file:
    lines = file.readlines()
    for i, line in enumerate(lines):
        print(f"Length of line {i + 1}: {len(line.strip())}")


def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    else:
        return result

# Test the function
print(divide(10, 2))  # Should print 5.0
print(divide(10, 0))  # Should print an error message

def safe_divide_with_finally(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except TypeError:
        return "Error: Inputs must be numbers."
    else:
        print("Division successful!")
        return result
    finally:
        print("Execution complete.")

# Test the function
print(safe_divide_with_finally(10, 2))  # Should print success message, result, and execution complete
print(safe_divide_with_finally(10, 0))  # Should print an error message for division by zero and execution complete
print(safe_divide_with_finally(10, 'a'))  # Should print an error message for invalid input and execution complete


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#data Collection 
data = pd.read_csv("data.csv")
#print(data.head)  #Prints the first 5 rows of the data
#print(data.head(10)) #Prints the first 10 rows of the data
#print(data.tail) #Prints the last 5 rows of the data
#print(data.tail(10)) #Prints the last 10 rows of the data
#Statistical analysis
#print(data.info()) #Prints the information about the data
#print(data.describe()) #Prints the statistical summary of the data
#print(data.isnull().sum()) #Prints the number of missing values in each column
#print(data.dropna()) #drops the null values
#Duplication 
#print(data.duplicated().sum())

#plotting
x=data["date"]
y=data["price"]
plt.scatter(x,y)
plt.xlabel("Mileage")
plt.ylabel("Price")
plt.title("Price v/s Mileage")
plt.show()

plt.hist(y,bins=30)
plt.xlabel("Mileage")
plt.ylabel("Price")
plt.title("Price v/s Mileage")
plt.show()

plt.subplot(1,2,1)
sns.boxplot(y=x)
plt.show() 

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

data = pd.read_csv("car_price_dataset.csv")
print(data.head())


x = data[["Price"]]  
y = data["Mileage"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Create and train the linear regression model
lrmodel = LinearRegression()
lrmodel.fit(x_train, y_train)

# Make predictions
y_pred = lrmodel.predict(x_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Plot the results
plt.scatter(x, y, color='blue', label='Actual data')
plt.plot(x_test, y_pred, color='red', linewidth=2, label='Regression line')
plt.xlabel("date")
plt.ylabel("price")
plt.title("Year vs Profit")
plt.legend()
plt.show()

import requests
r = requests.get('https://books.toscrape.com/')
print(r)
print(r.content)

import requests
from bs4 import BeautifulSoup
import csv

base_url = 'https://oceanofpdf.com/'
categories = ['webnovels']

for category in categories:
    url = f'{base_url}{category}/index.html'
    print(f"Scraping books for category: {category}")
    book_data = []
    page_number = 1
    total_books = 0

    while total_books < 10:
        page_url = f"{url}?page={page_number}"
        response = requests.get(page_url)
        soup = BeautifulSoup(response.content, 'html.parser')

        for book in soup.find_all('article', class_='product_pod'):
            title = book.h3.a.get('title')
            price = book.find('p', class_='price_color').get_text()
            availability = book.find('p', class_='instock availability').get_text().strip()
            image_url = book.img.get('src')
            rating = book.find('p', class_='star-rating')['class'][1]
            product_page_url = book.h3.a.get('href')

            book_data.append({
                'Title': title,
                'Price': price,
                'Availability': availability,
                'Image URL': image_url,
                'Rating': rating,
                'Product Page URL': f'{base_url}{product_page_url}'
            })
            total_books += 1
        page_number += 1

    filename = f'{category}_books.csv'
    keys = book_data[0].keys() if book_data else []
    with open(filename, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(book_data)
    
    print(f"Books data for '{category}' category saved in '{filename}'")"""

import requests
from bs4 import BeautifulSoup
import csv

base_url = 'https://webscraper.io/test-sites/e-commerce/'
categories = ['laptops']

for category in categories:
    url = f'{base_url}allinone/computers{category}/index.html'
    print(f"Scraping books for category: {category}")
    book_data = []
    page_number = 1
    total_books = 0

    while total_books < 10:
        page_url = f"{url}?page={page_number}"
        response = requests.get(page_url)
        soup = BeautifulSoup(response.content, 'html.parser')

        for book in soup.find_all('article', class_='product_pod'):
            title = book.h3.a.get('title')
            price = book.find('p', class_='price_color').get_text()
            availability = book.find('p', class_='instock availability').get_text().strip()
            image_url = book.img.get('src')
            rating = book.find('p', class_='star-rating')['class'][1]
            product_page_url = book.h3.a.get('href')

            book_data.append({
                'Title': title,
                'Price': price,
                'Image URL': image_url,
                'Rating': rating
            })
            total_books += 1
        page_number += 1

    filename = f'{category}_books.csv'
    keys = book_data[0].keys() if book_data else []
    with open(filename, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(book_data)
    
    print(f"Books data for '{category}' category saved in '{filename}'")
