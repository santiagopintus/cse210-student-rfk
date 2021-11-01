from game.action import Action

class DrawActorsAction(Action):

    def __init__(self, output_service):
        """An instance of the DrawActorsAction class.

        Attributes:
            output_service (OutputService): The output service to use.
        """
        self._output_service = output_service

    def execute(self, cast):
        """Excetute the action of drawing all actors in the cast.

        Attributes:
            cast (Cast): The cast to draw.
        """
        self._output_service.clear_screen()
        for actors in cast.values():
            self._output_service.draw_actors(actors)
        self._output_service.flush_buffer()