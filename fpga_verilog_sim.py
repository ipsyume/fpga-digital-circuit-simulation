# fpga_verilog_sim.py
# Basic FPGA digital circuit design simulated in Python:
# - Logic gates (AND, OR, NOT, XOR)
# - 1-bit full adder
# - 4-bit ripple-carry adder
# - Testbench stimulus
# - Waveform visualization (matplotlib)

import numpy as np
import matplotlib.pyplot as plt

# -------------------------------
# Logic Gate Definitions (1-bit)
# -------------------------------
def AND(a, b):
    return (a & b) & 1

def OR(a, b):
    return (a | b) & 1

def NOT(a):
    return (~a) & 1

def XOR(a, b):
    return (a ^ b) & 1

# -------------------------------
# 1-bit Full Adder
# sum = a ^ b ^ cin
# cout = (a & b) | ((a ^ b) & cin)
# -------------------------------
def full_adder(a, b, cin):
    s = XOR(XOR(a, b), cin)
    cout = OR(AND(a, b), AND(XOR(a, b), cin))
    return s, cout

# -------------------------------
# 4-bit Ripple Carry Adder
# Bits ordered LSB -> MSB
# -------------------------------
def four_bit_adder(a_bits, b_bits, cin=0):
    if len(a_bits) != 4 or len(b_bits) != 4:
        raise ValueError("a_bits and b_bits must be 4-bit lists [b0,b1,b2,b3].")
    sum_bits = []
    carry = cin
    for i in range(4):
        s, carry = full_adder(a_bits[i], b_bits[i], carry)
        sum_bits.append(s)
    return sum_bits, carry

# -------------------------------
# Utility: Convert integer to 4-bit list [b0..b3]
# -------------------------------
def int_to_bits4(x):
    return [(x >> i) & 1 for i in range(4)]

def bits4_to_int(bits):
    return sum((bits[i] & 1) << i for i in range(4))

# -------------------------------
# Testbench Stimulus Generation
# Produces sequences of 4-bit inputs over time
# -------------------------------
def generate_stimulus():
    # Example sequence: sweep A from 0..15, B from a pattern
    A_seq = [int_to_bits4(a) for a in range(0, 16, 3)]  # step through A
    B_seq = [int_to_bits4(b) for b in [1, 3, 7, 8, 12, 15, 2]]  # fixed pattern for B
    # Repeat shorter list to match length
    max_len = max(len(A_seq), len(B_seq))
    if len(A_seq) < max_len:
        A_seq = (A_seq * ((max_len // len(A_seq)) + 1))[:max_len]
    if len(B_seq) < max_len:
        B_seq = (B_seq * ((max_len // len(B_seq)) + 1))[:max_len]
    return A_seq, B_seq

# -------------------------------
# Simulation: Evaluate adder per time step
# -------------------------------
def run_simulation():
    A_seq, B_seq = generate_stimulus()
    results = []
    for t, (A, B) in enumerate(zip(A_seq, B_seq)):
        SUM, COUT = four_bit_adder(A, B, cin=0)
        results.append({
            "t": t,
            "A": A,
            "B": B,
            "SUM": SUM,
            "COUT": COUT,
            "A_int": bits4_to_int(A),
            "B_int": bits4_to_int(B),
            "SUM_int": bits4_to_int(SUM)
        })
    return results

# -------------------------------
# Waveform Visualization
# -------------------------------
def plot_waveforms(results, save_path="fpga_adder_waveform.png"):
    time = np.arange(len(results))
    # Extract bit streams
    def stream(key, bit=None):
        if bit is None:
            return [r[key] for r in results]
        return [r[key][bit] for r in results]

    plt.figure(figsize=(10, 8))
    # Plot SUM[0..3]
    for i in range(4):
        plt.step(time, stream("SUM", i), where="mid", label=f"SUM[{i}]")
    # Plot COUT
    plt.step(time, [r["COUT"] for r in results], where="mid", label="COUT", linewidth=2, color="red")

    plt.title("4-bit Ripple Carry Adder Waveforms")
    plt.xlabel("Time step")
    plt.ylabel("Logic level")
    plt.ylim(-0.2, 1.2)
    plt.grid(True, which="both", axis="x", linestyle="--", alpha=0.3)
    plt.legend(loc="upper right")
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()
    return save_path

# -------------------------------
# Pretty Print Simulation Table
# -------------------------------
def print_results(results):
    print("t |   A (dec)   B (dec)  |  SUM (dec)  |  Bits: A  +  B  =  SUM  | COUT")
    print("--+----------------------+-------------+-------------------------+-----")
    for r in results:
        A_str = "".join(str(bit) for bit in reversed(r["A"]))
        B_str = "".join(str(bit) for bit in reversed(r["B"]))
        S_str = "".join(str(bit) for bit in reversed(r["SUM"]))
        print(f"{r['t']:2d}|     {r['A_int']:2d}        {r['B_int']:2d}     |     {r['SUM_int']:2d}     |   {A_str} + {B_str} = {S_str}  |  {r['COUT']}")

# -------------------------------
# Main
# -------------------------------
if __name__ == "__main__":
    results = run_simulation()
    print_results(results)
    img_path = plot_waveforms(results)
    print(f"\nWaveform saved to: {img_path}")
    print("\nSimulation complete.")
