import csv
from numbers import Integral

from sqlalchemy.exc import IntegrityError

from cognitivo.config import PROJECT_ROOT, DBSession
from cognitivo.models import Component, BaseType, OutsideShape, TubeAssembly, \
    TubeAssemblyHasComponent


def run():
    with open(f'{PROJECT_ROOT}/files/bill_of_materials.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        session = DBSession()

        for row in reader:
            print(f"Insering row {row['tube_assembly_id']}")

            tube_assemly = TubeAssembly(id=row['tube_assembly_id'])
            session.add(tube_assemly)
            session.commit()

            for i in range(1, 9):
                if row[f'component_id_{i}'] == 'NA':
                    break

                item = TubeAssemblyHasComponent(
                    tube_assembly_id=tube_assemly.id,
                    component_id=row[f'component_id_{i}'],
                    quantity=row[f'quantity_{i}']
                )
                session.add(item)
                try:
                    session.commit()
                except IntegrityError:
                    session.rollback()
                    print(f'Ignorando repetição em tube_assembly_id: {tube_assemly.id}')

        session.close()


if __name__ == '__main__':
    run()
