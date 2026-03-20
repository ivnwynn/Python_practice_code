import time 
import logging
import configparser
import lib.monitor as monitor
import lib.alert as alert
import lib.utils as utils

#CONFIGURE LOGGING 
logging.basicConfig(filename='asmat.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

#CONSOLE HANDLER
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

logging.getLogger().addHandler(console_handler)

#OS DETECTOR
def detect_os():
     os_name = platform.system()
     
     if os_name == "Windows":
          print ("Windows:")
     elif os_name == "Linux":
        print("Linux:")
     elif os_name == "Darwin":
          print("MacOS:")
          
     else:
          print("UNKNOWN OS:")
     
     return os_name

#CONFIG LOADER
def load_config(config_file):
     config = configparser.ConfigParser()

     base_path = os.path.dirname(os.path.abspath(__file__))
     config_path = os.path.join(base_path, config_file)
     config.read(config_path)
     return config
  
#MAIN PROGRAM
def main():
    detect_os()
    config = load_config('asmat.conf')
    logging.info("Starting ASMAT...")
    try: 
        while True:
            metrics = monitor.get_system_metrics()
            
            logging.info(f"CPU Usage: {metrics['cpu_usage']}%")
            logging.info(f"Memory Usage: {metrics['memory_usage']}%")
            logging.info(f"Disk Usage: {metrics['disk_usage']}%")

            cpu_threshold = int(config['DEFAULT']['cpu_threshold'])
            memory_threshold = int(config['DEFAULT']['memory_threshold'])
            disk_threshold = int(config['DEFAULT']['disk_threshold'])
    
            if metrics['cpu_usage'] > cpu_threshold:
                subject = "High CPU Usage Alert!"
                body = f"CPU usage is at {metrics['cpu_usage']}%"
                alert.send_email_alert(subject, body, config)

            if metrics['memory_usage'] > memory_threshold:
                subject = "High Memory Usage Alert!"
                body = f"Memory usage is at {metrics['memory_usage']}%"
                alert.send_email_alert(subject, body, config)
            
            if metrics['disk_usage'] > disk_threshold:
                subject = "Low Disk Space Alert!"
                body = f"Disk usage is at {metrics['disk_usage']}%"
                alert.send_email_alert(subject, body, config)

            time.sleep(int(config['DEFAULT']['check_interval'])) # Check every x seconds
    except KeyboardInterrupt:
            logging.info("ASMAT interrupted by user. Exiting...")
    finally:
         logging.info("Asmat exiting.")

if __name__ == "__main__":
            main()
