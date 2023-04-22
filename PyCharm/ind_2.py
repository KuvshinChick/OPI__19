import argparse
import collections
from pathlib import Path


# Подсчет файлов в каталоге
def tree_count(path, seen, head="", tail=""):
    if path.resolve() not in seen:
        # path.resolve () преобразование в абсолютный путь
        seen.add(path.resolve())

        if path.is_dir():
            dirs = sorted(filter(Path.is_dir, path.iterdir()))
            files = sorted(filter(Path.is_file, path.iterdir()))
            cnt = dict(collections.Counter(p.suffix for p in files))

        if len(cnt) > 0:
            print(head + path.name + " " + str(cnt))
        else:
            print(head + path.name)

        for i, entry in enumerate(dirs):
            if i < len(dirs) - 1:
                tree_count(entry, seen, tail + "├──", tail + "│  ")
            else:
                tree_count(entry, seen, tail + "└──", tail + "   ")


# вывод древовидной структуры каталогов
def tree_d(path, seen, head="", tail=""):
    if path.resolve() not in seen and path.is_dir():
        # path.resolve () преобразование в абсолютный путь
        seen.add(path.resolve())
        print(head + path.name)
        entries = sorted(filter(Path.is_dir, path.iterdir()))
        for i, entry in enumerate(entries):
            if i < len(entries) - 1:
                tree_d(entry, seen, tail + "├──", tail + "│  ")
            else:
                tree_d(entry, seen, tail + "└──", tail + "   ")


# вывод древовидной структуры всех файлов
def tree_a(path, seen, head="", tail=""):
    if path.resolve() not in seen:
        # path.resolve () преобразование в абсолютный путь
        seen.add(path.resolve())
        print(head + path.name)
        # entries = sorted(path.glob('*'))
        dirs = []
        files = []
        # Сортировка: сначала папки, потом - файлы
        if path.is_dir():
            dirs = sorted(filter(Path.is_dir, path.iterdir()))
            files = sorted(filter(Path.is_file, path.iterdir()))
        entries = dirs + files
        for i, entry in enumerate(entries):
            if i < len(entries) - 1:
                tree_a(entry, seen, tail + "├──", tail + "│  ")
            else:
                tree_a(entry, seen, tail + "└──", tail + "   ")


# вывод древовидной структуры полных путей файлов
def tree_f(path, seen, head="", tail=""):
    if path.resolve() not in seen:
        # path.resolve () преобразование в абсолютный путь
        seen.add(path.resolve())
        print(head + str(path))
        # entries = sorted(path.glob('*'))
        dirs = []
        files = []
        # Сортировка: сначала папки, потом - файлы
        if path.is_dir():
            dirs = sorted(filter(Path.is_dir, path.iterdir()))
            files = sorted(filter(Path.is_file, path.iterdir()))
        entries = dirs + files
        for i, entry in enumerate(entries):
            if i < len(entries) - 1:
                tree_f(entry, seen, tail + "├──", tail + "│  ")
            else:
                tree_f(entry, seen, tail + "└──", tail + "   ")


def main(command_line=None):
    # Создать основной парсер командной строки.
    parser = argparse.ArgumentParser(description="tree")

    parser.add_argument(
        "path",
        help="path, cwd - Path.cwd(), home - Path.home()"
    )

    subparser_1 = parser.add_subparsers(dest="command", required=False)

    # Создать субпарсер для вывода только директорий
    subparser_1.add_parser("d", help="directories only")

    # Создать субпарсер для вывода всех файлов
    subparser_1.add_parser("a", help="all files")

    # Создать субпарсер для вывода всех файлов вместе с их полными путями
    subparser_1.add_parser("f", help="all files")

    # Создать субпарсер для вывода кол-ва различных файлов в каталоге
    subparser_1.add_parser("c", help="count files")

    # Выполнить разбор аргументов командной строки.
    args = parser.parse_args()

    # Если заданы значения cwd/home или выбранный каталог
    if args.path == "cwd":
        path = Path.cwd()
    elif args.path == "home":
        path = Path.home()
    else:
        path = Path(args.path)

    # разбор команд если путь существует
    if path.exists():
        if args.command == "d":
            tree_d(path, set())
        elif args.command == "a":
            tree_a(path, set())
        elif args.command == "f":
            tree_f(path, set())
        elif args.command == "c":
            tree_count(path, set())
        # по дефолту - вывод всех файлов
        else:
            tree_a(path, set())

    else:
        print("err")


if __name__ == "__main__":
    main()
