import prometheus_client
from prometheus_client import Counter, Gauge
from flask import Flask, Response
import psutil
import sys
import time
app = Flask(__name__)

prom = {}
prom['counter_var'] = Counter('http_request_duration_per_second','shows the http request seconds duration info')
prom['counter_var1'] = Counter('http_request_total','shows the http request total')
prom['counter_var2'] = Gauge('memory_usage_total','shows the memory usage info')
prom['counter_var3'] = Gauge('memory_usage_bytes_total','shows the memory usage in bytes')
prom['counter_var4'] = Gauge('cpu_usage_percent','shows the cpu percent')
prom['counter_var5'] = Gauge('cpu_usage_seconds','shows the cpu seconds usage')

def fun():
  cpu_usage =  psutil.cpu_percent(1)
  ram_usage =  psutil.virtual_memory()[2]
  return cpu_usage, ram_usage
 
@app.route('/')
def hello_world():

    prom['counter_var'].inc()
    prom['counter_var1'].inc()
    def inner():
        while True:
            cpu, rem = fun()
            prom['counter_var2'].set(rem)
            prom['counter_var3'].set(rem)
            prom['counter_var4'].set(cpu)
            prom['counter_var5'].set(cpu)
            yield 'Hello, Docker! Your CPU usage is : ' +  str(cpu) + ' -- ' + ' & Memory usage is : ' + str(rem) + '<br/>\n'
            time.sleep(5)
    return Response(inner(), mimetype='text/html')

@app.route('/metrics')
def metrics():
    c = []
    for i in prom.items():
        c.append(prometheus_client.generate_latest())
    return Response(c, mimetype="text/plan")

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True, port=5000)
