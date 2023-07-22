import logging
from robusta.api import *
from kubernetes import client, config

kube_config = config.load_incluster_config()
api_client = client.ApiClient(kube_config)
kube_client = client.CustomObjectsApi(api_client)

POLICY_REPORT_GROUP = "wgpolicyk8s.io"
POLICY_REPORT_VERSION = "v1alpha2"
POLICY_REPORT_PLURAL = "policyreports"
NAMESPACE = "default"


@action
def format_kyverno_policy_reports(event: ScheduledExecutionEvent):
    custom_object = \
        kube_client.list_namespaced_custom_object(
            POLICY_REPORT_GROUP,
            POLICY_REPORT_VERSION,
            NAMESPACE,
            POLICY_REPORT_PLURAL
        )

    all_policy_reports = custom_object.get('items')
    
    logging.info(f"These are all policy reports{all_policy_reports}")
