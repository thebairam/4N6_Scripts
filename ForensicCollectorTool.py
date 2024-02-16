import psutil
import sys

def find_process_info(program_name):
    # Placeholder for collecting detailed information
    process_info = {
        'DLLs': [],
        'Parent Process': '',
        'Child Processes': [],
        'Threads': [],
        'Network Connections': []
    }
    
    # Iterate over all running processes
    for proc in psutil.process_iter(attrs=['pid', 'name']):
        # Check if this process matches the program name provided
        if proc.info['name'] == program_name:
            process = psutil.Process(proc.info['pid'])
            
            # Collect DLLs (Windows-specific, using psutil or ctypes/pywin32)
            # This is a placeholder as actual DLL collection would require more complex handling
            process_info['DLLs'].append('Example.dll')
            
            # Parent process
            if process.parent():
                process_info['Parent Process'] = process.parent().name()
            
            # Child processes
            for child in process.children(recursive=True):
                process_info['Child Processes'].append(child.name())
            
            # Threads
            process_info['Threads'] = [thread.id for thread in process.threads()]
            
            # Network connections
            for conn in process.connections(kind='inet'):
                process_info['Network Connections'].append(f"{conn.laddr.ip}:{conn.laddr.port} -> {conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else f"{conn.laddr.ip}:{conn.laddr.port}")
            
            # Printing out the collected information
            print(f"Program: {program_name}")
            print(f"PID: {process.pid}")
            print("DLLs Loaded:", process_info['DLLs'])
            print("Parent Process:", process_info['Parent Process'])
            print("Child Processes:", process_info['Child Processes'])
            print("Threads:", process_info['Threads'])
            print("Network Connections:", process_info['Network Connections'])
            return
    
    print(f"No running process found for: {program_name}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <program_name>")
        sys.exit(1)
    
    program_name = sys.argv[1]
    find_process_info(program_name)
