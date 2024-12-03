### **Project Documentation: Log File Analysis and Suspicious Activity Detection**

#### **1. Project Overview**

This Python-based log file analysis tool is designed to process web server log files, extract and analyze key information related to requests, frequently accessed endpoints, and detect suspicious activities such as brute-force login attempts. The project is intended to assist in cybersecurity tasks by identifying patterns, potential security risks, and summarizing web server interactions.

#### **2. Features**

The tool provides the following features:
1. **Count Requests per IP Address**: Tracks the number of requests made by each unique IP address.
2. **Identify the Most Frequently Accessed Endpoint**: Identifies the most frequently accessed endpoint (URL/resource) in the log file.
3. **Detect Suspicious Activity**: Identifies potential brute-force login attempts by detecting IP addresses with multiple failed login attempts (HTTP status `401`).
4. **Results Output**: Displays the analysis results in the terminal and saves them to a CSV file for future reference.

#### **3. Functional Requirements**

The Python script implements the following functionalities:
1. **Count Requests per IP Address**:
   - Parse log entries to extract IP addresses.
   - Count the number of requests made by each IP address.
   - Display the IP address and its corresponding request count.

2. **Identify the Most Frequently Accessed Endpoint**:
   - Extract endpoints (URLs or resource paths) from the log entries.
   - Determine the most frequently accessed endpoint and count the number of times it was accessed.

3. **Detect Suspicious Activity**:
   - Identify failed login attempts (status code `401` or message `"Invalid credentials"`).
   - Flag IP addresses with failed login attempts exceeding a configurable threshold (default: 10).
   - Display IP addresses involved in suspicious activities and the number of failed login attempts.

4. **Output Results**:
   - Display analysis results in a clear, organized format in the terminal.
   - Save the results to a CSV file with the following structure:
     - **Requests per IP**: IP Address, Request Count
     - **Most Accessed Endpoint**: Endpoint, Access Count
     - **Suspicious Activity**: IP Address, Failed Login Count

#### **4. Non-Functional Requirements**

1. **Performance**:
   - The script efficiently processes log files, even for large datasets, providing results in under a few seconds for tens of thousands of log entries.
   - Memory usage remains minimal, with a footprint under 2.5 MB for typical use cases.

2. **Scalability**:
   - The script is designed to handle log files of increasing size with minimal delays.
   - For extremely large datasets (millions of log entries), optimization techniques such as parallelization may be considered to improve processing speed.

3. **User Interface**:
   - The results are displayed in a readable format in the terminal.
   - An output CSV file is generated for further review and analysis.

#### **5. Input and Output**

**Input**:  
- The script accepts a single **log file** (e.g., `access.log`) as input. The log file should follow the format typically found in web server logs, with entries containing information such as IP address, timestamp, request method, endpoint, and status code.

**Output**:  
- The results are displayed in the terminal, showing:
  - The number of requests per IP address.
  - The most frequently accessed endpoint.
  - Suspicious IP addresses involved in multiple failed login attempts.
- The results are also saved to a CSV file named `log_analysis_results.csv` (by default), with three sections:
  - **Requests per IP**: Lists the IP address and the number of requests.
  - **Most Accessed Endpoint**: Lists the most accessed endpoint and the number of requests made.
  - **Suspicious Activity**: Lists the IP address and the number of failed login attempts.

#### **6. Script Structure**

The project consists of the following Python files:
1. **`count_requests.py`**: Contains a function to count the number of requests made by each IP address.
2. **`frequently_accessed_endpoint.py`**: Contains a function to find the most frequently accessed endpoint in the log file.
3. **`detect_suspicion.py`**: Contains a function to detect suspicious activity based on failed login attempts.
4. **`main.py`**: The main script that coordinates the analysis by calling functions from the above modules, displays the results, and saves them to a CSV file.

#### **7. Code Flow**

1. **Log File Parsing**:
   - The log file is read line by line.
   - Each line is parsed to extract the necessary information (IP address, endpoint, status code, etc.).

2. **Request Counting**:
   - The IP addresses are collected and counted using a dictionary (hashmap).

3. **Endpoint Access Counting**:
   - The endpoint or resource path is extracted from each request and stored in a dictionary to count the occurrences.

4. **Suspicious Activity Detection**:
   - Each log entry is checked for failed login attempts (HTTP status `401` or failure message).
   - A count of failed attempts is maintained for each IP address.
   - IP addresses with failed attempts exceeding the threshold are flagged as suspicious.

5. **Results Display and Output**:
   - The results are printed to the terminal in a user-friendly format.
   - The results are saved to a CSV file for further analysis.

#### **8. Sample Usage**

```bash
$ python main.py sample.log
```

This command will run the script on the `sample.log` file and generate the output in the terminal and a CSV file (`log_analysis_results.csv`).

#### **9. Performance Considerations**

- **Execution Time**: The execution time scales with the size of the log file. For log files with tens of thousands of entries, the script runs within a few seconds.
- **Memory Usage**: The memory usage is minimal, with the current approach processing large files efficiently without memory bottlenecks.
  
For larger datasets (millions of log entries), optimizations such as parallelization or chunk-based processing may be necessary.

#### **10. Limitations**

- The script assumes that the log file follows a standard web server log format. Custom log formats may require additional parsing logic.
- Suspicious activity detection relies on a simple threshold-based approach for failed login attempts, which can be adjusted based on use case.

#### **11. Future Enhancements**

1. **Parallelization**: Implement parallel processing for handling larger log files more efficiently.
2. **Advanced Suspicious Activity Detection**: Introduce more sophisticated methods for detecting brute force or other malicious activities.
3. **Logging and Error Handling**: Implement detailed logging for debugging and error handling to improve script reliability.
4. **Real-time Threat Detection**:Implement real-time log monitoring using services like Apache Kafka or AWS Lambda to detect suspicious activity immediately.

#### **12. Conclusion**

This log file analysis tool is an efficient solution for processing web server logs, identifying frequently accessed endpoints, detecting suspicious activity, and summarizing key information. It provides valuable insights that can assist in identifying potential security risks, making it an essential tool for cybersecurity-related tasks.