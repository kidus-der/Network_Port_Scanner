import os
from datetime import datetime

def save_scan_results(results, directory="logs"):
    """
    Save the scan results to a .txt file. Each scan will generate a unique file name.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)  # Create logs directory if it doesn't exist

    # create a unique log file name based on current timestamp
    file_name = f"scan_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    file_path = os.path.join(directory, file_name)

    # write actual log file content in .txt file
    with open(file_path, 'w') as file:
        file.write("=== Python Port Scanner Results ===\n")
        file.write(f"Scan Date/Time: {datetime.now()}\n\n")
        
        for result in results:

            # if the port is open, write the banner information as well
            if result["status"] == "Open":
                file.write(f"IP: {result['ip']} | Port {result['port']}:\t{result['status']} ({result['service']})\n")
                file.write(f"  Banner: {result['banner']}\n\n")
            else:
                file.write(f"IP: {result['ip']} | Port {result['port']}:\t{result['status']}\n")

    print(f"Scan results logged to: {file_path}")
    return file_path
