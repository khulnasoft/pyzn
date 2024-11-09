import os

from behave.runner import Context


def before_all(context: Context):
    os.environ["APPLICATION_ENV"] = "test"
    from pyzn.infrastructure import container
    from pyzn.infrastructure.web import app

    context.container = container
    context.client = app.test_client()


def before_scenario(context, _):
    context.container.mongo_client.pyzn_test.projects.delete_many({})
    context.container.mongo_client.pyzn_test.project_downloads.delete_many({})
