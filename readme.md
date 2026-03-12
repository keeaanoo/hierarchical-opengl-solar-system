# Hierarchical Solar System (OpenGL)

This project demonstrates **hierarchical modeling using OpenGL** with Python.

The simulation shows a simple solar system consisting of:

Sun → Earth → Moon

Earth orbits the Sun, and the Moon orbits the Earth.  
The program uses **OpenGL Matrix Stack (`glPushMatrix` and `glPopMatrix`)** to implement hierarchical transformations.

---

## Features

- Hierarchical modeling
- Matrix stack transformation
- Orbit animation
- Orbit visualization lines
- Keyboard-controlled camera

---

## Hierarchy Structure
Sun
└── Earth
  └── Moon


---

## Requirements

Python 3.8+  
PyOpenGL

Install dependencies: pip install PyOpenGL PyOpenGL_accelerate



---

## How to Run

Clone the repository: 
https://github.com/keeaanoo/hierarchical-opengl-solar-system.git


Go to the project folder: 
cd hierarchical-opengl-solar-system


Run the program: 
python main.py


---

## Camera Controls

| Key | Action |
|----|----|
| W | Move forward |
| S | Move backward |
| A | Move left |
| D | Move right |
| Q | Move up |
| E | Move down |

---

