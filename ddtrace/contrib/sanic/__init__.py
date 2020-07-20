"""
The Sanic__ integration will add tracing to all requests to your Sanic application.


Enable Sanic tracing automatically via ``ddtrace-run``::

    ddtrace-run python app.py

Sanic tracing can also be enabled manually::

    from ddtrace import patch_all
    patch_all()
    
    from sanic import Sanic
    from sanic.response import text

    app = Sanic(__name__)

    @app.route('/')
    def index(request):
        return text('hello world')

    if __name__ == '__main__':
        app.run()


Configuration
~~~~~~~~~~~~~

.. py:data:: ddtrace.config.sanic['distributed_tracing_enabled']

   Whether to parse distributed tracing headers from requests received by your Sanic app.

   Default: ``True``

.. py:data:: ddtrace.config.sanic['analytics_enabled']

   Whether to analyze spans for Sanic in App Analytics.

   Can also be enabled with the ``DD_SANIC_ANALYTICS_ENABLED`` environment variable.

   Default: ``None``

.. py:data:: ddtrace.config.sanic['service_name']

   The service name reported for your Sanic app.

   Can also be configured via the ``DD_SERVICE`` environment variable.

   Default: ``'Sanic'``


Example::

    from ddtrace import config

    # Enable distributed tracing
    config.sanic['distributed_tracing_enabled'] = True

    # Override service name
    config.sanic['service_name'] = 'custom-service-name'

.. __: https://sanic.readthedocs.io/en/latest/
"""

from ...utils.importlib import require_modules


required_modules = ['sanic']

with require_modules(required_modules) as missing_modules:
    if not missing_modules:
        from .patch import patch, unpatch

        __all__ = ['patch']