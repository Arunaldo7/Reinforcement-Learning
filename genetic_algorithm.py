import numpy as np;
import random;


class GeneticAlgo:
    
    def __init__(self, total_population, total_genes, all_unique_individuals, total_generations, mutation_chance, fitness_function, fitness_function_default_params, 
                 after_generation_functaion, minimize):
        self.total_population = total_population;
        self.total_genes = total_genes;
        self.all_unique_individuals = all_unique_individuals;
        self.total_generations = total_generations;
        self.mutation_chance = mutation_chance;
        
        self.fitness_function = fitness_function;
        self.fitness_function_default_params = fitness_function_default_params;
        
        self.after_generation_functaion = after_generation_functaion;
        
        self.minimize = minimize;
        
        self.population_list = [];
        self.fitness_list = [];

    def init_population(self):
        for i in range(self.total_population):
            self.population_list.append(random.sample(range(0, self.total_genes, 1), self.total_genes));

    def calc_fitness_values(self, individuals_list):
        fitness_list = [];
        
        for individual in individuals_list:
            fitness_functaion_params = {};
            fitness_functaion_params["individual"] = individual;
            
            fitness_functaion_params.update(self.fitness_function_default_params);
            
            fitness_list.append(self.fitness_function(fitness_functaion_params));
            
        return fitness_list;
    
    def sort_population(self):
        self.fitness_list = self.calc_fitness_values(self.population_list);
        
        # print("self.fitness_list : ", self.fitness_list);
        # print("self.population_list : ", self.population_list);
        
        sorted_population_indices = list(np.argsort(self.fitness_list));
        self.fitness_list.sort();
        
        if not self.minimize:
            sorted_population_indices.reverse();
            self.fitness_list.reverse();
            
        temp_population = self.population_list.copy();
        self.population_list = [];
        
        for sorted_index in sorted_population_indices:
            self.population_list.append(temp_population[sorted_index]);
        
    def cross_over(self, parents_list):
        #randomize a gene for cross over
        cross_over_accepted = False;
        
        # print("parents_list : ", parents_list);
        
        parent_1 = parents_list[0].copy();
        parent_2 = parents_list[1].copy();
        
        while not cross_over_accepted:
            child = parent_1.copy();

            total_cross_over_genes =  random.randint(1, self.total_genes);

            parent_1_cross_over_indices = random.sample(range(self.total_genes), total_cross_over_genes);
            parent_2_cross_over_indices = random.sample(range(self.total_genes), total_cross_over_genes);
            
            # print("parent_1:",parent_1);
            # print("parent_2:",parent_2);
            
            # print("parent_1_indices:",parent_1_indices);
            # print("parent_2_indices:",parent_2_indices);
            
            for i in range(total_cross_over_genes):
                first_gene_index = parent_1_cross_over_indices[i];
                second_gene_index = parent_2_cross_over_indices[i]
                
                child[first_gene_index] = parent_2[second_gene_index];
            
            #find if duplicates in list
            if self.all_unique_individuals:
                if len(child) == len(set(child)):
                    cross_over_accepted = True;
            else:
                cross_over_accepted = True;
          
        # print("parent_1:",parent_1);
        # print("parent_2:",parent_2);
        
        # print("parent_1_indices:",parent_1_indices);
        # print("parent_2_indices:",parent_2_indices);
        
        # print("child:",child);
                  
        return child;
    
    def mutate(self, individual):
        mutation_accepted = False;
        while not mutation_accepted:
        
            mutation_index =  random.randint(0, self.total_genes - 1);
                    
            value_at_mutation_index = individual[mutation_index];
            
            #swap this value to index where the value is there
            new_value = random.randint(0, self.total_genes - 1);
            
            new_value_index = individual.index(new_value);
            
            if new_value_index != value_at_mutation_index:
                individual[mutation_index] = new_value;
                individual[new_value_index] = value_at_mutation_index;
                
                mutation_accepted = True;

        return individual;
        
        
    def optimize(self):
        self.population_list = [];
        
        #init population
        self.init_population();
        print("Init Population : ", self.population_list);
        
        self.sort_population();
        
        # print("Sorted Fitness values : ", self.fitness_list);
        # print("Sorted Population : ", self.population_list);
        
        for i in range(self.total_generations):
            print(f"Generation : {i+1}");
            
            child = self.cross_over(self.population_list);
            
            #mutate child
            random_number = random.randint(1, 100);
            
            if random_number <= self.mutation_chance:
                child = self.mutate(child);
            #to append child is not same as another individual
            if child not in self.population_list:
                self.population_list.append(child);
            
                #sort population after adding child
                self.sort_population();
                
                #delete last individual(unfittest of all)
                del self.population_list[self.total_population];
                del self.fitness_list[self.total_population];
                
            fitness_functaion_params = {};
            fitness_functaion_params["individual"] = self.population_list[0];
            
            fitness_functaion_params.update(self.fitness_function_default_params);
            
            self.after_generation_functaion(fitness_functaion_params);
            
            # print("Sorted Fitness values : ", self.fitness_list);
            # print("Sorted Population : ", self.population_list);
            
            fittest_individual = self.population_list[0];
            fittest_value = self.fitness_list[0];
            print(f"Fittest Individual : {fittest_individual} Fittest Value : {fittest_value:.2f}" );
            
        
        return fittest_individual, fittest_value;
        