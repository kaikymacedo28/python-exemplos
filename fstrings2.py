#Formatação de Strings com várias linhas
escola = 'Senai'
curso = 'Desenvolvimento de Sistemas'
uc = 'Lógica de Programação'
Matricula = 34
nota = 8.999999
print(f"Escola: {escola}\n"
      f"Curso: {curso}\n"
      f"Unidade Curricular: {uc}"
      f"Matrícula: {Matricula:06d}"
      f"Nota: {nota:.2f}")