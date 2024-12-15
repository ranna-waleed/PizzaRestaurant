# SOLID Principles and Design Patterns

## Decorator Pattern
- **Open/Closed Principle**: New toppings can be added without modifying existing code.
- **Single Responsibility Principle**: Each topping class has a single responsibility.

### Code Example
```python
class Cheese(ToppingDecorator):
    def get_description(self) -> str:
        return self._pizza.get_description() + ", Cheese"

    def get_cost(self) -> float:
        return self._pizza.get_cost() + 1.0
```
## Factory Pattern
- **Single Responsibility Principle**: Separates pizza creation from the main logic.
- **Open/Closed Principle**: New pizza types can be added without modifying existing code.

### Code Example
```python
class PizzaFactory:
    @staticmethod
    def create_pizza(pizza_type: str) -> Pizza:
        if pizza_type == "1":
            return Margherita()
        elif pizza_type == "2":
            return Pepperoni()
        else:
            return None
```

## Singleton Pattern
- **Single Responsibility Principle**: Ensures a single instance of inventory manager.
- **Dependency Inversion Principle**: High-level modules depend on abstraction of inventory manager.

### Code Example
```python
class InventoryManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(InventoryManager, cls).__new__(cls)
        return cls._instance
```

## Strategy Pattern
- **Open/Closed Principle**: New payment methods can be added without modifying existing code.
- **Single Responsibility Principle**: Each payment method class has a single responsibility.

### Code Example
```python
class PayPalPayment(PaymentStrategy):
    def pay(self, amount: float):
        print(f"Paid ${amount:.2f} using PayPal.")