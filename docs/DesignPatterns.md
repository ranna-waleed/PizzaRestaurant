# Design Patterns


## Decorator Pattern
- **Description**:Decorator Pattern allows behavior to be added to individual objects, dynamically, without affecting  behavior of other objects from same class.
- **Application**: Used to add toppings to pizzas dynamically.
- **Before**: Toppings were hardcoded, making it difficult to add new toppings.
- **After**: Toppings are added dynamically, making system more flexible and extensible.

### Code Example
```python
class Cheese(ToppingDecorator):
    def get_description(self) -> str:
        return self._pizza.get_description() + ", Cheese"

    def get_cost(self) -> float:
        return self._pizza.get_cost() + 1.0
```

## Factory Pattern
- **Description**: Factory Pattern is used to create objects without specifying exact class of the object that will be created.
- **Application**: Used to create Margherita and Pepperoni pizza objects.
- **Before**: Pizza creation logic was mixed with main program logic.
- **After**: Pizza creation is handled by PizzaFactory, improving maintainability and readability.

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
## Strategy Pattern
- **Description**: Strategy Pattern defines family of algorithms, encapsulates each one, and makes them interchangeable.
- **Application**: Used for payment methods (PayPal and Credit Card).
- **Before**: Payment logic was hardcoded, making it difficult to add new payment methods.
- **After**: Payment methods are encapsulated in their own classes, making it easy to add new methods.

### Code Example
```python
class PayPalPayment(PaymentStrategy):
    def pay(self, amount: float):
        print(f"Paid ${amount:.2f} using PayPal.")

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount: float):
        print(f"Paid ${amount:.2f} using Credit Card.")
```


## Singleton Pattern
- **Description**:Singleton Pattern ensures a class has only one instance and provides a global point of access to it.
- **Application**: Used for InventoryManager to manage ingredient availability.
- **Before**: Multiple instances of inventory manager could lead to inconsistent inventory states.
- **After**: A single instance of inventory manager ensures consistent inventory management.

### Code Example
```python
class InventoryManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(InventoryManager, cls).__new__(cls)
        return cls._instance
```

## Overengineering
- **Description**: Overengineering occurs when a system is made more complex than necessary.
- **Example**: Adding an unnecessary Observer pattern for inventory updates.

### Code Example
```python
class InventoryObserver(ABC):
    @abstractmethod
    def update(self, item: str):
        pass

class InventorySubject:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer: InventoryObserver):
        self._observers.append(observer)

    def remove_observer(self, observer: InventoryObserver):
        self._observers.remove(observer)

    def notify_observers(self, item: str):
        for observer in self._observers:
            observer.update(item)
