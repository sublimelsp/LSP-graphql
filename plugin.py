from __future__ import annotations

from lsp_utils import NpmClientHandler
import os


def plugin_loaded() -> None:
    LspGraphqlPlugin.setup()


def plugin_unloaded() -> None:
    LspGraphqlPlugin.cleanup()


class LspGraphqlPlugin(NpmClientHandler):
    package_name = str(__package__)
    server_directory = 'language-server'
    server_binary_path = os.path.join(server_directory, 'start-server.js')
