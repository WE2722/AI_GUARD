AI-Guard Documentation
======================

**AI-Guard** is an intelligent, real-time facial recognition security system developed for ENSAM Meknès. It aims to prevent unauthorized access by identifying individuals at campus entry points using deep learning and computer vision.

.. grid:: 1 2 2 2
    :gutter: 3

    .. grid-item-card:: Getting Started
        :link: getting-started/index
        :link-type: doc
        :text-align: center

        Installation and basic setup
        ^^^

    .. grid-item-card:: Face Enrollment
        :link: user-guide/enrollment
        :link-type: doc
        :text-align: center

        Register new users in the system
        ^^^

    .. grid-item-card:: Face Recognition
        :link: user-guide/recognition
        :link-type: doc
        :text-align: center

        Real-time monitoring and detection
        ^^^

    .. grid-item-card:: Alert System
        :link: user-guide/alerts
        :link-type: doc
        :text-align: center

        Security notifications
        ^^^

Key Features
-----------

* 🎥 **Multi-angle Face Enrollment** - Register users with front, left, and right profile captures
* 🔍 **Real-time Recognition** - Identify individuals from camera feeds
* 🔔 **Alert System** - Notify security personnel of unauthorized access
* 📊 **Security Analytics** - Visualize security data and trends
* 🛡️ **Access Control** - Manage authorized personnel database
* 🧠 **Advanced ML Models** - Based on FaceNet, ArcFace, and MTCNN

Project Status
-------------

AI-Guard is currently in **proof-of-concept stage**. This documentation covers both:

* **Current functionality**: What's implemented and available now
* **Planned features**: The complete vision for the system upon full deployment

Quick Start
----------

To get started with AI-Guard:

.. code-block:: bash

    # Clone the repository
    git clone https://github.com/your-username/ai-guard.git
    cd ai-guard

    # Create virtual environment
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

    # Install dependencies
    pip install -r requirements.txt

    # Run the enrollment script
    jupyter notebook notebooks/NNNNNNNNN1111.ipynb

Check the `Quick Start Guide <getting-started/quick-start.html>`_ for more detailed instructions.

Dataset
-------

AI-Guard uses an extensively processed version of the Labeled Faces in the Wild dataset as its foundation. You can download this dataset from Kaggle:

.. code-block:: python

    import kagglehub
    # Download latest version
    path = kagglehub.dataset_download("wiameelhafid/aiguard-split-data")
    print("Path to dataset files:", path)

About the Project
----------------

AI-Guard was developed by `Wiame El Hafid and Houssam Rjili <about/team.html>`_ at ENSAM Meknès to address growing security concerns in educational institutions. The system aims to provide a robust, cost-effective security solution through advanced facial recognition technology.

`Learn more about the project <about/index.html>`_

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: Contents:
   
   getting-started/index
   user-guide/index
   technical/index
   development/index
   about/index