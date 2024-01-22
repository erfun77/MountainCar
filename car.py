import gym
import numpy as np
import random
import pickle

env = gym.make("MountainCar-v0", new_step_api=True, render_mode='human')

LEARNING_RATE = 0.1
DISCOUNT = 0.95
EPISODES = 3500
SHOW_EVERY = 2000

DISCRETE_OS_SIZE = [20, 20]
discrete_os_win_size = (env.observation_space.high - env.observation_space.low) / DISCRETE_OS_SIZE
q_table = np.random.uniform(low=-2, high=0, size=(DISCRETE_OS_SIZE + [env.action_space.n]))


########## IN CASE YOU ARE NOT TRAINING THE MODEL##############
# f = open('mountain_car.pkl', 'rb')
# q_table = pickle.load(f)
# f.close()
###############################################################

def get_discrete_state(state):
    discrete_state = (state - env.observation_space.low) / discrete_os_win_size
    return tuple(discrete_state.astype(np.int))


''''  Another solution to digitize

# pos_space = np.linspace(env.observation_space.low[0], env.observation_space.high[0], 20)    # Between -1.2 and 0.6
# vel_space = np.linspace(env.observation_space.low[1], env.observation_space.high[1], 20)
# state = env.reset()    # Starting position, starting velocity always 0
# state_p = np.digitize(state[0], pos_space)
# state_v = np.digitize(state[1], vel_space)

'''

epsilon = 0.95
epsilon_decay_rate = 2/EPISODES   
rewards = []

for episodes in range(EPISODES):
  
  discrete_state = get_discrete_state(env.reset())
  done = False
  rewards_current_episode = 0
  
  for steps in range(200):
      
      rand = random.uniform(0, 1)

      ###########IN CASE YOU WANT TO SAVE YOUR TRAINED MODEL##############
      if rand > epsilon:
        action = np.argmax(q_table[discrete_state])
      else:
        action = env.action_space.sample()
      ####################################################################
        
      #action = np.argmax(q_table[discrete_state])  # if you are using Q-values file uncomment this line

      new_state, reward, done, _ , _ = env.step(action)
      new_discrete_state = get_discrete_state(new_state)

      # comment this line if you are using Q-values file
    
      q_table[discrete_state + (action,)] = q_table[discrete_state + (action,)] * (1 - LEARNING_RATE) + \
        LEARNING_RATE * (reward + DISCOUNT * np.max(q_table[new_discrete_state]))

      discrete_state = new_discrete_state
      rewards_current_episode += reward

      if done == True:
          print('We made it!')
          break


      
  print("------------Episode----------", episodes)
  epsilon = max(epsilon - epsilon_decay_rate, 0)
  rewards.append(rewards_current_episode) 
  print("rewards:", rewards_current_episode/200)
 

env.close()

##############IN CASE YOU WANT TO SAVE YOUR TRAINED MODEL##############
f = open('mountain_car.pkl','wb')
pickle.dump(q_table, f)
f.close()
######################################################################



