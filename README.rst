===============================
Cookiecutter PyScience Package
===============================

.. image:: https://github.com/CCampJr/cookiecutter-pyscience/actions/workflows/python-testing.yml/badge.svg
	:alt: pytest
	:target: https://github.com/CCampJr/cookiecutter-pyscience/actions/workflows/python-testing.yml

.. image:: https://codecov.io/gh/CCampJr/cookiecutter-pyscience/branch/master/graph/badge.svg?token=WIHgHEUc82
	:alt: Codecov
	:target: https://codecov.io/gh/CCampJr/cookiecutter-pyscience

.. image:: https://img.shields.io/badge/License-NIST%20Public%20Domain-green.svg
    :alt: NIST Public Domain
    :target: https://github.com/CCampJr/cookiecutter-pyscience/blob/master/LICENSE.md

Cookiecutter_ template for a scientific computing with Python package.

* GitHub repo: https://github.com/CCampJr/cookiecutter-pyscience

Features
--------

* Testing with GitHub actions via `pytest`` and `coverage``
  
  * Using coverage API token saved in GitHub secrets
  
* Deployment to PyPi with GitHub actions
  
  * Using PyPi API token saved in GitHub secrets
  
* Versioning set in `_version.py`

.. _Cookiecutter: https://github.com/cookiecutter/cookiecutter

Quickstart
----------

Install the latest Cookiecutter if you haven't installed it yet (this requires
Cookiecutter 1.4.0 or higher)::

    pip install -U cookiecutter

Generate a Python package project::

    cookiecutter https://github.com/CCampJr/cookiecutter-pyscience.git

LICENSE
----------
This software was developed by employees of the National Institute of Standards and Technology (NIST), an agency of the Federal Government. Pursuant to `title 17 United States Code Section 105 <http://www.copyright.gov/title17/92chap1.html#105>`_, works of NIST employees are not subject to copyright protection in the United States and are considered to be in the public domain. Permission to freely use, copy, modify, and distribute this software and its documentation without fee is hereby granted, provided that this notice and disclaimer of warranty appears in all copies.

THE SOFTWARE IS PROVIDED 'AS IS' WITHOUT ANY WARRANTY OF ANY KIND, EITHER EXPRESSED, IMPLIED, OR STATUTORY, INCLUDING, BUT NOT LIMITED TO, ANY WARRANTY THAT THE SOFTWARE WILL CONFORM TO SPECIFICATIONS, ANY IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND FREEDOM FROM INFRINGEMENT, AND ANY WARRANTY THAT THE DOCUMENTATION WILL CONFORM TO THE SOFTWARE, OR ANY WARRANTY THAT THE SOFTWARE WILL BE ERROR FREE. IN NO EVENT SHALL NIST BE LIABLE FOR ANY DAMAGES, INCLUDING, BUT NOT LIMITED TO, DIRECT, INDIRECT, SPECIAL OR CONSEQUENTIAL DAMAGES, ARISING OUT OF, RESULTING FROM, OR IN ANY WAY CONNECTED WITH THIS SOFTWARE, WHETHER OR NOT BASED UPON WARRANTY, CONTRACT, TORT, OR OTHERWISE, WHETHER OR NOT INJURY WAS SUSTAINED BY PERSONS OR PROPERTY OR OTHERWISE, AND WHETHER OR NOT LOSS WAS SUSTAINED FROM, OR AROSE OUT OF THE RESULTS OF, OR USE OF, THE SOFTWARE OR SERVICES PROVIDED HEREUNDER.

Contact
-------
Charles H. Camp Jr.
`charles.camp@nist.gov <mailto:charles.camp@nist.gov>`_

Contributors
-------------

-   Charles H. Camp Jr.