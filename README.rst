==========
cla_common
==========

.. image:: https://coveralls.io/repos/ministryofjustice/cla_common/badge.svg?branch=master
    :target: https://coveralls.io/r/ministryofjustice/cla_common?branch=master

.. image:: https://circleci.com/gh/ministryofjustice/cla_common.svg?style=shield
    :target: https://circleci.com/gh/ministryofjustice/cla_common

Documentation
-------------
Common code for

- `cla_backend <https://github.com/ministryofjustice/cla_backend/>`_
- `cla_frontend <https://github.com/ministryofjustice/cla_frontend/>`_
- `cla_public <https://github.com/ministryofjustice/cla_public/>`_

Quickstart
----------

Install cla_common::

    pip install cla_common

Then use it in a project::

    import cla_common

How to make changes
-------------------
1. Create a feature branch
2. Make your changes
3. Check if the build job and tests pass on CircleCI
4. Submit a pull request
5. merge it (ask for a code review if you did anything scary)
6. Once code is merged, pull develop branch
7. Follow Semantic Versioning to increment cla_common/__init__.py __version__ appropriately
8. Commit and merge to master
9. Tag master with your new version
10. $ git push && git push --tags
