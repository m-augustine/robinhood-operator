import asyncio
import pprint

import kopf
import pykube
import yaml

@kopf.on.startup()
async def startup_fn_simple(logger, **kwargs):
    logger.info('Starting ...')
    await asyncio.sleep(1)

@kopf.on.cleanup()
async def cleanup_fn(logger, **kwargs):
    logger.info('Cleaning ...')
    await asyncio.sleep(3)

@kopf.on.update('equity')
def update(body, meta, spec, status, old, new, diff, **kwargs):
    print('Handling the diff')
    pprint.pprint(list(diff))


@kopf.on.delete('equity')
def delete(body, meta, spec, status, **kwargs):
    pass

@kopf.on.create('equity')
def create_pod(spec, **kwargs):
    print("Whamo")

    # Render the pod yaml with some spec fields used in the template.
    deployment = yaml.safe_load(f"""
        apiVersion: apps/v1
        kind: Deployment
        metadata:
            name: equity-{spec.get('ticker', "null")}
        spec:
            replicas: 1
            selector:
                matchLabels:
                    equity: {spec.get('ticker', "null")}
            template:
                metadata:
                labels:
                    equity: {spec.get('ticker', "null")}
                spec:
                    containers:
                    - name: equity-{spec.get('ticker', "null")}
                        image: {spec.get('image', "null")}
                        env:
                            - name: DELAY
                              value: 30
                            - name: ROBINHOOD_USERNAME
                              value: 30
                            - name: ROBINHOOD_PASSWORD
                              value: 30
                            - name: ROBINHOOD_otp
                              value: 30
                        ports:
                        - containerPort: 9200
    """)

    # # Make it our child: assign the namespace, name, labels, owner references, etc.
    # kopf.adopt(pod_data)
    # kopf.label(pod_data, {'application': 'kopf-example-10'})

    # # Actually create an object by requesting the Kubernetes API.
    # api = pykube.HTTPClient(pykube.KubeConfig.from_env())
    # pod = pykube.Pod(api, pod_data)
    # pod.create()
    # api.session.close()


@kopf.on.event('pods', labels={'application': 'kopf-example-10'})
def example_pod_change(logger, **kwargs):
    logger.info("This pod is special for us.")
