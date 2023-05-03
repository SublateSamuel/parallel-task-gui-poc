import time
from add_on import labels


def bot_run(log_file, task):
  # Simulação de uma tarefa que demora 5 segundos
  log_file.write(f"Iniciando tarefa -> {task[0]}\n")
  log_file.write(f"Dados da tarefa {task}\n")
  
  for i in range(1, 11):
    time.sleep(1)
    
    # Registra o progresso da tarefa no arquivo de log
    log_file.write(f"Progresso da Tarefa -> {task}: {i}/10\n")
    
  # Atualiza o status da tarefa para 'concluída'
  log_file.write("Tarefa concluída com sucesso.\n")