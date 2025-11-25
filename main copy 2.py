cat = r"""
 /\_/\
( o.o )
 > ^ <
"""

tree = r"""
    /\
   /  \
  /____\
    ||
    ||
"""

choice = input("Hello, welcome to the ASCII art code. Would you like to see a cat or a tree?").lower()

if choice == "cat":
    print(cat)
elif choice == "tree":
    print(tree)
else:
    print("Hey, you need to answer with either 'cat' or 'tree', sorry..")

