from genetic_algorithm import GeneticAlgo;
import random;
from environment import Environment;

def calc_dist(point_1, point_2):
    #euclidean dist
    return ((point_1[0] - point_2[0]) ** 2 + (point_1[1] - point_2[1]) ** 2) ** 0.5;

def calc_total_dist(params):
    planet_order = params["individual"];
    env = params["env"];
    
    env.reset();
    
    total_dist = 0;
    
    for planet in planet_order:
        
        dist = env.step(planet, "none");
        
        # print("dist:",dist)
        
        total_dist = total_dist + dist;
    
    return total_dist;

def display_path(params):
    planet_order = params["individual"];
    env = params["env"];
    
    env.reset();
    
    for planet in planet_order:
        
        _ = env.step(planet, "normal");
        
def display_flight(fittest_path, env):
    env.reset();
    
    for planet in fittest_path:
        
        _ = env.step(planet, "beautiful");

total_population = 5;
# total_planets = 6;
total_generations = 500;
mutation_chance = 10;

all_unique_individuals = True;
minimize = True;

env = Environment();
total_planets = len(env.planets);

fitness_function_default_params = {};
fitness_function_default_params["env"] = env;

# planet_positions = [];

# for i in range(total_planets):
#     planet_positions.append(random.sample(range(0, 100), 2));
    
# fitness_function_default_params["planet_positions"] = planet_positions;

# print("planet_positions:", planet_positions)

ga = GeneticAlgo(total_population, total_planets, all_unique_individuals, total_generations, mutation_chance, calc_total_dist, fitness_function_default_params, display_path, minimize);
fittest_individual, fittest_value = ga.optimize();

display_flight(fittest_individual, env);