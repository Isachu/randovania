from PySide2 import QtWidgets

from randovania.game_description.game_patches import GamePatches
from randovania.games.game import RandovaniaGame
from randovania.layout.base.base_configuration import BaseConfiguration


class GameDetailsTab:
    def __init__(self, parent: QtWidgets.QWidget, game: RandovaniaGame):
        self.game_enum = game

    def widget(self) -> QtWidgets.QWidget:
        raise NotImplementedError()

    def tab_title(self) -> str:
        raise NotImplementedError()

    def update_content(self, configuration: BaseConfiguration, patches: GamePatches):
        raise NotImplementedError()
