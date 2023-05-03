import os
from contextlib import contextmanager
from winshell import desktop

DESKTOP_PATH = desktop()

def create_bot_folder():
  bot_path = os.path.join(DESKTOP_PATH, "bot")
  if not os.path.exists(bot_path):
    os.mkdir(bot_path)
  return bot_path

def create_folder_reference_task(task):
  bot_path = create_bot_folder()
  task_folder_path = os.path.join(bot_path, task)
  if not os.path.exists(task_folder_path):
    os.mkdir(task_folder_path)
  return task_folder_path

@contextmanager
def create_file_log_task(task):
  task_folder_path = create_folder_reference_task(task)
  log_file_path = os.path.join(task_folder_path, f"{task}.txt")
  yield open(log_file_path, "w")
