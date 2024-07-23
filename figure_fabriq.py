

class FigureFactory:

    def __init__(self, figures: list[object], figures_names: list[str]):
        """Raises exceptions if class to figure or figure name are missing"""
        if len(figures) > len(figures_names):
            raise Exception('Please, provide name for additional figure class')
        elif len(figures_names) > len(figures):
            raise Exception('Some of named figures are missing!')
        self.figures_map = dict(zip([x.lower() for x in figures_names], figures))
        self.factory = None

    def chose_factory(self, figure_name: str, *args):
        """Finds suited class in provided lists"""
        try:
            self.factory = self.figures_map[figure_name.lower()](*args)
        except KeyError:
            raise KeyError('This figure class yet not implemented')

    def calculate_area(self, figure_name: str, *args):
        self.chose_factory(figure_name, *args)
        return self.factory.area()


