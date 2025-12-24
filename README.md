# FPGA Digital Circuit Simulation (Python-Based)

This project simulates fundamental FPGA-style digital circuits using Python. It focuses on understanding digital logic design concepts such as logic gates, adders, carry propagation, and waveform analysis through a testbench-style simulation.

---

## Overview
Digital circuits form the foundation of FPGA and hardware system design. This project demonstrates how basic combinational logic and arithmetic circuits work internally by simulating their behavior step-by-step and visualizing signal transitions over time.

Although implemented in Python, the design mirrors how such circuits are described and verified in hardware description languages like Verilog.

---

## Implemented Components
- Basic logic gates: AND, OR, NOT, XOR
- 1-bit Full Adder
- 4-bit Ripple Carry Adder
- Testbench-style input stimulus generation
- Waveform visualization of outputs over time

---

## Simulation Details
- Inputs are applied sequentially, similar to a hardware testbench
- Each time step evaluates the adder logic
- Outputs include:
  - Sum bits (SUM[0–3])
  - Carry-out (COUT)
- Waveforms are generated to visualize digital signal behavior

---

## Waveform Output
The simulation produces a waveform showing the evolution of output bits over time.

![Adder Waveform](results/fpga_adder_waveform.png)

---

## Project Structure
fpga-digital-circuit-simulation/
├── fpga_verilog_sim.py
├── README.md
├── requirements.txt
└── results/
└── fpga_adder_waveform.png

yaml
Copy code

---

## How to Run
```bash
pip install -r requirements.txt
python fpga_verilog_sim.py
The waveform image will be saved as:

bash
Copy code
results/fpga_adder_waveform.png
Key Concepts Demonstrated
Digital logic fundamentals

Full adder and ripple-carry adder design

Bit-level arithmetic operations

Carry propagation

Testbench-style simulation

Waveform analysis

Future Extensions
Verilog implementation of the same circuits

FPGA synthesis and hardware deployment

Multi-bit ALU design

Clocked sequential circuits

Timing analysis and propagation delay modeling

Notes
This project emphasizes conceptual clarity and digital design fundamentals rather than performance optimization.

yaml
Copy code

---

## 🧾 Commit message
Use this:
Initial commit – FPGA digital circuit simulation