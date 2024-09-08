fruit = input("Item: ").strip().title()

calorie_table = {
        "Banana":"110",
        "Apple":"130",
        "Lemon":"15",
        "Lime":"20",
        "Plums":"70"

}
calorie = dict.fromkeys(["Cantaloupe","Avocado","Honeydew Melon","Tangerine","Pineapple","Strawberries"], "50") | dict.fromkeys(["Grapefruit","Nectarine","Peach"],"60")|dict.fromkeys(["Grapes","Kiwifruit"],"90")|dict.fromkeys(["Orange","Watermelon"],"80")|dict.fromkeys(["Sweet Cherries","Pear"],"100")
calorie.update(calorie_table)
if fruit in calorie:
    print("Calories:",calorie.get(fruit,""))
