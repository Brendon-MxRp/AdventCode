def day1(file):
    with open(file, 'r') as tfile:
        elf_Data = tfile.read()
    lines = elf_Data.strip().split('\n')
    elves_Calories = []
    current_Elf_Calories = []
    for line in lines:
        if line == "":
            elves_Calories.append(current_Elf_Calories)
            current_Elf_Calories = []
        else:
            current_Elf_Calories.append(int(line))
    total_Calories_Per_Elf = [sum(calories) for calories in elves_Calories]
    max_Calories = max(total_Calories_Per_Elf)
    index_Max_Calories = total_Calories_Per_Elf.index(max_Calories)
    print("Elf carrying the most Calories:", index_Max_Calories + 1)
    print("Total Calories carried by the Elf:", max_Calories)

def day2(file):
    def play_round(player_Choice, opponent_Choice):
        if (player_Choice, opponent_Choice) in[('X', 'C'), ('Y', 'A'), ('Z', 'B')]:
            return 6
        if (player_Choice, opponent_Choice) in [('X', 'A'), ('Y', 'B'), ('Z', 'C')]:
            return 3
        return 0
    score = 0

    with open(file, 'r') as tfile:
        for line in tfile:
            opponent_Choice, player_Choice = line.strip().split()
            round_Score = play_round(player_Choice, opponent_Choice)
            score += round_Score
            if player_Choice == 'X': score += 1
            if player_Choice == 'Y': score += 2
            if player_Choice == 'Z': score += 3

    print("Total score:", score)

def day3(file):
    def calculate_Priority(item_Type):
        if 'a' <= item_Type <= 'z':
            return ord(item_Type) - ord('a') + 1
        elif 'A' <= item_Type <= 'Z':
            return ord(item_Type) - ord('A') + 27
        else:
            raise ValueError("Invalid item type: " + item_Type)

    def find_Common(rucksack):
        first_compartment = rucksack[:len(rucksack) // 2]
        second_compartment = rucksack[len(rucksack) // 2:]
        
        common_Item = set(first_compartment) & set(second_compartment)
        return common_Item.pop()

    with open(file) as tfile:
        rucksack_list = tfile.readlines()

    sum_Priorities = 0
    for rucksack in rucksack_list:
        common_Item = find_Common(rucksack)
        priority = calculate_Priority(common_Item)
        sum_Priorities += priority

    print("Sum of priorities of common item types:", sum_Priorities)

def day4(file):
    with open(file, 'r') as tFile:
        lines = tFile.readlines()
    assignment_Pairs = [entry.strip() for entry in lines]
    def is_A_in_B(range_A, range_B):
        start_A, end_A = map(int, range_A.split('-'))
        start_B, end_B = map(int, range_B.split('-'))
        return start_B <= start_A and end_A <= end_B
    number_Contains = 0
    for assignment_Pair in assignment_Pairs:
        first_Range, second_Range = assignment_Pair.split(',')
        if is_A_in_B(first_Range, second_Range) or is_A_in_B(second_Range, first_Range):
            number_Contains += 1
    print(number_Contains)

def day5(file):
    class CreateStack:
        def __init__(self) -> None:
            self.content = []

        def add_Item_Top(self, item):
            self.content.append(item)

        def take_X_Crates(self, x):
            return_Crates = self.content[-x:]
            self.content = self.content[:-x]
            return reversed(return_Crates)
        
        def add_Crates(self, new_crates):
            self.content += new_crates

        def get_Top_Content(self):
            return self.content[-1] if len(self.content) > 0 else ""
    
    class Cargo:
        def __init__(self, number_Crates):
            self.number_Crates = number_Crates
            self.crates = [CreateStack() for _ in range(number_Crates)]

        def add_Items_To_Crates(self, items):
            for crate, item in zip(self.crates, items):
                if item != ' ':
                    crate.add_Item_Top(item)

        def move_Items(self, amount, source, target):
            moving_Crates = self.crates[source].take_X_Crates(amount)
            self.crates[target].add_Crates(moving_Crates)

        def get_Stacks_Ontop(self):
            return_Message = ""
            for crate in self.crates:
                return_Message += crate.get_Top_Content()
            return return_Message

    with open(file, 'r') as tFile:
        lines = tFile.readlines()
    lines = [entry for entry in lines]
    
    number_of_crates = len(lines[0])//4
    cargo_bay = Cargo(number_of_crates)
    
    crate_lines = lines[:lines.index('\n')-1]
    for line in reversed(crate_lines):
        items = list(line)[1:-1:4]
        cargo_bay.add_Items_To_Crates(items)
    moving_lines = lines[lines.index('\n')+1:]
    for line in moving_lines:
        amount, source, target = [int(entry) for entry in line.strip().split(' ') if entry.isdigit()]
        cargo_bay.move_Items(amount, source-1, target-1)
    
    print(cargo_bay.get_Stacks_Ontop())

day5(r'SupplyStacks.txt')