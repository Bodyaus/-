inst = '''
Ця програма дозволить вам за допомогою тесту Руф'є провести первинну діагностику вашого здоров'я.\n
Проба Руф'є являє собою навантажувальний комплекс, призначений для оцінки працездатності серця при \n
фізичному навантаженні.
У випробуваного визначають частоту пульсу за 15 секунд.
Потім протягом 45 секунд випробуваний виконує 30 присідань.\n
Після закінчення навантаження пульс підраховується знову: число \n
пульсацій за перші 15 секунд, 30 секунд відпочинку, число пульсацій за останні 15 секунд.\n '''
inst2 = "Давай зараз дізнаємось який ти квас."
inst3 = "Виконайте 30 присідань за 45 секунд"

inst4 = '''
Протягом хвилини заміряйте пульс двічі \n 
за перші 15 секунд, потім за останні 15 секунд \n 
результати запишіть у відповідні поля'''
def test(P1, P2, P3):
   '''повертає значення індексу за трьома показниками пульсу для звірки з таблицею'''
   return ((4*(P1+P2+P3))-200)/10

def finish(a,new_age):
   if new_age >=7 and new_age <=8:
      if a <= 6.4:
         return "чудово"
      if a >= 6.5 and a <= 11.9:
         return "добре"
      if a >= 12 and a <= 16.9:
         return "задовільно"
      if a >= 17 and a <= 20.9:
         return "слабкий"
      if a >= 21:
         return "незадовільно"
      
   if new_age >=9 and new_age <=10:
      if a <= 4.9:
         return "чудово"
      if a >= 5 and a <= 10.4:
         return "добре"
      if a >= 10.5 and a <= 15.4:
         return "задовільно"
      if a >= 15.5 and a <= 19.4:
         return "слабкий"
      if a >= 19.5:
         return "незадовільно"