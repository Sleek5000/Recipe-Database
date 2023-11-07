
class Recipe:
    def __init__(self,
                 name="",
                 course="",
                 ingredients="",
                 instructions="",
                 time="",
                 portions=0,
                 kidfriendly=0,
                 ):
        self.name = name
        self.course = course
        self.ingredients = ingredients
        self.instructions = instructions
        self.time = time
        self.portions = portions
        self.kidfriendly = kidfriendly


    def addRecipe(self):
        pass

    def viewRecipes(self):
        pass
