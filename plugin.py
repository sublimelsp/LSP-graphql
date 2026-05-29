from __future__ import annotations

from LSP.plugin import LspPlugin
from LSP.plugin import OnPreStartContext
from lsp_utils import NodeManager
from pathlib import Path
from sublime_lib import ResourcePath
from typing_extensions import override


def plugin_loaded() -> None:
    LspGraphqlPlugin.register()


def plugin_unloaded() -> None:
    LspGraphqlPlugin.unregister()


class LspGraphqlPlugin(LspPlugin):

    @classmethod
    @override
    def on_pre_start_async(cls, context: OnPreStartContext) -> None:
        package_name = cls.plugin_storage_path.name
        NodeManager.on_pre_start_async(
            context,
            cls.plugin_storage_path,
            ResourcePath('Packages', package_name, 'language-server'),
            Path('start-server.js'),
            node_version_requirement='>=14',
        )
