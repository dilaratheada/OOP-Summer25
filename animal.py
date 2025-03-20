class Animal:
    def __init__(self, name, group, number_of_legs, skills):
        self.name = name
        self.group = group
        self.number_of_legs = number_of_legs
        self.skills = skills

    def show_skills(self):
        return f"{self.name} has the following skills: {', '.join(self.skills)}"

dog_dict = {
    'name': 'dog',
    'group': 'mammalia',
    'number_of_legs': 4,
    'skills': ['running', 'biting', 'swimming']
}

croc_dict = {
    'name': 'crocodile',
    'group': 'reptilia',
    'number_of_legs': 4,
    'skills': ['holding breath under water', 'strong jaw', 'predator']
}

human_dict = {
    'name': 'human',
    'group': 'mammalia',
    'number_of_legs': 2,
    'skills': ['walking', 'talking', 'thinking']
}

chic_dict = {
    'name': 'chicken',
    'group': 'aves',
    'number_of_legs': 2,
    'skills': ['partially fly', 'clucking', 'eating']
}

fish_dict = {
    'name': 'fish',
    'group': 'vertebrates',
    'number_of_legs': 0,
    'skills': ['no need for oxygen', 'swimming', 'seeing 360']
}

animals = [Animal(**data) for data in [dog_dict, croc_dict, human_dict, chic_dict, fish_dict]]

for animal in animals:
    print(animal.show_skills())
