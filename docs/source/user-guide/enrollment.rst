Face Enrollment Guide
====================

This guide explains the process of enrolling new users into the AI-Guard system through our multi-angle face registration workflow.

Enrollment Process Overview
--------------------------

The enrollment process captures multiple face angles to create a robust face signature:

1. Front-facing capture
2. Left profile capture (approximately 45°)
3. Right profile capture (approximately 45°)
4. User metadata collection (name, ID, etc.)
5. Embedding generation and storage

.. image:: ../assets/images/enrollment-process.png
   :alt: Face Enrollment Process

User Roles Required
-----------------

To enroll users, you need one of the following roles:

* Administrator
* Enrollment Operator

Step-by-Step Enrollment
----------------------

Step 1: Launch the Enrollment Notebook
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Activate your Python environment:

   .. code-block:: bash

      source venv/bin/activate  # On Windows: venv\Scripts\activate

2. Launch the Jupyter notebook:

   .. code-block:: bash

      jupyter notebook notebooks/NNNNNNNNN1111.ipynb

3. Run the initialization cells to set up the webcam and detection models

Step 2: Front Capture
~~~~~~~~~~~~~~~~~~~

1. Position the person centered in front of the camera:

   * Ensure their face is clearly visible
   * Maintain a distance of 50-70cm from the camera
   * Face should be well-lit with even lighting

2. In the notebook, run the cell for front-face capture

3. The system will:

   * Display a live preview with face detection
   * Capture the image when ready
   * Perform quality checks
   * Save the image temporarily

4. If the quality check fails, you'll see specific feedback (e.g., "Face too small" or "Poor lighting"). Adjust as needed and try again.

Step 3: Left Profile Capture
~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Ask the person to turn their head left (approximately 45°):

   * The left ear and side of face should be visible
   * Maintain the same distance from the camera
   * Keep the same lighting conditions

2. Run the cell for left profile capture

3. The system will follow the same quality check process as with the front capture

Step 4: Right Profile Capture
~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Ask the person to turn their head right (approximately 45°)
2. Run the cell for right profile capture
3. Complete the same quality verification process

Step 5: User Information
~~~~~~~~~~~~~~~~~~~~~~

1. When prompted, enter the person's information:

   * Full name (required)
   * ID number (optional)
   * Department/role (optional)
   * Access level (optional)

2. Run the final enrollment cell to:

   * Process all three captured images
   * Generate face embeddings
   * Save the enrollment data securely
   * Create a user record in the system

3. Upon successful completion, you'll see a confirmation message with the new user's details

Updating Enrollments
------------------

To update an existing enrollment:

1. Launch the enrollment notebook
2. Run the cell for enrollment updates
3. Enter the name of the person whose enrollment you want to update
4. Follow the same capture process as with new enrollments
5. The system will replace the old embeddings with the new ones

Batch Enrollment
--------------

For enrolling multiple users in sequence:

1. Launch the batch enrollment notebook ``notebooks/batch_enrollment.ipynb``
2. Run the initialization cells
3. For each person:

   * Enter their name when prompted
   * Complete the three-angle capture process
   * Verify the enrollment was successful

4. When finished, run the final cell to complete the batch process

Best Practices
------------

Lighting Considerations
~~~~~~~~~~~~~~~~~~~~~

* **Ensure even lighting**: Avoid harsh shadows on the face
* **Avoid backlighting**: Don't position the subject in front of windows or bright lights
* **Consistent lighting**: Try to maintain similar lighting for all three angles

Positioning Guidelines
~~~~~~~~~~~~~~~~~~~~

* **Distance**: Keep a consistent 50-70cm distance from the camera
* **Height**: Camera should be at eye level
* **Angles**: For profile views, aim for consistent 45° angles
* **Background**: Use a plain, uncluttered background when possible

Image Quality
~~~~~~~~~~~

* **Resolution**: The face should occupy at least 200x200 pixels in the image
* **Clarity**: Images should be sharp, not blurry
* **Expressions**: Maintain a neutral expression across all captures
* **Accessories**: If the person normally wears glasses, capture with glasses on

Troubleshooting
-------------

Common Issues
~~~~~~~~~~~

1. **"Face not detected"**

   * Ensure adequate lighting
   * Position the face within the camera frame
   * Remove obstacles blocking the face

2. **"Quality check failed"**

   * Improve lighting conditions
   * Adjust distance from camera
   * Ensure face is properly aligned

3. **"Processing error"**

   * Restart the notebook kernel
   * Check for system resource limitations
   * Verify webcam is functioning properly

When to Re-enroll
~~~~~~~~~~~~~~~

Consider re-enrolling a user if:

* Recognition accuracy has decreased
* The person's appearance has significantly changed (new glasses, hairstyle change, etc.)
* The original enrollment was performed under poor conditions

Privacy and Consent
----------------

Before enrolling individuals:

1. Obtain explicit consent for capturing and storing their biometric data
2. Explain how their data will be used and stored
3. Inform them of their rights regarding their personal data
4. Document their consent according to your organization's policies

Next Steps
--------

* :doc:`recognition` - Learn how the system recognizes enrolled individuals
* :doc:`management` - Manage enrolled users and their access levels
* :doc:`../getting-started/configuration` - Adjust system settings for optimal performance