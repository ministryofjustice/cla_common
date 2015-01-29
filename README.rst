=============================
cla_common
=============================

.. image:: https://badge.fury.io/py/cla_common.png
    :target: https://badge.fury.io/py/cla_common

.. image:: http://jenkins.dsd.io/buildStatus/icon?job=CLA Common
    :target: https://travis-ci.org/ministryofjustice/cla_common

.. image:: https://coveralls.io/repos/ministryofjustice/cla_common/badge.png?branch=master
    :target: https://coveralls.io/r/ministryofjustice/cla_common?branch=master

common code for CLA

Documentation
-------------

Quickstart
----------

Install cla_common::

    pip install cla_common

Then use it in a project::

    import cla_common

Making a new release
--------------------

1. Make a feature branch
2. Make your changes
3. submit a PR
4. check if the build job / tests pass on jenkins
5. merge it (ask for a code review if you did anything scary)
6. pull cla_common's develop branch
7. $ bumpversion patch
8. $ git push && git push --tags
 

   
