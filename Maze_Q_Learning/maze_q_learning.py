import numpy as np;
from maze_q_learning_environment import Environment;

#defining the params
gamma = 0.9;
alpha = 0.75;
no_of_epochs = 10000;

#env and Q table initialization
env = Environment();
rewards = env.rewardBoard;

q_table = rewards.copy();

#preparing the q learning process
possible_states = list();

for i in range(rewards.shape[0]):
    if sum(abs(rewards[i])) != 0:
           possible_states.append(i);
           
def get_max_q_value(q_values):
    
    index_max_q_value = np.argmax(q_values);
    max_q_value = np.max(q_values);
    
    return index_max_q_value, max_q_value;


#train bot using q_learning
for i in range(no_of_epochs):
    print(f"Epoch {i + 1}");
    
    start_pos = np.random.choice(possible_states);
    
    #find all possible next position
    all_possible_next_states = [index for index, reward in enumerate(rewards[start_pos]) if reward != 0];
    
    action = np.random.choice(all_possible_next_states);
    
    reward = rewards[start_pos][action];
    
    #update q value
    __, max_q_value = get_max_q_value(q_table[action]);
    
    temp_diff = reward + gamma * max_q_value - q_table[start_pos][action];
    
    q_table[start_pos][action] = q_table[start_pos][action] + alpha * temp_diff;
    
#display results
current_pos = env.startingPos;

while True:
    action, __ = get_max_q_value(q_table[current_pos]);
    
    env.movePlayer(action);
    
    current_pos = action;