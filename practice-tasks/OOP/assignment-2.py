class Machines:
    def __init__(self, name):
        self.name = name
        print(f"The {self.name} has been initialized")
        
class Electric(Machines):
    def __init__(self, name, battery_percentage, **kwargs):
        super().__init__(name)
        # super().__init__(**kwargs)
        self._battery_percentage = battery_percentage
    def turn_on(self):
        print(f"{self.name} is now turned on")
    def turn_off(self):
        print(f"{self.name} is now turned off")        
    def check_battery(self):
        print(f"{self.name} has {self._battery_percentage}% battery left")
    
class Mechanical(Machines):
    def __init__(self, name, components, **kwargs):
        super().__init__(name)
        # super().__init__(**kwargs)
        self._components = components
    def number_of_components(self):
        print(f"Machine {self.name} has {self._components} components")
    
class Cleaning(Machines):
    def __init__(self, name, capacity, **kwargs):
        super().__init__(name)
        # super().__init__(**kwargs)
        self._capacity = capacity
    
    def get_capacity(self):
        return self._capacity
    
class Gardening(Machines):
    def __init__(self, name, use_case, **kwargs):
        super().__init__(name)
        self._use_case = use_case
    def get_use_case(self):
        return self._use_case
    
class Measuring(Machines):
    def __init__(self, name, range, **kwargs):
        super().__init__(name)
        # super().__init__(**kwargs)
        self._range = range
    def get_range(self):
        return self._range
      
class VaccumCleaner(Cleaning, Electric):
    def __init__(self, name, capacity, battery_percentage):
        super().__init__(name=name, capacity=capacity, battery_percentage=battery_percentage)
    def clean(self):
        print(f"Vaccum Cleaner {self.name} is being used to clean the house...")
    
    
class Scissors(Gardening, Mechanical):
    def __init__(self, name, use_case, components):
        super().__init__(name=name, use_case=use_case, components=components)
    def cut(self):
        print(f"{self.name} is being used to trim the bush...")
    
class LawnMower(Gardening, Electric):
    def __init__(self, name, use_case, components):
        super().__init__(name=name, use_case=use_case, components=components)
    def mow(self):
        print(f"{self.name} is being used to mow the grass in the lawn...")
    
class Balance(Measuring, Mechanical):
    def __init__(self, name, range, components):
        super().__init__(name=name, range=range, components=components)
    def measure(self):
        print(f"{self.name} is being used to measure the weights...")
    
class ElectricBalance(Measuring, Electric):
    def __init__(self, name, range, battery_percentage):
        super().__init__(name=name, range=range, battery_percentage=battery_percentage)
    def measure(self):
        print(f"{self.name} is being used to measure the weights...")
        
        
vc1 = VaccumCleaner(name="vc1", capacity="300 sq. ft.", battery_percentage=80)
vc1.turn_on()
vc1.check_battery()
vc1.clean()
vc1.turn_off()

b = Balance(name="b1", range="0-1000 kg", components=2)
b.measure()