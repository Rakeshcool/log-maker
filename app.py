import psutil
from flask import Flask, render_template, jsonify
from datetime import datetime
import logging
import threading
import time  # Import the time module


app = Flask(__name__)

# Set up logging configuration
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


# Function to log system metrics and warnings
def log_system_metrics():
    while True:
        cpu_metric = psutil.cpu_percent()
        mem_metric = psutil.virtual_memory().percent
        disk_metric = psutil.disk_usage("/").percent

        # Log the system metrics
        logging.info(f"CPU Usage: {cpu_metric}%")
        logging.info(f"Memory Usage: {mem_metric}%")
        logging.info(f"Disk Usage: {disk_metric}%")

        message = None
        if cpu_metric > 80 or mem_metric > 80 or disk_metric > 80:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            message = (
                f"Scale up your system: Device usage is more than 80% at {timestamp}."
            )
            # Log the warning message
            logging.warning(message)

        time.sleep(2)  # Adjust the interval (in seconds) as needed

        # Start the logging thread


logging_thread = threading.Thread(target=log_system_metrics, daemon=True)
logging_thread.start()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/get_metrics")
def get_metrics():
    cpu_metric = psutil.cpu_percent()
    mem_metric = psutil.virtual_memory().percent
    disk_metric = psutil.disk_usage("/").percent

    message = None
    if cpu_metric > 80 or mem_metric > 80 or disk_metric > 80:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message = f"Scale up your system: Device usage is more than 80% at {timestamp}."

    return jsonify(
        cpu_metric=cpu_metric,
        mem_metric=mem_metric,
        disk_metric=disk_metric,
        message=message,
    )


if __name__ == "__main__":
    app.run(debug=True)
