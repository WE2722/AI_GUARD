Alert System Guide
=================

The AI-Guard alert system notifies security personnel when unauthorized individuals are detected, allowing for prompt response to potential security threats.

Alert Types
----------

AI-Guard generates different types of alerts based on security events:

Unauthorized Access Alert
~~~~~~~~~~~~~~~~~~~~~~~~

Triggered when an unknown individual is detected in a monitored area. This is the primary security alert type.

Multiple Unknown Individuals
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Triggered when several unknown individuals are detected simultaneously, which may indicate a coordinated unauthorized access attempt.

Failed Recognition Alert
~~~~~~~~~~~~~~~~~~~~~~

Triggered when the system detects a face but the confidence score is below the threshold for a reliable match.

System Status Alerts
~~~~~~~~~~~~~~~~~~

Non-security alerts related to system health:

* Camera disconnection
* Recognition service interruption  
* Low disk space for logs
* Model loading failures

Alert Notification Methods
-------------------------

Currently, AI-Guard supports the following notification methods:

On-Screen Alerts
~~~~~~~~~~~~~~~

Real-time visual notifications displayed in the recognition interface:

* Red highlight around unauthorized faces
* Alert banner at the top of the screen
* Sound alert (if enabled)

Future Notification Methods
~~~~~~~~~~~~~~~~~~~~~~~~~

The following notification methods are planned for future releases:

* **Email Notifications**: Alerts sent to configured email addresses
* **SMS Notifications**: Text message alerts to security personnel
* **Mobile App Notifications**: Push notifications to the AI-Guard mobile app
* **Integration with Security Systems**: Connections to existing alarm and security infrastructure

Alert Configuration
-----------------

Alert behavior can be customized through the configuration file:

.. code-block:: bash

    # Alert Settings in .env file
    ALERT_NOTIFICATION=True               # Enable/disable alerts
    ALERT_SOUND=True                      # Enable/disable sound alerts
    ALERT_CONSECUTIVE_FRAMES=3            # Number of frames before triggering alert
    ALERT_COOLDOWN_PERIOD=60              # Seconds between repeated alerts
    ALERT_MIN_FACE_SIZE=100               # Minimum face size to trigger alerts

Responding to Alerts
------------------

Viewing Alert Details
~~~~~~~~~~~~~~~~~~~

When an alert is triggered:

1. The alert appears in the recognition interface
2. Click on the alert to view details:
   
   * Timestamp
   * Camera location
   * Screenshot of the detected face
   * Confidence score
   * Any available metadata

Alert Actions
~~~~~~~~~~~

Security personnel can take the following actions when responding to an alert:

* **Acknowledge**: Mark the alert as seen
* **Investigate**: Begin formal response protocol
* **Dismiss**: Mark as false positive
* **Enroll**: Register the unknown individual if authorized
* **Export**: Save alert details for reporting

Alert Workflow
~~~~~~~~~~~~

.. image:: ../assets/images/alert-workflow.png
   :alt: Alert Workflow Diagram

The recommended workflow for handling alerts:

1. **Alert Triggered**: System detects unauthorized access
2. **Initial Assessment**: Security personnel evaluate the alert
3. **Response Decision**: Determine appropriate action based on security protocols
4. **Resolution**: Take action and document the incident
5. **Follow-up**: Update alert status and add any relevant notes

Alert Log and History
-------------------

Accessing Alert History
~~~~~~~~~~~~~~~~~~~~~

Currently, alert history is available in log files generated by the system:

.. code-block:: bash

    # View recent alerts
    cat logs/alerts.log | tail -n 20

In future releases, a dedicated Alert Management Dashboard will provide:

* Searchable alert history
* Filtering by date, time, and alert type
* Statistical analysis of alert patterns
* Alert resolution tracking

Alert Retention 
~~~~~~~~~~~~~

By default, alerts are retained for 90 days. This retention period can be customized in the configuration file:

.. code-block:: bash

    # Alert retention settings
    ALERT_RETENTION_DAYS=90               # Days to keep alert history

Alert Testing
-----------

To test the alert system without actual security events:

1. Launch the recognition system in test mode:

   .. code-block:: bash

      jupyter notebook notebooks/alert_test.ipynb

2. Run the test cells to simulate different alert scenarios
3. Verify that alerts are triggered correctly
4. Test the response workflow

Best Practices
------------

Alert Configuration
~~~~~~~~~~~~~~~~

* **Threshold Tuning**: Adjust confidence thresholds to minimize false positives
* **Cooldown Periods**: Configure appropriate intervals between repeated alerts
* **Notification Routing**: Ensure alerts reach the right personnel

Alert Response
~~~~~~~~~~~~

* **Response Time**: Establish maximum response time guidelines
* **Verification**: Confirm alerts with secondary methods when possible
* **Documentation**: Record all alert responses for audit purposes
* **Training**: Regularly practice alert response procedures

Troubleshooting
-------------

Common Issues
~~~~~~~~~~~

1. **Too Many False Positives**

   * Increase the confidence threshold
   * Increase the consecutive frames setting
   * Improve camera placement and lighting

2. **Missed Alerts**

   * Lower the confidence threshold
   * Verify camera positioning
   * Check system performance and resource usage

3. **Alert Notification Delays**

   * Verify network connectivity
   * Check system resource utilization
   * Reduce processing resolution if necessary

Future Enhancements
-----------------

Planned improvements to the alert system:

* **Automated Response Integration**: Connect with access control systems
* **Alert Prioritization**: AI-based ranking of alert importance
* **Video Recording**: Automatic recording when alerts are triggered
* **Alert Analytics**: Pattern recognition in security events
* **Mobile Response App**: Dedicated mobile application for security personnel

Next Steps
---------

* :doc:`User Management <management>` - Manage user access and permissions
* :doc:`System Configuration <../getting-started/configuration>` - Customize alert settings
* :doc:`Technical Documentation <../technical/index>` - Understand system architecture