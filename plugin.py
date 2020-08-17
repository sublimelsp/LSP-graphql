import os
from LSP.plugin.core.typing import Dict, List
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

    @classmethod
    def get_binary_arguments(cls):
        return ['server', '--method', 'stream']
