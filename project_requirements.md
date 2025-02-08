Advanced Data engineering
Final project


For your final project you will need to work on a data engineering project. As a deliverable of the project will be your presentation of a working system and a documentation for the work done. Two students can work on a project. 

The documentation of the project should be a maximum five-page document that will contain the following outline:

•	Project overview
•	Architecture and design
•	Setup and configuration
•	Results 

Your final project should contain the following:

•	A clear definition of the problem or objective the project aims to address. It should specify the data engineering challenges or requirements to be tackled.
•	Identify and describe the data sources to be used in the project. Explain the data formats, structures, and any potential issues or complexities involved.
•	Design a data pipeline architecture that outlines the flow of data from source to destination. Define the stages of extraction, transformation, and loading, and specify the tools or technologies to be employed.
•	Describe the steps and transformations necessary to clean, preprocess, aggregate, or enrich the data. Discuss the techniques, algorithms, or frameworks used for data manipulation and cleansing.
•	Specify the storage and infrastructure components required to support the data pipeline. Discuss the selection of databases, data lakes, or cloud storage solutions, and explain the rationale behind the choices made.
•	Explain how the data pipeline will be orchestrated and scheduled. Discuss the usage of workflow management tools or frameworks like Apache Airflow, Luigi, or custom scripts to manage the pipeline execution.
•	Document the project comprehensively, including clear instructions, code documentation, and explanations of design choices. Discuss the testing methodologies and practices used to validate the functionality and correctness of the data pipeline.


Optional requirements:

•	Error Handling and Monitoring: Describe the mechanisms in place for error handling, data quality checks, and exception handling. Discuss how monitoring and alerting will be implemented to ensure the health and reliability of the data pipeline.
•	Performance Optimization: Outline any performance optimization techniques considered or implemented to enhance the efficiency and scalability of the data pipeline. Discuss strategies for handling large volumes of data or improving processing speeds.
•	Results and Evaluation: Present the outcomes of the project, including the processed data, insights gained, or any visualizations or reports generated. Evaluate the effectiveness and efficiency of the data engineering solution against the stated problem or objective.
•	Future Considerations: Discuss potential improvements, further enhancements, or future directions for the project. Consider scalability, automation, additional data sources, or advanced techniques that could be implemented.

Some examples:

•	Data Pipeline Development: Design and implement a data pipeline that ingests data from various sources, performs data transformations, and loads it into a target system or database. The project may involve working with technologies like Apache Kafka, Apache Spark, or Apache Airflow.
•	ETL (Extract, Transform, Load) Process Optimization: Analyze an existing ETL process and identify opportunities for optimization in terms of performance, scalability, or resource utilization. Implement and measure the improvements made to the process using tools like Apache Hadoop, Apache Hive, or cloud-based data processing platforms.
•	Data Warehouse Design: Create a data warehouse schema and develop a pipeline that extracts data from multiple sources, transforms it into a unified schema, and loads it into a data warehouse. Use tools such as Amazon Redshift, Google BigQuery, or Apache Cassandra for building the data warehouse.
•	Real-time Data Processing: Build a real-time data processing system that can handle streaming data from sources like IoT devices, social media feeds, or log files. Implement technologies such as Apache Kafka, Apache Flink, or Apache Storm for processing and analyzing the streaming data in real-time.
•	Data Quality Assessment and Monitoring: Develop a system to assess and monitor data quality in a dataset or data pipeline. Create metrics and checks to identify data anomalies, outliers, or inconsistencies. Use tools like Apache Nifi, Apache Kafka, or custom scripts to implement data quality monitoring processes.
•	Cloud-based Data Engineering: Implement a data engineering project using cloud-based platforms like Amazon Web Services (AWS), Microsoft Azure, or Google Cloud Platform (GCP). Build data pipelines, leverage cloud-based data storage and processing services, and explore features such as serverless computing or managed data services.
•	Data Visualization: Create a data visualization project that demonstrates the ability to extract data from various sources, transform it into a suitable format, and present it visually using tools like Tableau, Power BI, or Python libraries such as Matplotlib or Plotly.
•	Data Governance and Security: Design and implement a data governance framework that ensures data security, privacy, and compliance with regulations such as GDPR or HIPAA. Develop mechanisms for data access control, data masking, encryption, and auditing.

 
Some sources where you can obtain data are as follows:

1.	data.gov: The U.S. government's official website for open data, providing access to a wide range of datasets on various topics. https://www.data.gov/ 
2.	European Data Portal: The official portal for open data from the European Union, offering datasets from EU member states and other European countries. https://www.europeandataportal.eu/ 
3.	World Bank Open Data: A comprehensive collection of economic, social, and environmental data from countries around the world, provided by the World Bank. https://data.worldbank.org/ 
4.	United Nations Data: The United Nations' open data platform, offering a wide range of datasets on global development and humanitarian issues. https://data.un.org/ 
5.	Open Data Network: A platform that provides access to a vast collection of open datasets from various sources, including government agencies, non-profit organizations, and research institutions. https://www.opendatanetwork.com/ 
6.	Kaggle: A popular platform for data science and machine learning, which hosts a wide range of datasets contributed by the community. https://www.kaggle.com/datasets 
7.	Google Public Data Explorer: A tool that allows users to explore and visualize a variety of public datasets, covering topics such as population, education, health, and more. https://www.google.com/publicdata/directory 
8.	OpenStreetMap: An open-source mapping platform that provides free and editable map data for locations worldwide. https://www.openstreetmap.org/ 
9.	Data.gov.uk: The UK government's portal for open data, providing access to datasets from various government departments and agencies. https://data.gov.uk/ 
10.	Open Data on AWS: Amazon Web Services (AWS) provides a registry of publicly available datasets that can be accessed and analyzed on their platform. https://registry.opendata.aws/ 


Also notes from class:
```
    - To build a system to retrieval data from multiple sources
    - You can think about anything
    - Something to aggregate data from other sources
    - Data warehouse is one of those systems
    - =============
    - Some students created a db where using airflow pipes they were crawling data from websites, from web services. About bus iteniraries
        ○ From Struga MKD to Kocani MKD. Information that does not exist currently in other places
    - I do not want you to create an application
    - The part that was interesting was automatic process of crawling data
        ○ Daily jobs in airflow
        ○ That will go and crawl data from websites
    - ============
Had students that were working with eprocurement system in MKD. Crawling and combining data, if the government data is wrong
```