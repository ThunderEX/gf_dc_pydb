.. _quickstart:

QuickStart
==========

This document presents a brief, high-level overview of DC Database Helper features. This guide will cover 2 examples:

* Add new headline label
* Add new subject

Example 1
---------

Here is a simple example to show how to use this tool. We want to add one label in **4. Settings screen**.

.. image:: example.png
    :align: center

1. Create new py file in scripts\\feature as example1.py and then add below code in this file.

.. code-block:: python
    :linenos:

    # -*- coding: utf-8 -*-
    from ..template.tpl import template
    from ..util.log import *
    
    def example1():
        comment('This is an example')
        t = template('LabelHeadline')
        t.description = '---------- Add headline text in 4. Settings ----------'
        t.label_name = '4. test headline'
        t.define_name = 'SID_TEST_HEADLINE'
        t.label_string = 'test headline'
        t.listview_id = '4. Settings List 1'
        t.save()

2. Open run.py and modify it as below:

.. code-block:: python
    :linenos:

    # -*- coding: utf-8 -*-
    from scripts.misc import copy_database, run_generators, ghs_build, vc_build
    from scripts.tables import *
    from scripts.feature.example1 import example1
    
    if __name__ == '__main__':
        example1()
        run_generators()
        vc_build()
        
3. Run run.py in windows command.

.. code-block:: console

    python run.py


Elaborate 1
^^^^^^^^^^^

**example1.py**

.. code-block:: python

    from ..template.tpl import template
    from ..util.log import *

1. There are a lot of templates in template directory, so the first step is import this module. And we also import log module because we need to output some log.

.. code-block:: python

    def example1():
        comment('This is an example')
        t = template('LabelHeadline')


2. We create new function named ``example1()``. In this function, we call ``comment()`` firstly so that it can output some comment in console. Then use ``template()`` we can get an instance of template. Here the instance is from **LabelHeadline**. Please read :ref:`template <template>` to get more details of templates.


.. code-block:: python

        t.description = '---------- Add headline text in 4. Settings ----------'
        t.label_name = '4. test headline'
        t.define_name = 'SID_TEST_HEADLINE'
        t.label_string = 'test headline'
        t.listview_id = '4. Settings List 1'


3. After creating new instance from template, we need set some attributes for this instance. Here are some explanation of attributes: 

+---------------+--------------------------------------------------------+
| attribute     | explanation                                            |
+===============+========================================================+
| description   | Add some description to output, it is optional         |
+---------------+--------------------------------------------------------+
| label_name    | define new component name in DisplayComponent table    |
+---------------+--------------------------------------------------------+
| define_name   | string define name in StringDefines table, all capital |
+---------------+--------------------------------------------------------+
| label_string  | the string which want to show on screen                |
+---------------+--------------------------------------------------------+
| listview_id   | the listview id where the new added text belongs       |
+---------------+--------------------------------------------------------+

.. code-block:: python

        t.save()

4. Finally, we should invoke the ``save()`` function to insert data into database.

**run.py**

.. code-block:: python

    # -*- coding: utf-8 -*-
    from scripts.misc import copy_database, run_generators, ghs_build, vc_build
    from scripts.tables import *
    from scripts.feature.example import example
    
5. In run.py, import the example module we just created.

.. code-block:: python

    if __name__ == '__main__':
        example()
        run_generators()
        vc_build()

6. In the main entry, we use ``example()`` to insert database, ``run_generators()`` to run factory, languange, web generators, and then use ``vc_build()`` to build vc project 'cu3x1AppPcSim_SRC\PcMrViewer\pc.sln'.


Example 2
---------

Second example is how to add one subject in Factory database.

1. First create new py file as example2.py, add below code in this file.

