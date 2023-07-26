import psutil
from flask import Flask, render_template, jsonify
import os

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
        message = "Scale up your system: Device usage is more than 80%."

    return jsonify(
        cpu_metric=cpu_metric,
        mem_metric=mem_metric,
        disk_metric=disk_metric,
        message=message,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0")
