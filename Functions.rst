
.. code:: ipython3

    a =5
    def add1(a):
        b=a+1
        return b
    add1(a)




.. parsed-literal::

    6



.. code:: ipython3

    def add1(a):
        b=a+1
        pass
    add1(5)


.. code:: ipython3

    list = [1,2,3,4,5]
    def printstuff(stuff):
        for i,s in enumerate(stuff):
            print("Index", i , "Value is ",s)
    printstuff(list)        


.. parsed-literal::

    Index 0 Value is  1
    Index 1 Value is  2
    Index 2 Value is  3
    Index 3 Value is  4
    Index 4 Value is  5


.. code:: ipython3

    Artist = ("MJ", "JJ", "PF")
    def artname(*names):
        for n in names:
            print(n)
    artname(Artist)        


.. parsed-literal::

    ('MJ', 'JJ', 'PF')


.. code:: ipython3

    a=1
    def add(b):
        return a+b
    c=add(10)
    print(c)


.. parsed-literal::

    11


.. code:: ipython3

    #this is invalid function
    def f(*x):
        return sum(c)



