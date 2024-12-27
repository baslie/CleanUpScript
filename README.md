# CleanUpScript

## Описание
**CleanUpScript** — это утилита на языке Python для автоматического удаления заданных файлов и папок в текущей директории и её поддиректориях. Этот инструмент может быть полезен для очистки файловой системы от ненужных файлов или папок по заранее заданному списку.

### Ключевые возможности
- Подсчёт количества файлов и папок, подлежащих удалению.
- Удаление файлов и папок с отображением прогресса выполнения.
- Управление списком удаляемых файлов и папок через редактирование исходного кода.
- Обработка ошибок при удалении, с выводом подробных сообщений.

## Установка

1. Убедитесь, что у вас установлен Python версии 3.6 или выше.
2. Скачайте или клонируйте репозиторий:
   ```bash
   git clone https://github.com/baslie/CleanUpScript.git
   ```
3. Перейдите в директорию проекта:
   ```bash
   cd CleanUpScript
   ```

## Использование

1. Откройте файл `delete_files.py` в текстовом редакторе.
2. Отредактируйте списки `files_to_delete` и `folders_to_delete`, добавив в них имена файлов и папок, которые нужно удалить. Пример:
   ```python
   files_to_delete = [
       "example_file.txt",
       "document.docx",
   ]

   folders_to_delete = ["example_folder"]
   ```
3. Запустите скрипт из командной строки или терминала:
   ```bash
   python delete_files.py
   ```
4. Скрипт отобразит количество найденных файлов и папок для удаления, а затем начнёт процесс их удаления с прогрессом.

### Примечания
- Скрипт удаляет файлы и папки в текущей директории и всех её поддиректориях.
- Убедитесь, что у вас есть права доступа для удаления указанных файлов и папок.
- Используйте с осторожностью, чтобы случайно не удалить нужные файлы.

## Автор
Этот проект разработан [baslie](https://github.com/baslie).

## Лицензия
Этот проект распространяется под лицензией MIT. Подробности можно найти в файле [LICENSE](LICENSE).
