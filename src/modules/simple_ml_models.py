"""
Simple ML Models
"""


class HousePriceModel:

    def __call__(self, area: float, n_floors: int, heating: str):
        heating_map = {
            'A': 100,
            'B': 50,
            'C': 25
        }

        return 100 * n_floors + 5 * area + heating_map.get(heating, 0)


class SentimentModel:
    def __init__(self) -> None:
        self.word_map = {
            'nice': 10,
            'fine': 5,
            'good': 1,
            'hate': -1,
            'bad': -5,
            'disgusting': -10
        }

    def __call__(self, text: str):
        lower_text = text.lower()
        total_score = sum(value for key, value in self.word_map.items() if key in lower_text)
        sentiment = 1 if total_score > 0 else -1 if total_score < 0 else 0
        return {"sentiment": sentiment,
                "score": total_score
                }