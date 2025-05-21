User Guide
==========

Welcome to the AI-Guard User Guide. This section provides detailed information about how to use the AI-Guard facial recognition security system effectively.

User Roles
-----------

AI-Guard supports different user roles, each with specific permissions and responsibilities:

Administrator
~~~~~~~~~~~~

Administrators have full access to the system with privileges to:

* Manage user accounts and permissions
* Configure system settings
* Access all analytics and reports
* Modify recognition thresholds
* Add or remove users from the face database

Enrollment Operator
~~~~~~~~~~~~~~~~~~

Enrollment operators are responsible for:

* Registering new individuals in the system
* Capturing face images from multiple angles
* Verifying image quality
* Entering user metadata (name, ID, etc.)

Security Guard
~~~~~~~~~~~~~

Security guards use the system to:

* Monitor real-time recognition feeds
* Respond to security alerts
* View entry logs
* Verify individual identities

System Components
----------------

The AI-Guard system consists of several key components:

Face Enrollment System
~~~~~~~~~~~~~~~~~~~~~

The :doc:`Face Enrollment <enrollment>` module allows operators to register individuals in the system by capturing multiple face angles and storing their biometric data securely.

Face Recognition System
~~~~~~~~~~~~~~~~~~~~~~

The :doc:`Face Recognition <recognition>` module continuously monitors camera feeds, detects faces, and compares them against the database of enrolled individuals.

Alert System
~~~~~~~~~~~

The :doc:`Alert System <alerts>` notifies security personnel when unauthorized individuals are detected, providing details about the location and time of the detection.

User Management
~~~~~~~~~~~~~~

The :doc:`User Management <management>` module allows administrators to add, edit, and remove system users, as well as manage their permissions.

Common Tasks
-----------

Here are some common tasks that users perform with AI-Guard:

For Administrators
~~~~~~~~~~~~~~~~~

* :doc:`System Configuration <../getting-started/configuration>`
* :doc:`Managing Users and Permissions <management>`
* :doc:`Viewing System Analytics <analytics>`
* :doc:`Backing Up and Restoring Data <backup-restore>`

For Enrollment Operators
~~~~~~~~~~~~~~~~~~~~~~~

* :doc:`Enrolling New Users <enrollment>`
* :ref:`Updating Existing Enrollments <updating-enrollments>`
* :ref:`Verifying Enrollment Quality <quality-verification>`

For Security Guards
~~~~~~~~~~~~~~~~~

* :ref:`Monitoring Real-time Feeds <monitoring>`
* :ref:`Responding to Alerts <responding>`
* :doc:`Creating Security Reports <reports>`

Best Practices
-------------

To get the most out of the AI-Guard system:

1. **Regular Updates**: Keep the system and its models up to date for the best performance
2. **Quality Enrollments**: Follow the :ref:`enrollment guidelines <best-practices>` to ensure high-quality face captures
3. **Proper Lighting**: Ensure adequate lighting in areas being monitored
4. **Regular Audits**: Periodically review access logs and system performance
5. **Training**: Ensure all users are properly trained on their respective modules

Getting Help
-----------

If you encounter issues while using AI-Guard:

* Check the :doc:`Troubleshooting Guide <troubleshooting>`
* Review the :doc:`FAQ <faq>` for answers to common questions
* Contact system support for assistance

Next Steps
---------

Choose a section from the sidebar to learn more about specific aspects of the AI-Guard system, or start with the :doc:`Face Enrollment Guide <enrollment>` to begin registering users.

.. toctree::
   :maxdepth: 2
   :hidden:
   
   enrollment
   recognition
   alerts
   management
   analytics
   reports
   backup-restore
   troubleshooting
   faq