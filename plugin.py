import os
from lsp_utils import NpmClientHandler


def plugin_loaded() -> None:
    LspGraphqlPlugin.setup()


def plugin_unloaded() -> None:
    LspGraphqlPlugin.cleanup()


class LspGraphqlPlugin(NpmClientHandler):
    package_name = __package__
    server_directory = 'language-server'
    server_binary_path = os.path.join(
        server_directory, 'node_modules', 'graphql-language-service-cli', 'bin', 'graphql.js'
    )
