fake_measures = {1: {'name': 'test1'}}

fake_recipes = {
    1: {'name': 'sandwich'},
    2: {'name': 'pancake'},
    3: {'name': 'scrambled egg'},
}


class FakeMeasureRepository:
    def create_measure(self, json: dict):
        pass

    def get_measure(self, id: int):
        fake_measures.get(id)