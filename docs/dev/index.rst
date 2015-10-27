Developer documentation
=======================

Component overview
------------------

The Eggplant application contains the following sub-applications (python packages
nested in ``eggplant/`` containing models and migrations).

All applications are loosely coupled, only ``core`` and ``common`` are dependencies
of other sub-applications.

 - ``common`` - is NOT a django application. Contains utilities for all other
   packages. Is not allowed to depend on anything else.
 - ``core`` - an application with models that all other applications may depend
   on.
 - ``dashboard`` - Functionality for workflow of members, administrators etc.
 - ``membership`` - Extends from Django allauth and contains the models of
   memberships and their organizations.
 - ``payments`` - Contains payment logic based on Django getpaid.
 - ``webshop`` - An application that handles the webshop logic
 
 
TODO
~~~~

``webshop`` and ``payments`` should be merged.

Dependency overview
-------------------

askdasdk