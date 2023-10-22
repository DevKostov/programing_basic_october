import random
from datetime import datetime
from locale import setlocale, LC_ALL
from string import Template
from typing import Iterable

BODY_TEMPLATE = Template(
    '''Lotto 6aus49: $lotto

Eurojackpot Zahlen: $euro_1
Eurojackpot Eurozahlen: $euro_2

generiert am: $now von Herrn Enzo
'''
)


def generate_lotto(
        highest: int, n: int,
) -> list[int]:
    numbers = range(1, 1 + highest)
    return sorted(random.sample(numbers, n))


def generate_body(
        lotto: Iterable[int],
        euro_1: Iterable[int],
        euro_2: Iterable[int],
        now: datetime,
) -> str:
    return BODY_TEMPLATE.substitute(
        lotto=', '.join(str(i) for i in lotto),
        euro_1=', '.join(str(i) for i in euro_1),
        euro_2=', '.join(str(i) for i in euro_2),
        now=now.strftime('%c'),
    )


def generate_textfile(
        body: str,
        now: datetime,
        stem: str = 'Lottozahlen generiert am ',
) -> None:
    with open(f'{stem}{now.isoformat()}.txt', 'w') as f:
        f.write(body)


def main() -> None:
    setlocale(LC_ALL, 'de_DE.UTF-8')

    now = datetime.now()

    body = generate_body(
        lotto=generate_lotto(50, 6),
        euro_1=generate_lotto(50, 5),
        euro_2=generate_lotto(12, 2),
        now=now,
    )
    print(body)
    generate_textfile(body, now)

    print('Die Text Datei wurde erfolgreich erstellt.')


if __name__ == '__main__':
    main()
