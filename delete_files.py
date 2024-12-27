import os
import sys

# Список имен файлов и папок, которые нужно удалить
files_to_delete = [
    "Название ярлыка.url",
    "Название файла.docx",
]

folders_to_delete = [
    "Пример папки для удаления",
]

# Получение текущей директории, откуда запускается скрипт
current_directory = os.getcwd()

# Подсчет количества файлов и папок для удаления
files_count = 0
folders_count = 0
for root, dirs, files in os.walk(current_directory):
    files_count += sum(1 for file in files if file in files_to_delete)
    folders_count += sum(1 for folder in dirs if folder in folders_to_delete)

total_items = files_count + folders_count

# Вывод общего количества объектов для удаления
print(
    f"Объектов для удаления: {total_items} (Файлов: {files_count}, Папок: {folders_count})"
)

# Удаление файлов и отображение прогресса
deleted_count = 0
for root, dirs, files in os.walk(current_directory, topdown=False):
    # Удаление файлов
    for file in files:
        if file in files_to_delete:
            file_path = os.path.join(root, file)
            try:
                os.remove(file_path)
                deleted_count += 1
                sys.stdout.write(f"\rУдалено {deleted_count} из {total_items}...")
                sys.stdout.flush()

            except Exception as e:
                print(f"\nНе удалось удалить файл {file_path}: {e}")

    # Удаление папок
    for folder in dirs:
        if folder in folders_to_delete:

            folder_path = os.path.join(root, folder)
            try:
                os.rmdir(folder_path)
                deleted_count += 1
                sys.stdout.write(f"\rУдалено {deleted_count} из {total_items}...")
                sys.stdout.flush()
            except Exception as e:
                print(f"\nНе удалось удалить папку {folder_path}: {e}")

print(f"\nЗавершено! Удалено объектов: {deleted_count}")