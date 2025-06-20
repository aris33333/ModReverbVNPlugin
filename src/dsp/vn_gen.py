import numpy as np
import matplotlib.pyplot as plt

def generate(length, density, fs):
    num_impulses = int(density * length)
    ir = np.zeros(int(fs * length))
    
    positions = np.random.choice(len(ir), num_impulses, replace=False)
    signs = np.random.choice([-1, 1], num_impulses)
    ir[positions] = signs
    
    t = np.linspace(0, length, len(ir))
    decay = np.exp(-6.91 * (t / length) ** 0.5) 
    ir *= decay
    
    return ir

velvet_ir = generate(3.0, 5000, 48000)

plt.figure(figsize=(8, 6))
plt.plot(velvet_ir[:5000]) 
plt.title("Velvet Noise Impulse Response")
plt.xlabel("Samples")
plt.ylabel("Amplitude")
plt.grid()
plt.show()