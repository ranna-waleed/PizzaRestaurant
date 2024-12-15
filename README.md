# Pizza Restaurant Ordering System

## Overview
This project provides a basic ordering system for pizza restaurants. Customers can design their pizzas with different toppings and select a payment option. 

## Features
- Create Margherita and Pepperoni pizzas.
- Add toppings dynamically (Cheese, Olives, Mushrooms).
- Calculate and display the total cost of the pizza.
- Choose between PayPal and Credit Card payment methods.
- Manage ingredient inventory with a singleton inventory manager.

## Design Patterns Used
- Factory Pattern
- Decorator Pattern
- Singleton Pattern
- Strategy Pattern

## SOLID Principles
The project adheres to SOLID principles to ensure clean and maintainable code.

## Setup

### Prerequisites
- Python 3.x

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/ranna-waleed/PizzaRestaurant
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
3. Install the required packages (if any):
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Navigate to the `src` directory:
   ```bash
   cd src
   ```

2. Run the main program:
   ```bash
   python main.py
   ```

3. Follow the prompts to create and customize your pizza, and choose a payment method.

## Running Tests
1. Navigate to the root directory of the project:
   ```bash
   cd PizzaRestaurant
   ```

2. Run all tests:
   ```bash
   python -m unittest discover -s tests
   ```

## Documentation
- **Design Patterns**: Detailed explanations of the design patterns used can be found in `docs/DesignPatterns.md`.
- **SOLID Principles**: How the design patterns adhere to SOLID principles is explained in `docs/SOLID_DP.md`.

