from random import choice
from oopexercises import Dog  

class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(self.bark())  
        self.trained = True

    def play(self, *other_dogs):
        dog_names = ", ".join(dog.name for dog in other_dogs)
        print(f"{self.name}, {dog_names} all play together")

    def do_a_trick(self):
        if self.trained:
            tricks = [
                f"{self.name} does a barrel roll",
                f"{self.name} stands on his back legs",
                f"{self.name} shakes your hand",
                f"{self.name} plays dead"
            ]
            print(choice(tricks))  
        else:
            print(f"{self.name} is not trained yet and refuses to do a trick.")


pet_dog1 = PetDog("Buddy", 4, 22)
pet_dog2 = PetDog("Charlie", 3, 18)
pet_dog3 = PetDog("Rocky", 5, 25)


pet_dog1.train()
pet_dog1.play(pet_dog2, pet_dog3)
pet_dog1.do_a_trick()
pet_dog2.do_a_trick()  
