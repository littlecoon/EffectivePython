main.py
mypackage/__init__.py
mypackage/models.py
mypackage/utils.py

# main.py
form mypackage import utils

# main.py
from analysis.utils import log_base2_bucket
from frontend.utils import stringify

bucket = stringify(log_base2_bucket(33))


#main2.py
from analysis.utils import inspect
from fronted.utils import inspect   # Overwrites!


# main3.py
from analysis.utils import inspect as analysis_inspect
from frontend.utils import inspect as frontend_inspect

value = 33
if analysis_inspect(value) == frontend_inspect(value):
    print('Inspection equal!')


# models.py
__all__ = ['projectile']

class Projectile(object):
    def __init__(self, mass, velocity):
        self.mass = mass
        self.velocity = velocity


# utils.py
from .models import Projectile     

__all__ = ['simulate_collision']   

def _dot_product(a,b):
    # ...

def simulate_collision(a,b):
    # ...


# __init__.py
__all__ = []
from . models import *
__all__ += models.__all__
from .utils import *
__all__ += utils.__all__


# api_consumer.py
from mypackage import *

a = Projectile(1.5,3 )
b = Projectile(4, 1.7)
after_a, after_b = simulate_collision(a, b)