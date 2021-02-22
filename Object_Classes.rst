
.. code:: ipython3

    # int: 1,2,324
    # float: 23.45, 54.56, 0.4345
    # String: "a", 'anmns', 'u r awsome'
    # List: [1,2,'asd']
    # Dictionary: {"name":"Jassy", "address":"Jupiter","sunsign":"libra"}
    # Bool: False, True
    # Each is an Object
    #     Class has data attribute and methods
    


.. code:: ipython3

    class Circle(object): #define a class
        def __init__(self, radius, color): #data attributes used to initialize each instance of class
            self.radius = radius;
            self.color = color;
            
        def add_radius(self,r):
            self.radius += r
            print(self.radius)
    
    class Rectangle(object):
        def __init__(self, color, height, width):
            self.height = height;
            self.width = width;
            self.color = color;
    
    c1 = Circle(10,"red") #create an object 
    c2 = Circle # create another object of type Circle
    c2.color = "blue" 
    c2.radius = 12
    print(c1.add_radius(8))
    print(c2.color)


.. parsed-literal::

    18
    None
    blue


.. code:: ipython3

    # Set a default value to constructors
    class Circle(object): #define a class
        def __init__(self, radius=3, color='red'): #data attributes used to initialize each instance of class
            self.radius = radius;
            self.color = color;
            
        def add_radius(self,r):
            self.radius += r
            print(self.radius)
        def drawCircle(self):
            BC = Circle()
            BC.drawCircle()

.. code:: ipython3

    # Using the Class Car in the lab, create a Car object with the following attributes:
    # make="Honda"
    # model="Accord"
    # color="blue"
    
    # Car(make="Honda",model="Accord",color="blue")
    # Car("Honda","Accord","blue")
    # Car(model="Accord",make="Honda",color="blue")
            


::


      File "<ipython-input-4-c5212d0d008f>", line 1
        Using the Class Car in the lab, create a Car object with the following attributes:
                ^
    SyntaxError: invalid syntax



.. code:: ipython3

    x=1
    if(x!=1):
        print('Hello')
    else:
        print('Hi')
    print('Mike')


.. parsed-literal::

    Hi
    Mike


.. code:: ipython3

    A=['1','2','3']
    for a in A:
        print(2*a)


.. parsed-literal::

    11
    22
    33


.. code:: ipython3

    def Delta(x):
        if x==0:
            y=1;
        else:
            y=0;
        return(y)
    Delta(0)




.. parsed-literal::

    1



.. code:: ipython3

    B=[3,2,1]
    B.sort()
    print(B)


.. parsed-literal::

    [1, 2, 3]


