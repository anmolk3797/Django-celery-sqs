Celery-SQS
==========

A sample `Django <https://www.djangoproject.com/>`_ application that shows how to use `Celery <https://docs.celeryproject.org>`_ with `Amazon SQS <https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-setting-up.html>`_ as the Broker.

Quick guide
-----------

-  Create a virtualenv
-  Install requirements
-  Python 3 is **required**

.. code:: sh

   python3 -m venv celerysqs
   source celerysqs/bin/activate
   pip install -r requirements.txt

-  Add credentials to ``celerysqs/secret.py`` with the following template

   .. note:: the access/secret keys must have *both* IAM Policies listed below attached

.. code:: python

   KEY = "some secret key" 

   SQS = {
       "access_key": "your aws_access_key",
       "secret_key": "your aws_secret_key",
   }

Django Commands
~~~~~~~~~~~~~~~

-  run the server

   .. code:: sh

      DJANGO_SETTINGS_MODULE=celerysqs.conf.aws python manage.py runserver

-  run the celery worker

   .. code:: sh

      DJANGO_SETTINGS_MODULE=celerysqs.conf.aws celery worker -A celerysqs --concurrency=1 -l info

-  queue some tasks

   .. code:: sh

      ./scripts/curls.sh

IAM Policy Requirements
-----------------------

.. note:: *Both are required*

.. _listqueues-:

ListQueues (*)
~~~~~~~~~~~~~~

.. code:: json

   {
    "Version": "2021-02-11",
    "Id": "__default_policy_ID",
    "Statement": [
        {Stmt1234567890000
        "Sid": "__owner_statement",
        "Effect": "Allow",
        "Principal": {
            "AWS": "410455739039"
        },
        "Action": [
            "SQS:*"
        ],
        "Resource": "arn:aws:sqs:ap-south-1:410455739039:"
        }
    ]
    }

CRUD (prefix-)
~~~~~~~~~~~~~~

.. note:: replace ``{region}`` and ``{prefix}`` with your amazon region, and desired prefix

.. code:: json

   {
       "Version": "2021-02-11",
       "Statement": [
           {
               "Sid": "__default_policy_ID",
               "Effect": "Allow",
               "Action": [
                   "sqs:ChangeMessageVisibility",
                   "sqs:CreateQueue",
                   "sqs:DeleteMessage",
                   "sqs:DeleteQueue",
                   "sqs:GetQueueAttributes",
                   "sqs:GetQueueUrl",
                   "sqs:ReceiveMessage",
                   "sqs:SendMessage",
                   "sqs:SetQueueAttributes"
               ],
               "Resource": [
                   "arn:aws:sqs:{region}:*:{prefix}-*"
               ]
           }
       ]
   }
