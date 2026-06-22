import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import joblib
cpu_model = joblib.load("cpu_forecasting_model.pkl")
cpu_scaler = joblib.load("cpu_scaler.pkl")
memory_model = joblib.load("memory_forecasting_model.pkl")
memory_scaler = joblib.load("memory_scaler.pkl")
anomaly_model = joblib.load("anomaly_model.pkl")
anomaly_scaler = joblib.load("anomaly_scaler.pkl")
st.title('AI Cloud Digital Twin')
st.sidebar.title('Feature Avilable')
df = pd.read_csv('cloud_dataset.csv')
df['Timestamp'] = pd.to_datetime(df['Timestamp'])
if st.sidebar.checkbox('Show Raw Data'):
    st.subheader('Original dataset')
    st.write(df)

st.sidebar.subheader('Types of User Avilable')
user_options = ['user_1','user_2','user_3','user_4','user_5','user_6','user_7','user_8','user_9','user_10']
box = st.sidebar.selectbox('User',options=user_options)
st.sidebar.subheader('Type of Workload Avilable')
work_options = ['Web_Service','Database_Query','Video_Streaming','Crypto_Mining','Backup']
box_2 = st.sidebar.selectbox('Workload',options= work_options)
st.write(f'User: {box}')
st.write(f'Workload: {box_2}')
x = df[(df['User_ID'] == box) & (df['Workload_Type'] == box_2)]
st.subheader('Latest Data')
st.write(x.iloc[-1].loc[['CPU_Usage','Memory_Usage','Disk_IO','Network_IO']])
st.subheader(f'Amount of Data Collected')
v = x.shape[0]
st.write(f'Total observations: {v}')

df_encoded = df.copy()
from sklearn.preprocessing import LabelEncoder
le_user = LabelEncoder()
le_work = LabelEncoder()
df_encoded['User_ID'] = le_user.fit_transform(df_encoded['User_ID'])
df_encoded['Workload_Type'] = le_work.fit_transform(df_encoded['Workload_Type'])
df_encoded['Timestamp'] = pd.to_datetime(df_encoded['Timestamp']).astype('int64') / 1e9
encoded_x = df_encoded[(df_encoded['User_ID'] == le_user.transform([box])[0]) & 
                       (df_encoded['Workload_Type'] == le_work.transform([box_2])[0])]
latest_encoded_row = encoded_x.iloc[-1]
memory_features = ['Timestamp', 'CPU_Usage', 'Disk_IO', 'Network_IO', 'Workload_Type', 'User_ID', 'Anomaly_Label']
memory_input = pd.DataFrame([latest_encoded_row[memory_features]])
memory_input_scaled = memory_scaler.transform(memory_input)
memory_pred = memory_model.predict(memory_input_scaled)[0]
cpu_features = ['Timestamp', 'Memory_Usage', 'Disk_IO', 'Network_IO', 'Workload_Type', 'User_ID', 'Anomaly_Label']
cpu_input = pd.DataFrame([latest_encoded_row[cpu_features]])
cpu_input_scaled = cpu_scaler.transform(cpu_input)
cpu_pred = cpu_model.predict(cpu_input_scaled)[0]
anomaly_features = ['Timestamp', 'CPU_Usage', 'Memory_Usage', 'Disk_IO', 'Network_IO', 'Workload_Type', 'User_ID']
anomaly_input = pd.DataFrame([latest_encoded_row[anomaly_features]])
anomaly_input_scaled = anomaly_scaler.transform(anomaly_input)
anomaly = anomaly_model.predict(anomaly_input_scaled)[0]
st.subheader("AI Digital Twin Forecasts")
col1, col2, col3 = st.columns(3)
col1.metric("Predicted CPU", f"{cpu_pred:.2f}%")
col2.metric("Predicted Memory", f"{memory_pred:.2f}%")
col3.metric("Anomaly Detected?", "YES" if anomaly == 1 else "NO")

st.subheader('Health Status')
cpu = x.iloc[-1]['CPU_Usage']
mem = x.iloc[-1]['Memory_Usage']
score = (cpu * 0.6 + mem * 0.4)
if score <= 60:
    st.success("Status Healthy")
elif score <= 85:
    st.warning("Status Warning")
else:
    st.error("Status Critical")

baseline_cpu = df['CPU_Usage'].mean()
deviation = cpu - baseline_cpu
st.subheader("Deviation from System Baseline")
st.write(f"{deviation:.2f}")

st.sidebar.subheader('Time-Series Graphs')
if st.sidebar.checkbox('Timestamp vs CPU Usage'):
    fig, ax = plt.subplots()
    plt.plot(x.Timestamp,x.CPU_Usage)
    plt.xticks(rotation=45)
    plt.ylabel('CPU Consumption')
    plt.xlabel('Timestamp')
    plt.title('Time v/s CPU')
    st.pyplot(fig)
if st.sidebar.checkbox('Timestamp vs Memory Usage'):
    fig, ax = plt.subplots()
    plt.plot(x.Timestamp,x.Memory_Usage)
    plt.xticks(rotation=45)
    plt.ylabel('Memory Usage')
    plt.xlabel('Timestamp')
    plt.title('Time v/s Memory')
    st.pyplot(fig)
if st.sidebar.checkbox('Timestamp vs Disk IO'):
    fig, ax = plt.subplots()
    plt.plot(x.Timestamp,x.Disk_IO)
    plt.xticks(rotation=45)
    plt.ylabel('Disk IO')
    plt.xlabel('Timestamp')
    plt.title('Time v/s Disk')
    st.pyplot(fig)
if st.sidebar.checkbox('Timestamp vs Network IO'):
    fig, ax = plt.subplots()
    plt.plot(x.Timestamp,x.Network_IO)
    plt.xticks(rotation=45)
    plt.ylabel('Network IO')
    plt.xlabel('Timestamp')
    plt.title('Time v/s Network')
    st.pyplot(fig)

st.sidebar.subheader('Anomaly_Label')
if st.sidebar.checkbox('Show Anomaly Graph'):
    st.subheader('Anomalies Detected per User')
    fig, ax = plt.subplots()
    anomaly_counts = df[df['Anomaly_Label'] == 1]['User_ID'].value_counts()
    plt.bar(anomaly_counts.index, anomaly_counts.values,edgecolor='black')
    plt.xlabel('Users')
    plt.ylabel('Anomalies Detected')
    plt.title('Anomalies per User')
    st.pyplot(fig)
st.subheader('Anomalies Detected wrt User & Work')
anomaly_counts = len(df[(df['Anomaly_Label'] == 1) & (df['User_ID'] == box) & (df['Workload_Type'] == box_2) ])
st.write(f'Anomalies Detected: {anomaly_counts}')

st.subheader("Optimization Recommendations")
recommendations = []
if cpu > 85:
    recommendations.append(
        "Scale CPU Resources"
    )

if mem > 85:
    recommendations.append(
        "Increase Memory Allocation"
    )

if x.iloc[-1]["Disk_IO"] > 80:
    recommendations.append(
        "Increase Disk Throughput"
    )

if x.iloc[-1]["Network_IO"] > 80:
    recommendations.append(
        "Increase Network Capacity"
    )

if anomaly == 1:
    recommendations.append(
        "Investigate Abnormal System Behaviour"
    )

if cpu_pred > 85:
    recommendations.append(
        "Proactively Scale CPU Resources"
    )

if memory_pred > 90:
    recommendations.append(
        "Proactively Increase Memory Resources"
    )

if len(recommendations) == 0:
    st.success(
        "No optimization required."
    )

for r in recommendations:
    st.write("•", r)
