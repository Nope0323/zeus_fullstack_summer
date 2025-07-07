#python dictionary
# problem

favorit_sport= ['Ralph Williams, Football',"Micheal Tippet,Basketball","Edward Elgar,Basketball"]

ralph_sport= favorit_sport[0]

print(ralph_sport[16:])

favorit_sport= {
    "Ralf Williams":"Football",
    "Micheal Tippet":"Basketball",
    "Edward Elgar":"Basketball"
}
print(favorit_sport)

print(favorit_sport['Edward Elgar'])

favorit_sport["Rebecca Clarke"] = "Netball"
favorit_sport["Frank Bridge"] = "Rugby"
favorit_sport["Ethel Smyth"] = "Badminton"

favorit_sport[" Ralf Williams"] = "Ice Hokey"
print(favorit_sport)

del favorit_sport["Rebecca Clarke"]

a_list = [1,2]
b_list = [3,4]
c_list= a_list+b_list
print(c_list)

print(len(favorit_sport))
#exercise1
Foods={"soup,carrot meat", "freid meat, meat"}
print (Foods)

mongolian_dictionary={"do":"хийх", "pump":"шахуурга"}
print (mongolian_dictionary)

family_pet={"mother,dog", "sister,cat", "brother,zebra"}
print (family_pet)


Name_age={"Enhkee":"42", "Khulan":"24", "Ayana":"28"}
print (Name_age)




person_city = {"name": "Alice", "age": 25}
person_city["city"] = "UB"

print (person_city)

persons_age={"name": "Bob","age": 30} 

print (persons_age["name"])

del persons_age["age"]

print (persons_age )

colors = {"r": "red", "g": "green", "b": "blue"}

print (colors.keys(),colors.values())