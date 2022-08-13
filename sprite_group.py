from tile import Tile
from entity import Entity

class TileGroup(list[Tile]):

    def update(self) -> None:
        for i in self:
            i.update()

    def draw(self) -> None:
        for i in self:
            i.draw()


    def sort_by_y(self) -> None:
        """
        lambda function to sort it by Y for camera optimization
        although this might be completely unecessary as I am rendering everything systematically in the main renderer
        """
        pass

class EntityGroup(list[Entity]):

    def update(self) -> None:
        for i in self:
            i.update()

    def draw(self) -> None:
        for i in self:
            i.draw()


    def sort_by_y(self) -> None:
        """
        lambda function to sort it by Y for camera optimization
        although this might be completely unecessary as I am rendering everything systematically in the main renderer
        """
        pass
