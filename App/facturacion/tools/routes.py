from flask import Blueprint, jsonify, Flask
from facturacion.tools.utils import server_status
import psutil

tools = Blueprint('tools', __name__)


@tools.route('/health', methods=['GET'])
def health_check() -> dict:
    '''
    Check if the server is up
    status: OK, SLOW, CRITICAL
    memory_usage: percentage of memory usage
    cpu_usage: percentage of cpu usage
    port: port where the server is running
    message: Server is up and running
    '''
    cpu = psutil.cpu_percent()
    return jsonify({
        "status": f"{server_status()}",
        "memory_usage": f"{getattr(psutil.virtual_memory(), 'percent')}%",
        "cpu_usage": f"{cpu}%",
        "port": 5555,
        "message": "Server is up and running",
    })
