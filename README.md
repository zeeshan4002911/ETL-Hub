# ETL_Hub

Pandas Installation using pip:
pip install pandas

## Spark Installation for linux (WSL)

Prerequisites:
    Before installing PySpark, make sure that the following software is installed on your Linux machine:
    
    Python 3.6 or later
    Java Development Kit (JDK) 8 or later
    Apache Spark

1. Install Java Development Kit (JDK)

    First, update the package index by running:
    
    sudo apt update
    
    Next, install the default JDK using the following command:
    
    sudo apt install default-jdk
    
    Verify the installation by checking the Java version:
    
    java -version

2. Install Apache Spark

    Download the latest version of Apache Spark from the official website (https://spark.apache.org/downloads.html). At the time of writing, the latest version is Spark 3.2.0. Choose the package type as “Pre-built for Apache Hadoop 3.2 and later”.
    
    Use the following commands to download and extract the Spark archive:
    
    wget https://archive.apache.org/dist/spark/spark-3.2.0/spark-3.2.0-bin-hadoop3.2.tgz
    tar -xvzf spark-3.2.0-bin-hadoop3.2.tgz
    
    Move the extracted folder to the /opt directory
    
    sudo mv spark-3.2.0-bin-hadoop3.2 /opt/spark

3. Set Up Environment Variables

    Add the following lines to your ~/.bashrc file to set up the required environment variables:
    
    export SPARK_HOME=/opt/spark
    export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin
    
    Source the updated ~/.bashrc file to apply the changes:
    
    source ~/.bashrc
    
4. Install PySpark

    Install PySpark using pip:
    pip install pyspark

## Spark Installation for Windows

Prerequisites
    
    1. Python 3.6 or later: Download and install Python from the official website (https://www.python.org/downloads/). Make sure to add Python to your PATH during installation.
    2. Java 8: Download and install the Java Development Kit (JDK) 8 from Oracle’s website (https://www.oracle.com/java/technologies/javase/javase-jdk8-downloads.html). Set the JAVA_HOME environment variable to the installation directory.

1. Install Apache Spark

    Download the latest version of Apache Spark from the official website (https://spark.apache.org/downloads.html). Select the package type as “Pre-built for Apache Hadoop”.

    Extract the downloaded .tgz file to a directory, e.g., C:\spark.

    Set the SPARK_HOME environment variable to the extracted directory path, e.g., C:\spark.

2. Install Hadoop

    Download the latest version of Hadoop from the official website (https://hadoop.apache.org/releases.html).

    Extract the downloaded .tar.gz file to a directory, e.g., C:\hadoop.

    Set the HADOOP_HOME environment variable to the extracted directory path, e.g., C:\hadoop.

3. Install PySpark using pip

    Open a Command Prompt with administrative privileges and execute the following command to install PySpark using the Python package manager pip:

    pip install findspark
    pip install pyspark

4. Install winutils.exe

    Since Hadoop is not natively supported on Windows, we need to use a utility called ‘winutils.exe’ to run Spark.

    Download the appropriate version of winutils.exe for your Hadoop version from the following repository: https://github.com/steveloughran/winutils.

    Create a new directory called ‘hadoop’ in your C: drive (C:\hadoop) and a subdirectory called ‘bin’ (C:\hadoop\bin). Place the downloaded ‘winutils.exe’ file in the ‘bin’ directory.
5. Set the Environment Variables

    a) Open the System Properties dialog by right-clicking on ‘This PC’ or ‘Computer’, then selecting ‘Properties’.

    b) Click on ‘Advanced system settings’ and then the ‘Environment Variables’ button.

    c) Under ‘System variables’, click on the ‘New’ button and add the following environment

### variables:

    Variable Name: HADOOP_HOME

    Variable Value: C:\hadoop

    Variable Name: SPARK_HOME

    Variable Value: %USERPROFILE%\AppData\Local\Programs\Python\Python{your_python_version}\Lib\site-packages\pyspark

    Replace {your_python_version} with your installed Python version, e.g., Python39 for Python 3.9.



d) Edit the ‘Path’ variable under ‘System variables’ by adding the following entries:

    %HADOOP_HOME%\bin

    %SPARK_HOME%\bin

e) Click ‘OK’ to save the changes.
