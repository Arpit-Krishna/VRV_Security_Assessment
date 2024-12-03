import csv
import time, tracemalloc
from Count_Request import count_requests_per_ip  # Module to count requests per IP
from Frequently_Accessed_endpoint import find_most_accessed_endpoint  # Module to find the most accessed endpoint
from Detect_Suspision import detect_suspicious_activity  # Module to detect suspicious activities

def save(results, csv_file):
    """
    Save the analysis results to a CSV file.
    
    Parameters:
    - results (dict): A dictionary containing analysis results (requests per IP, most accessed endpoint, and suspicious activity).
    - csv_file (str): The name of the CSV file to save the results.
    """
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        
        # Write requests per IP section
        writer.writerow(["Requests per IP"])
        writer.writerow(["IP Address", "Request Count"])
        for ip, count in results['requests_per_ip'].items():
            writer.writerow([ip, count])
        
        
        writer.writerow([])
        
        # Write the most accessed endpoint section
        writer.writerow(["Most Accessed Endpoint"])
        writer.writerow(["Endpoint", "Access Count"])
        writer.writerow([results['most_accessed_endpoint']['endpoint'], 
                         results['most_accessed_endpoint']['count']])
        
        writer.writerow([])
        
        # Write suspicious activity section, if any
        if results['suspicious_activity']:
            writer.writerow(["Suspicious Activity"])
            writer.writerow(["IP Address", "Failed Login Count"])
            for ip, count in results['suspicious_activity'].items():
                writer.writerow([ip, count])
        else:
            writer.writerow(["No suspicious activity found."])  # Note when no suspicious activity is detected

def main(log_file, output_csv='log_analysis_results.csv'):
    """
    Perform log analysis and display/save results.
    
    Parameters:
    - log_file (str): Path to the log file to be analyzed.
    - output_csv (str): Name of the output CSV file (default: 'log_analysis_results.csv').
    """
    # Count requests per IP from the log file
    requests_per_ip = count_requests_per_ip(log_file)
    
    # Find the most accessed endpoint and its access count
    most_accessed_endpoint, access_count = find_most_accessed_endpoint(log_file)
    
    # Detect suspicious activity (e.g., brute force login attempts), with a threshold of 5 failed attempts
    suspicious_activity = detect_suspicious_activity(log_file, 5)
    
    # Compile results into a dictionary for further processing and saving
    results = {
        'requests_per_ip': requests_per_ip,
        'most_accessed_endpoint': {
            'endpoint': most_accessed_endpoint,
            'count': access_count
        },
        'suspicious_activity': suspicious_activity
    }

    # Display requests per IP in the terminal
    print("Requests per IP:")
    for ip, count in requests_per_ip.items():
        print(f"{ip}: {count}")
    
    # Display the most accessed endpoint in the terminal
    print("\nMost Accessed Endpoint:")
    print(f"{most_accessed_endpoint}: {access_count} times")
    
    # Display suspicious activity in the terminal
    print("\nSuspicious Activity:")
    if not suspicious_activity:
        print("No suspicious activity found.")
    else:
        for ip, count in suspicious_activity.items():
            print(f"{ip}: {count} failed attempts")
    
    # Save the results to a CSV file
    save(results, output_csv)
    print(f"\nResults saved to {output_csv}")


if __name__ == '__main__':
    tracemalloc.start()
    start_time = time.time()
    log_file = 'sample.log'
    main(log_file)
    end_time = time.time()
    print(f"Execution Time: {end_time - start_time} seconds")
    print("Memory used: ", tracemalloc.get_traced_memory())
    tracemalloc.stop()                          