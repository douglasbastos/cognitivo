import csv

from cognitivo.config import PROJECT_ROOT, DBSession
from cognitivo.models import Component, BaseType, OutsideShape


class Cache:
    item = {}

    def get(self, key):
        return self.item.get(key)

    def set(self, key, value):
        self.item[key] = value


def run():
    with open(f'{PROJECT_ROOT}/files/comp_boss.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        cache = Cache()
        session = DBSession()

        key_pattern_in_cache = '{tablename}:{key}'

        for row in reader:
            # BASE_TYPE
            print('Insering row')
            base_type = cache.get(
                key_pattern_in_cache.format(
                    tablename='base_type',
                    key=row['base_type'])
            )
            if not base_type:
                base_type = BaseType(name=row['base_type'])
                session.add(base_type)
                session.commit()
                cache.set(key_pattern_in_cache.format(
                    tablename='base_type',
                    key=row['base_type']), base_type)

            # outside_shape
            outside_shape = cache.get(
                key_pattern_in_cache.format(
                    tablename='outside_shape',
                    key=row['outside_shape'])
            )
            if not outside_shape:
                outside_shape = OutsideShape(name=row['outside_shape'])
                session.add(outside_shape)
                session.commit()
                cache.set(key_pattern_in_cache.format(
                    tablename='outside_shape',
                    key=row['outside_shape']), outside_shape)

            # TODO: lembrar de validar o NA
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
                outside_shape_id=outside_shape.id,
                base_type_id=base_type.id
            )
            session.add(component)
            session.commit()

        session.close()

if __name__ == '__main__':
    run()
