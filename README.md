# AI-Powered Cloud Digital Twin for Resource Monitoring, Forecasting, and Anomaly Detection

## Overview

Modern cloud environments generate large volumes of resource usage data, making it difficult for administrators to continuously monitor system health and anticipate potential failures. This project presents an AI-powered Cloud Digital Twin that creates a virtual representation of cloud infrastructure for real-time monitoring, resource forecasting, anomaly detection, and optimization recommendations.

The system combines machine learning models with an interactive Streamlit dashboard to provide operational insights and support proactive resource management.

---

## Objectives

* Build a Digital Twin of cloud resource utilization.
* Monitor CPU, Memory, Disk I/O, and Network I/O metrics.
* Forecast future CPU and Memory usage.
* Detect abnormal system behavior using machine learning.
* Generate optimization recommendations for resource management.

---

## Dataset

**Dataset Used:**

Cloud Resource Usage Dataset for Anomaly Detection

### Features

* Timestamp
* CPU_Usage
* Memory_Usage
* Disk_IO
* Network_IO
* Workload_Type
* User_ID
* Anomaly_Label

### Dataset Statistics

* Total Records: 14,400
* Users: 10
* Workload Categories:

  * Web Service
  * Database Query
  * Video Streaming
  * Crypto Mining
  * Backup

---

## System Architecture

Cloud Resource Dataset

↓

Digital Twin Dashboard

↓

Resource Forecasting

(CPU & Memory)

↓

Anomaly Detection

↓

Optimization Engine

↓

Actionable Recommendations

---

## Project Components

### 1. Digital Twin Dashboard

The Digital Twin dashboard provides a virtual representation of cloud infrastructure by displaying:

* Current CPU utilization
* Current Memory utilization
* Current Disk I/O
* Current Network I/O
* Health status monitoring
* Time-series visualization of resource usage
* User-specific and workload-specific analysis

### 2. Resource Forecasting

Machine learning models are used to estimate future resource demand.

#### CPU Forecasting

Models Evaluated:

* Linear Regression
* Random Forest Regressor

Best Model:

* Random Forest Regressor

Results:

* MAE: 7.55
* RMSE: 9.73
* R² Score: 0.734

#### Memory Forecasting

Models Evaluated:

* Linear Regression
* Random Forest Regressor

Best Model:

* Random Forest Regressor

Results:

* MAE: 7.74
* RMSE: 9.74
* R² Score: 0.614

### 3. Anomaly Detection

The anomaly detection module identifies unusual system behavior using machine learning.

Models Evaluated:

* Logistic Regression
* Random Forest Classifier

Best Model:

* Random Forest Classifier

Results:

* Accuracy: 99.97%
* Precision: 99.60%
* Recall: 100%
* F1 Score: 99.80%

### 4. Optimization Recommendation Engine

Based on current resource utilization, forecasted demand, and anomaly status, the system generates recommendations such as:

* Scale CPU resources
* Increase memory allocation
* Increase disk throughput
* Increase network capacity
* Investigate abnormal system behavior
* Proactively allocate resources before bottlenecks occur

---

## Technologies Used

### Programming Language

* Python

### Libraries

* Pandas
* NumPy
* Scikit-Learn
* Matplotlib
* Joblib
* Streamlit

### Machine Learning Algorithms

* Linear Regression
* Logistic Regression
* Random Forest Regressor
* Random Forest Classifier

---

## Project Workflow

1. Data Collection
2. Data Preprocessing
3. Exploratory Data Analysis
4. Digital Twin Development
5. Resource Forecasting
6. Anomaly Detection
7. Optimization Recommendation Generation
8. Dashboard Deployment

---

## Results

The proposed system successfully integrates Digital Twin technology with Machine Learning to create an intelligent cloud monitoring platform.

Key achievements include:

* Real-time cloud resource monitoring
* CPU and Memory demand forecasting
* High-performance anomaly detection
* Automated optimization recommendations
* Interactive visualization dashboard

---

## Future Work

* Real-time cloud monitoring using live telemetry streams
* Integration with AWS, Azure, or Google Cloud
* Deep Learning-based forecasting models
* Reinforcement Learning for autonomous resource allocation
* Quantum Machine Learning-based anomaly detection
* Multi-cloud infrastructure monitoring

---

## Author

Sifat Bhatia

B.Tech Computer Science & Engineering

Machine Learning | AI | Quantum Machine Learning | Cloud Systems
