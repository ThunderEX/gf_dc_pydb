.. _query:

Query
=====

This tool can support simply query method rather than open database with Microsoft Access.

1. In run.py, you can modify the code as below:

.. code-block:: python

    # -*- coding: utf-8 -*-
    from scripts.tables import *
    
    if __name__ == '__main__':
        x = QuantityType()
        x.query()

After run this script, you can get the console output:

.. code-block:: console

    +-----+----------------------------+
    |  id |            Name            |
    +-----+----------------------------+
    |  0  |         Q_NO_UNIT          |
    |  1  |           Q_FLOW           |
    |  2  |          Q_ENERGY          |
    |  3  |       Q_TEMPERATURE        |
    |  4  | Q_DIFFERENCIAL_TEMPERATURE |
    |  5  |          Q_HEIGHT          |
    |  6  |          Q_DEPTH           |
    |  7  |           Q_HEAD           |
    |  8  |         Q_PRESSURE         |
    |  9  |  Q_DIFFERENCIAL_PRESSURE   |
    |  10 |         Q_VOLTAGE          |
    |  11 |       Q_LOW_CURRENT        |
    |  12 |     Q_SPECIFIC_ENERGY      |
    |  13 |          Q_POWER           |
    |  14 |         Q_COS_PHI          |
    |  15 |          Q_VOLUME          |
    |  16 |         Q_PERCENT          |
    |  17 |           Q_TIME           |
    |  18 |         Q_PH_VALUE         |
    |  19 |        Q_FREQUENCY         |
    |  20 |        Q_REVOLUTION        |
    |  21 |       Q_PERFORMANCE        |
    |  22 |        Q_RESISTANCE        |
    |  23 |           Q_AREA           |
    |  24 |       Q_CONDUCTIVITY       |
    |  25 |          Q_FORCE           |
    |  26 |          Q_TORQUE          |
    |  27 |         Q_VELOCITY         |
    |  28 |           Q_MASS           |
    |  29 |       Q_ACCELERATION       |
    |  30 |        Q_MASS_FLOW         |
    |  31 |     Q_ANGULAR_VELOCITY     |
    |  32 |   Q_ANGULAR_ACCELERATION   |
    |  33 |    Q_LUMINOUS_INTENSITY    |
    |  34 |        Q_CLOCK_HOUR        |
    |  35 |       Q_CLOCK_MINUTE       |
    |  36 |        Q_CLOCK_DAY         |
    |  37 |       Q_CLOCK_MONTH        |
    |  38 |        Q_CLOCK_YEAR        |
    |  39 |         Q_TIME_SUM         |
    |  40 |          Q_RATIO           |
    |  41 |       Q_MAC_ADDRESS        |
    |  42 |        Q_DATA_SIZE         |
    |  43 |         Q_DATETIME         |
    |  44 |       Q_HIGH_CURRENT       |
    |  45 |        Q_SMALL_AREA        |
    |  46 |      Q_HIGH_VELOCITY       |
    | 100 |        Q_LAST_UNIT         |
    |  47 |    Q_PARTS_PER_MILLION     |
    |  48 |          Q_LEVEL           |
    +-----+----------------------------+


2. With condition query, write code as below

.. code-block:: python

    # -*- coding: utf-8 -*-
    from scripts.tables import *
    
    if __name__ == '__main__':
        x = QuantityType()
        x.query(id=100)


Output:

.. code-block:: console

    +-----+-------------+
    |  id |     Name    |
    +-----+-------------+
    | 100 | Q_LAST_UNIT |
    +-----+-------------+


3. Fuzzy search 

.. code-block:: python

    # -*- coding: utf-8 -*-
    from scripts.tables import *
    
    if __name__ == '__main__':
        x = QuantityType()
        x.query(Name__icontains='Q_L')


Output:

.. code-block:: console

    +-----+----------------------+
    |  id |         Name         |
    +-----+----------------------+
    |  11 |    Q_LOW_CURRENT     |
    |  33 | Q_LUMINOUS_INTENSITY |
    | 100 |     Q_LAST_UNIT      |
    |  48 |       Q_LEVEL        |
    +-----+----------------------+
