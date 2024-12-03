import re
from collections import defaultdict

def count_requests_per_ip(log_file):
    """
    The function `count_requests_per_ip` reads a log file and counts the number of requests per IP
    address.
    
    :param log_file: The function `count_requests_per_ip` takes a log file as input and counts the
    number of requests made by each unique IP address in the log file. It uses a regular expression to
    extract IP addresses from each line of the log file and then stores the counts in a dictionary where
    the keys are the
    :return: The function `count_requests_per_ip` returns a dictionary where the keys are IP addresses
    found in the log file and the values are the number of times each IP address appears in the log
    file.
    """
    ip_counts = defaultdict(int)
    ip_regex = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
    
    with open(log_file, 'r') as file:
        for line in file:
            match = re.search(ip_regex, line)
            if match:
                ip_address = match.group()
                ip_counts[ip_address] += 1
    return ip_counts
