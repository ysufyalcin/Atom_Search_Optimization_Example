import random

# Constants
num_days = 7  # Tatil günü sayısı
budget = 500  # Tatil için bütçe
num_atoms = 20  # Atom sayısı
num_iterations = 100  # İterasyon sayısı

# Vacation activities and their costs (example data)
activities = {
    'Beach': 50,
    'Hiking': 30,
    'City Tour': 40,
    'Museum Visit': 20,
    'Restaurant': 60,
    'Amusement Park': 70,
    'Shopping': 50,
    'Spa Day': 90
}

# Initializing Atom Positions
def initialize_atoms(num_atoms, num_days, activities):
    atoms = []
    for _ in range(num_atoms):
        atom = random.choices(list(activities.keys()), k=num_days)
        atoms.append(atom)
    return atoms

# Evaluating Atoms Using the Objective Function
def evaluate_atom(atom, activities, budget):
    total_cost = sum(activities[activity] for activity in atom)
    if total_cost <= budget:
        return len(atom) 
    else:
        return 0

# Finding the Best Atom
def find_best_atom(atoms, activities, budget):
    best_atom = max(atoms, key=lambda atom: evaluate_atom(atom, activities, budget))
    return best_atom

# Mutating Atoms
def mutate_atom(atom, activities, budget):
    mutated_atom = atom.copy()
    day_to_mutate = random.randint(0, num_days - 1)
    available_activities = [activity for activity in activities.keys() if activities[activity] <= budget]
    mutated_activity = random.choice(available_activities)
    mutated_atom[day_to_mutate] = mutated_activity
    return mutated_atom

# Atomic Search Algorithm
def atom_search(activities, budget, num_atoms, num_days, num_iterations):
    atoms = initialize_atoms(num_atoms, num_days, activities)
    best_atom = find_best_atom(atoms, activities, budget)

    for iteration in range(num_iterations):
        new_atoms = [mutate_atom(atom, activities, budget) for atom in atoms]
        new_best_atom = find_best_atom(new_atoms, activities, budget)
         
        # daha iyi atom bulursa güncelle
        if evaluate_atom(new_best_atom, activities, budget) > evaluate_atom(best_atom, activities, budget):
            best_atom = new_best_atom
            print(f"Iteration {iteration}: Best atom updated. Fitness: {evaluate_atom(best_atom, activities, budget)}")

    return best_atom

# Main Process
best_solution = atom_search(activities, budget, num_atoms, num_days, num_iterations)

# Show results
print("Best vacation plan:")
for i, activity in enumerate(best_solution):
    print(f"Day {i + 1}: Activity: {activity}, Cost: {activities[activity]}")

total_cost = sum(activities[activity] for activity in best_solution)
print("Total Cost:", total_cost)
