import psutil
from flask import Flask, render_template, jsonify
from datetime import datetime

# from csv_logger import CsvLogger
# import logging


app = Flask(__name__)


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


# filename = "logs/log.csv"
# delimiter = ","
# level = logging.INFO
# custom_additional_levels = ["logs_a", "logs_b", "logs_c"]
# fmt = f"%(asctime)s{delimiter}%(levelname)s{delimiter}%(message)s"
# datefmt = "%Y/%m/%d %H:%M:%S"
# max_size = 1024  # 1 kilobyte
# max_files = 4  # 4 rotating files
# header = ["date", "level", "value_1", "value_2"]

# # Creat logger with csv rotating handler
# csvlogger = CsvLogger(
#     filename=filename,
#     delimiter=delimiter,
#     level=level,
#     add_level_names=custom_additional_levels,
#     add_level_nums=None,
#     fmt=fmt,
#     datefmt=datefmt,
#     max_size=max_size,
#     max_files=max_files,
#     header=header,
# )


if __name__ == "__main__":
    app.run(debug=True)
