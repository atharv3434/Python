class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Hello {self.name}, You are {self.age} Year's Old"



s1 = Student("Atharv", 23)  
fruits = "Apple, Mango,   Guava, Pineapple"
print("=" * 30)


city = "Bangalore"

print(f"[{city:<15}]")  # Left-aligned:  [Bangalore      ]
print(f"[{city:>15}]")  # Right-aligned: [      Bangalore]
print(f"[{city:^15}]")  # Center-aligned: [   Bangalore   ]

# Using a custom padding fill character (e.g. '*')
print(f"{city:*^17}")   # Center star-padded: ****Bangalore****
# print(s1)  
# print(fruits.split(","))
# print(fruits)