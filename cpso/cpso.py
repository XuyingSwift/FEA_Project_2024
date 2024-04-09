import numpy as np
import math

class Particle:
    def __init__(self, dim_bounds):
        self.position = np.array([np.random.uniform(low, high) for low, high in dim_bounds])
        self.velocity = np.random.rand(len(dim_bounds))
        self.best_position = np.copy(self.position)
        self.best_score = float('inf')

class SubSwarm:
    def __init__(self, num_particles, dim_bounds):
        self.particles = [Particle(dim_bounds) for _ in range(num_particles)]

def objective_function(x):
    # Extract the elements of the input vector x except the last one (xi)
    xi = x[:-1]
    # Extract the elements of the input vector x starting from the second element (xi+1)
    xi1 = x[1:]
    # Calculate the terms for each pair of xi and xi+1
    with np.errstate(over='ignore'):
        terms = ((xi ** 2) ** ((xi ** 2 + xi1 + 1) / (xi ** 2 + xi1)))
    # Sum up the terms and add the first element of the input vector (x0)
    result = terms.sum() + x[0]
    # Return the final result
    return result

def cooperative_pso(objective_function, bounds, num_particles, num_swarms, max_iter):
    dim = len(bounds)
    dims_per_swarm = dim // num_swarms
    sub_swarm_bounds = [bounds[i:i + dims_per_swarm] for i in range(0, dim, dims_per_swarm)]

    sub_swarms = [SubSwarm(num_particles, dim_bounds) for dim_bounds in sub_swarm_bounds]

    global_best_position = np.zeros(dim)
    global_best_score = float('inf')

    for t in range(max_iter):
        # Update global best position
        for i, swarm in enumerate(sub_swarms):
            start = i * dims_per_swarm
            end = start + dims_per_swarm
            for particle in swarm.particles:
                combined_position = np.copy(global_best_position)
                combined_position[start:end] = particle.position
                fitness = objective_function(combined_position)

                if fitness < particle.best_score:
                    particle.best_score = fitness
                    particle.best_position = np.copy(particle.position)

                if fitness < global_best_score:
                    global_best_score = fitness
                    global_best_position[start:end] = particle.position

        # Update velocities and positions
        for i, swarm in enumerate(sub_swarms):
            start = i * dims_per_swarm
            end = start + dims_per_swarm
            for particle in swarm.particles:
                r1, r2 = np.random.rand(2)
                cognitive_velocity = r1 * (particle.best_position - particle.position)
                social_velocity = r2 * (global_best_position[start:end] - particle.position)
                particle.velocity = particle.velocity + cognitive_velocity + social_velocity
                particle.position = particle.position + particle.velocity

    return global_best_position, global_best_score

bounds = [(-10, 10)] * 50
best_position, best_score = cooperative_pso(objective_function, bounds, num_particles=30, num_swarms=5, max_iter=100)

print("Best Position:", best_position)
print("Best Score:", best_score)