.. code-block:: python
    :linenos:

    # -*- coding: utf-8 -*-
    from ..template.tpl import template
    from ..util.log import *

    def example2():
        t = template('NewSubject')
        t.description = '---------- 加Subject: h2s_level_act ----------'
        t.subject_name = 'h2s_level_act'
        t.subject_type_id = 'IntDataPoint'
        t.geni_app_if = True
        t.subject_save = '-'
        t.flash_block = '-'
        t.observer_name = 'dosing_pump_ctrl'
        t.observer_type = 'DDACtrl'
        t.subject_relation_name = 'h2s_level_act'

        t.int_value = '0'
        t.int_type = 'U32'
        t.int_min = '0'
        t.int_max = '99999999'
        t.int_quantity_type = 'Q_PARTS_PER_MILLION'
        t.int_verified = False

        t.geni_var_name = 'h2s_level'
        t.geni_class = 14
        t.geni_id = 190
        t.auto_generate = True
        t.geni_convert_id = 'Dim. less with NA'
        t.save()


2. Open run.py and modify it as below:

.. code-block:: python
    :linenos:

    # -*- coding: utf-8 -*-
    from scripts.misc import copy_database, run_generators, ghs_build, vc_build
    from scripts.tables import *
    from scripts.feature.example2 import example2
    
    if __name__ == '__main__':
        example2()
        run_generators()
        
3. Run run.py in windows command.

.. code-block:: console

    python run.py


Elaborate 2
^^^^^^^^^^^

**example2.py**

.. code-block:: python

    def example2():
        t = template('NewSubject')
        t.description = '---------- Add Subject: h2s_level_act ----------'
        t.subject_name = 'h2s_level_act'
        t.subject_type_id = 'IntDataPoint'
        t.geni_app_if = True
        t.subject_save = '-'
        t.flash_block = '-'
        t.observer_name = 'dosing_pump_ctrl'
        t.observer_type = 'DDACtrl'
        t.subject_relation_name = 'h2s_level_act'

        t.int_value = '0'
        t.int_type = 'U32'
        t.int_min = '0'
        t.int_max = '99999999'
        t.int_quantity_type = 'Q_PARTS_PER_MILLION'
        t.int_verified = False

        t.geni_var_name = 'h2s_level'
        t.geni_class = 14
        t.geni_id = 190
        t.auto_generate = True
        t.geni_convert_id = 'Dim. less with NA'
        t.save()


1. We just talk from the ``example2()``, other parts please refer example 1. After creating new instance from template, we also set some value to this instance.

+-----------------------+-------------------------------------------------------------------------------------------------------------------------+
| attribute             | explanation                                                                                                             |
+=======================+=========================================================================================================================+
| subject_name          | new subject name, this name will be used as SP_ + short_name + _ + subject_name (all capitalized) in application.       |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------+
| subject_type_id       | which subject type to use, IntDataPoint, BoolDataPoint or something else.                                               |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------+
| geni_app_if           | True - geni interface, False - not geni interface.                                                                      |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------+
| subject_save          | '-', 'All', 'Value'.                                                                                                    |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------+
| flash_block           | '-', 'Config', 'Log', 'GSC', 'No boot', 'Log series 1', 'Log series 2', 'Log series 3', 'Log series 4', 'Log series 5'. |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------+
| observer_name         | the corresponding observer name.                                                                                        |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------+
| observer_type         | the corresponding observer type.                                                                                        |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------+
| subject_relation_name | subject relation name, must be all capitalized.                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------+
| int_value             | set value                                                                                                               |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------+
| int_type              | int data type, 'I16', 'I32', 'U16', 'U32', 'U8'                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------+
| int_min               | minimum value                                                                                                           |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------+
| int_max               | maximum value                                                                                                           |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------+
| int_quantity_type     | quantity type for this int data                                                                                         |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------+
| int_verified          | verified                                                                                                                |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------+
| geni_var_name         | geni variable name                                                                                                      |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------+
| geni_class            | geni class                                                                                                              |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------+
| geni_id               | geni id                                                                                                                 |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------+
| auto_generate         | auto generate geni data for this subject                                                                                |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------+
| geni_convert_id       | geni convert id, defined in GeniConvert table                                                                           |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------+

.. warning::
    Please also modify the application that use the new added subject, otherwise, it will cause critical issue.
