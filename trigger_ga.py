from genetic_algorithm import GeneticAlgo;
import random;
from environment import Environment;

def calc_dist(point_1, point_2):
    #euclidean dist
    return ((point_1[0] - point_2[0]) ** 2 + (point_1[1] - point_2[1]) ** 2) ** 0.5;

def calc_total_dist(params):
    planet_order = params["individual"];
    
    planet_positions = params["planet_positions"];
    
    total_dist = 0;
    
    for i in range(len(planet_order) - 1):
        curr_planet_number = planet_order[i];
        next_planet_number = planet_order[i + 1];
        
        dist = calc_dist(planet_positions[curr_planet_number], planet_positions[next_planet_number]);
        
        total_dist = total_dist + dist;
    
    return total_dist;

total_population = 5;
total_planets = 6;
total_generations = 50;
mutation_chance = 25;

all_unique_individuals = True;
minimize = True;

fitness_function_default_params = {};

planet_positions = [];

for i in range(total_planets):
    planet_positions.append(random.sample(range(0, 100), 2));
    
fitness_function_default_params["planet_positions"] = planet_positions;

print("planet_positions:", planet_positions)

ga = GeneticAlgo(total_population, total_planets, all_unique_individuals, total_generations, mutation_chance, calc_total_dist, fitness_function_default_params, minimize);
ga.optimize();