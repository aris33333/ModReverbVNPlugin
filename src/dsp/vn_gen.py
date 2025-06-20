import numpy as np
import os
import matplotlib.pyplot as plt

def generate(length, density, fs):
    """
    Args: Length of the IR in seconds, 
          Density in Samples
          FS - Sampling Rate
    Returns: 
          Impulse Response of given length
    """
    num_impulses = int(density * length)
    ir = np.zeros(int(fs * length))
    
    positions = np.random.choice(len(ir), num_impulses, replace=False)
    signs = np.random.choice([-1, 1], num_impulses)
    ir[positions] = signs

    return np.array(ir).astype(float)

def export(ir_array, var_name, filename="IR.h"):
    path = "."
    full_path = os.path.join(path, filename)

    with open(filename, 'w') as f:
        f.write(f"constexpr float {var_name}[] = {{\n    ")
        f.write(", ".join(f"{x:.8f}f" for x in ir_array))
        f.write("\n};\n")
        f.write(f"constexpr int {var_name}_length = {len(ir_array)};\n")

    print(f"Impulse response exported to: {full_path}")

impulse_response = generate(5.0, 100.0, 48000.0)
export(impulse_response, "IR")

plt.figure(figsize=(12, 8))
plt.plot(impulse_response) 
plt.title("Velvet Noise Impulse Response")
plt.xlabel("Samples")
plt.ylabel("Amplitude")
plt.grid()
plt.show()