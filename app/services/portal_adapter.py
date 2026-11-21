from typing import List, Dict, Any

SUPPORTED_PORTALS: List[Dict[str, Any]] = [{"id": "cian", "name": "Циан (CIAN)", "badge": "🇷🇺 Циан"}, {"id": "avito", "name": "Авито Недвижимость", "badge": "🇷🇺 Авито"}, {"id": "domclick", "name": "Домклик Сбер", "badge": "🇷🇺 Домклик"}, {"id": "yandex_realty", "name": "Яндекс Недвижимость", "badge": "🇷🇺 Яндекс"}, {"id": "mirkvartir", "name": "Мир Квартир", "badge": "🇷🇺 Мир Квартир"}]

def get_portal_by_id(portal_id: str):
    for p in SUPPORTED_PORTALS:
        if p["id"] == portal_id:
            return p
    return None
