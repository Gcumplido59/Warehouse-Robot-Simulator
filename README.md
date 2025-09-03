# Warehouse Robot Simulator 🤖

An interactive pathfinding visualizer built with Python and Pygame. This project allows users to design a custom warehouse layout with obstacles and then runs the Breadth-First Search (BFS) algorithm to find the shortest path for a robot to retrieve a package.

![Warehouse Robot Simulator Demo](https-placeholder-for-your-gif.gif)


## Features

* **Interactive Grid:** Design your own warehouse layout in real-time.
* **Object Placement:** Use your mouse to place and remove obstacles and the target package.
* **Pathfinding Algorithm:** Implements the Breadth-First Search (BFS) algorithm to guarantee the shortest path.
* **Dynamic Visualization:** The warehouse, robot, and final path are all rendered cleanly using Pygame.
* **Reset Functionality:** A UI button allows you to clear the grid and start a new design.

## Technologies Used

* **Python**: Core programming language.
* **Pygame**: For rendering the graphical user interface and handling user input.

## Setup and Installation

Follow these steps to run the project on your local machine.

**1. Clone the Repository**
```bash
git clone [https://github.com/your-username/Warehouse-Robot-Simulator.git](https://github.com/your-username/Warehouse-Robot-Simulator.git)
cd Warehouse-Robot-Simulator
```
**2. Create and Activate a Virtual Environment (Recommended)**

* **On macOS/Linux:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
* **On Windows:**
    ```bash
    py -m venv venv
    .\venv\Scripts\activate
    ```

**3. Install Dependencies**
The only dependency is Pygame.
```bash
pip install pygame
```

**4. Run the Application**
```bash
python main_visual.py
```

## How to Use

The application will launch in "Setup Mode."

* **Left Mouse Click**: Place an obstacle (`1`) on an empty square.
* **Right Mouse Click**: Place or move the package (`📦`) on an empty square.
* **Press `SPACE` Key**: After placing the package, press the spacebar to run the BFS algorithm and find the path.
* **"Reset" Button**: Click the button to clear all obstacles and the package, allowing you to create a new layout.

## Project Structure

The project is organized using Object-Oriented principles to separate logic from visualization.
```
Warehouse-Robot-Simulator/
├── main_visual.py       # Main entry point for the Pygame application
├── visualizer.py        # Contains the Visualizer class for Pygame rendering
├── warehouse.py         # Contains the Almacen (Warehouse) class and BFS logic
├── robot.py             # Contains the Robot class
└── package.py           # Contains the Package class
```

#Project made by Gael Cumplido
