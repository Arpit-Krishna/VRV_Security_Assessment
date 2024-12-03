import re
from collections import defaultdict

def detect_suspicious_activity(log_file_path, threshold=10):
    """
    The function `detect_suspicious_activity` reads a log file, identifies IP addresses with multiple
    failed login attempts, and returns a dictionary of suspicious IP addresses exceeding a specified
    threshold.
    
    :param log_file_path: The `detect_suspicious_activity` function takes in a log file path and an
    optional threshold value as parameters. The log_file_path parameter is the path to the log file that
    contains information about login attempts. The threshold parameter is set to a default value of 10,
    but you can adjust it
    :param threshold: The `threshold` parameter in the `detect_suspicious_activity` function is used to
    specify the minimum number of failed login attempts that will be considered as suspicious activity.
    Any IP address with failed login attempts greater than this threshold will be identified as
    suspicious. By default, the threshold is set to, defaults to 10 (optional)
    :return: The `detect_suspicious_activity` function returns a dictionary containing IP addresses as
    keys and the number of failed login attempts associated with each IP address as values. Only IP
    addresses with failed login attempts exceeding the specified threshold (default is 10) are included
    in the dictionary.
    """
    f_attempts = defaultdict(int)
    ip_regex = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
    failure_regex = r'401|Invalid credentials'
    
    with open(log_file_path, 'r') as file:
        for line in file:
            if re.search(failure_regex, line):
                match = re.search(ip_regex, line)
                if match:
                    ip = match.group()
                    f_attempts[ip] += 1
    
    suss_ips = {ip: count for ip, count in f_attempts.items() if count > threshold}
    return suss_ips 
