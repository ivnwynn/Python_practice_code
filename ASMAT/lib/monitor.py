import psutil
import os 

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    return psutil.virtual_memory().percent

def get_disk_usage(path):
    try:
        usage = psutil.disk_usage(path)
        return usage.percent
    except Exception as e:
        print(f"Error getting disk usage for {path}: {e}")
        return None
    
def get_system_metrics():
    metrics = {}
    metrics['cpu_usage'] = get_cpu_usage()
    memory = psutil.virtual_memory()
    metrics['memory_usage'] = memory.percent
    disk = psutil.disk_usage('/')
    metrics['disk_usage'] = disk.percent
    net_io = psutil.net_io_counters()
    metrics['bytes_sent'] = net_io.bytes_sent
    metrics['bytes_recv'] = net_io.bytes_recv

    if os.name == 'posix':
        try:
            load_avg = os.getloadavg()
            metrics['load_1'] = load_avg[0]
            metrics['load_5'] = load_avg[1]  
            metrics['load_15'] = load_avg[2] 
        except OSError:
            metrics['load_1'] = None
            metrics['load_5'] = None
            metrics['load_15'] = None
    else:
       metrics['load_1'] = None
       metrics['load_5'] = None
       metrics['load_15'] = No

    return metrics

if __name__ == '__main__':
    metrics = get_system_metrics()
    for key, value in metrics.items():
        print(f"{key}: {value}")

