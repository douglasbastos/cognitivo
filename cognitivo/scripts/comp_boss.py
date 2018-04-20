import csv

from cognitivo.config import PROJECT_ROOT, DBSession
from cognitivo.models import Component, BaseType, OutsideShape

CACHE_KEY = '{tablename}:{key}'


class Cache:
    item = {}

    def get(self, key):
        return self.item.get(key)

    def set(self, key, value):
        self.item[key] = value


def get_or_create(cache, session, table, data):
    if data == 'NA':
        return

    item = cache.get(
        CACHE_KEY.format(
            tablename=table.__tablename__,
            key=data)
    )
    if not item:
        item = table(name=data)
        session.add(item)
        session.commit()
        cache.set(CACHE_KEY.format(
            tablename=table.__tablename__,
            key=data), item)

    return item


def run():
    with open(f'{PROJECT_ROOT}/files/comp_boss.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        cache = Cache()
        session = DBSession()

        for row in reader:
            print(f'Insering row {row["component_id"]}')

            base_type = get_or_create(cache, session,
                                      table=BaseType,
                                      data=row['base_type'])
            outside_shape = get_or_create(cache, session,
                                          table=OutsideShape,
                                          data=row['outside_shape'])

            component = Component(
                id=row['component_id'],
                component_type_id=row['component_type_id'],
                connection_type_id=row['connection_type_id'],
                type=row['type'] if row['type'] != 'NA' else None,
                height_over_tube=row['height_over_tube'],
                bolt_pattern_long=row['bolt_pattern_long'] if row['bolt_pattern_long'] != 'NA' else None,
                bolt_pattern_wide=row['bolt_pattern_wide'] if row['bolt_pattern_wide'] != 'NA' else None,
                groove=True if row['groove'] == 'Yes' else False,
                base_diameter=row['base_diameter'] if row['base_diameter'] != 'NA' else None,
                shoulder_diameter=row['shoulder_diameter'] if row['shoulder_diameter'] != 'NA' else None,
                unique_feature=True if row['unique_feature'] == 'Yes' else False,
                orientation=True if row['orientation'] == 'Yes' else False,
                weight=row['weight'] if row['weight'] != 'NA' else None,
                outside_shape=outside_shape,
                base_type=base_type
            )
            session.add(component)
            session.commit()

        session.close()

if __name__ == '__main__':
    run()
