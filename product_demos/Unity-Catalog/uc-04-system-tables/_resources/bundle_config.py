# Databricks notebook source
# MAGIC %md 
# MAGIC ## Demo bundle configuration
# MAGIC Please ignore / do not delete, only used to prep and bundle the demo

# COMMAND ----------

{
  "name": "uc-04-system-tables",
  "category": "governance",
  "title": "System Tables: Billing Forecast, Usage and Audit",
  "custom_schema_supported": True,
  "default_schema": "dbdemos_billing_forecast",
  "default_catalog": "main",
  "custom_message": "System tables need the be enabled first on UC for this demo to work. See <a href=\"https://notebooks.databricks.com/demos/uc-04-system-tables/index.html#\">_enable_system_tables notebook</a> for more details (also installed as part of the demo).<br/><strong>We have a cache issue loading the dashboard - Please run the 2 widget queries individually to see all SKU & all workspace IDs - we're working on it. To find the queries, search \"System Tables - Distinct workspace id\" and \"System Tables - Distinct SKU\"</strong>",
  "description": "Track and analysis usage, billing & access with UC System tables.",
  "fullDescription": "Databricks Unity Catalog is the world's first AI-powered governance solution for the lakehouse. It empowers enterprises to seamlessly govern their structured and unstructured data, ML models, notebooks, dashboards, and files on any cloud or platform. <br/>Through Delta Sharing, Databricks Unity Catalog offers direct access to many of the lakehouse activity logs exposed in Delta as System Tables. System Tables are the cornerstone of lakehouse observability and enable at-scale operational intelligence on numerous key business questions. <br/>In this demo, we'll show how Unity Catalog System Tables can be used to: <ul><li>Monitor your consumption and leverage the lakehouse AI capabilities to forecast your future usage, triggering alerts when billing goes above your criterias</li><li>Monitor accesses to your data assets</li><li>Monitor and understand your platform usage</li></ul>",
    "usecase": "Data Governance",
  "products": ["Unity Catalog"],
  "related_links": [
      {"title": "View all Product demos", "url": "<TBD: LINK TO A FILTER WITH ALL DBDEMOS CONTENT>"},
      {"title": "Databricks Unity Catalog: Fine grained Governance", "url": "https://www.databricks.com/blog/2021/05/26/introducing-databricks-unity-catalog-fine-grained-governance-for-data-and-ai-on-the-lakehouse.html"}],
  "recommended_items": ["uc-01-acl", "uc-02-external-location", "uc-03-data-lineage"],
  "demo_assets": [],
  "bundle": True,
  "tags": [{"uc": "Unity Catalog"}],
  "notebooks": [
     {
      "path": "_resources/00-setup",
      "pre_run": False,
      "publish_on_website": False,
      "add_cluster_setup_cell": False,
      "title":  "Setup",
      "description": "Init data for demo."
    },
    {
      "path": "00-intro-system-tables", 
      "pre_run": False, 
      "publish_on_website": True, 
      "add_cluster_setup_cell": False, 
      "title":  "Introduction to system tables", 
      "description": "Start here to review the main system tables available."
    },
    {
      "path": "01-billing-tables/01-billing-tables-overview", 
      "pre_run": False,
      "publish_on_website": True, 
      "add_cluster_setup_cell": True, 
      "title":  "Billing table overview", 
      "description": "Explore the billing table to track your usage."
    },
    {
      "path": "01-billing-tables/02-forecast-billing-tables", 
      "pre_run": False, 
      "publish_on_website": True, 
      "add_cluster_setup_cell": True, 
      "title":  "Forecast your consumption", 
      "description": "Leverage the Lakehouse AI capabilities to forecast your usage"
    },
    {
      "path": "02-audit-logs-tables/02-audit-log", 
      "pre_run": False, 
      "publish_on_website": True, 
      "add_cluster_setup_cell": True, 
      "title":  "Audit Log system table", 
      "description": "Track lakehouse operation, including data access"
    },
    {
      "path": "03-lineage-tables/03-lineage", 
      "pre_run": False, 
      "publish_on_website": True, 
      "add_cluster_setup_cell": True, 
      "title":  "Data lineage", 
      "description": "Track data lineage on all assets (tables, workflow, dashboards, AI...)"
    },
    {
      "path": "_enable_system_tables", 
      "pre_run": False, 
      "publish_on_website": True, 
      "add_cluster_setup_cell": False, 
      "title":  "Enable system tables", 
      "description": "Helper to turn on the system tables - read before you run."
    }
  ],
  "init_job": {
    "settings": {
        "name": "dbdemos_billing_forecast_init_{{CURRENT_USER_NAME}}",
        "email_notifications": {
            "no_alert_for_skipped_runs": False
        },
        "timeout_seconds": 0,
        "max_concurrent_runs": 1,
        "tasks": [
            {
                "task_key": "init_data",
                "notebook_task": {
                    "notebook_path": "{{DEMO_FOLDER}}/01-billing-tables/02-forecast-billing-tables",
                    "source": "WORKSPACE",
                    "base_parameters": {"catalog": "main", "schema": "billing_forecast"}
                },
                "job_cluster_key": "Shared_job_cluster",
                "timeout_seconds": 0,
                "email_notifications": {}            
            }
        ],
        "job_clusters": [
            {
                "job_cluster_key": "Shared_job_cluster",
                "new_cluster": {
                    "spark_version": "13.1.x-cpu-ml-scala2.12",
                    "spark_conf": {
                        "spark.master": "local[*, 4]",
                        "spark.databricks.cluster.profile": "singleNode"
                    },
                    "custom_tags": {
                        "ResourceClass": "SingleNode"
                    },
                    "spark_env_vars": {
                        "PYSPARK_PYTHON": "/databricks/python3/bin/python3"
                    },
                    "enable_elastic_disk": True,
                    "data_security_mode": "SINGLE_USER",
                    "runtime_engine": "STANDARD",
                    "num_workers": 0
                }
            }
        ],
        "format": "MULTI_TASK"
    }
  },
  "cluster": {
    "num_workers": 4,
    "single_user_name": "{{CURRENT_USER}}",
    "data_security_mode": "SINGLE_USER",
    "spark_version": "13.3.x-cpu-ml-scala2.12"
  }
}
