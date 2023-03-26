
from kubernetes import client, config, watch
import datetime
import os

def main():
    config.load_kube_config()
    v1 = client.CoreV1Api()
    w = watch.Watch()
    for event in w.stream(v1.list_pod_for_all_namespaces):
        pod = event['object']
        if pod.status.phase != 'Running':
            continue
        logs = v1.read_namespaced_pod_log(name=pod.metadata.name, namespace=pod.metadata.namespace)
        print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} {pod.metadata.namespace}/{pod.metadata.name}: {logs}")

if __name__ == '__main__':
    main()
