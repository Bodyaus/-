inst = '''
Ця програма дозволить вам за допомогою тесту Руф'є провести первинну діагностику вашого здоров'я.\n
Проба Руф'є являє собою навантажувальний комплекс, призначений для оцінки працездатності серця при \n
фізичному навантаженні.
У випробуваного визначають частоту пульсу за 15 секунд.
Потім протягом 45 секунд випробуваний виконує 30 присідань.\n
Після закінчення навантаження пульс підраховується знову: число \n
пульсацій за перші 15 секунд, 30 секунд відпочинку, число пульсацій за останні 15 секунд.\n '''
inst2 = "Давай зараз дізнаємось який ти квас."
inst3 = "З якого ти міста?(назва міста)"
inst4 = "Скільки тобі років?(число)"
inst5 = "Хто ти по гороскопу?"
inst6 = "Ти хлопець чи дівчина?"

inst7 = '''
Протягом хвилини заміряйте пульс двічі \n 
за перші 15 секунд, потім за останні 15 секунд \n 
результати запишіть у відповідні поля'''


def finish(a,b,age,mounth,male_or_female):
   if age >= 18:
      
      a="настоянний"
   else:
      a="свіжий"

   if mounth == "скорпіон":
      
      b="крутий"
   elif mounth == "овен":
      
      b="солодкий"

   elif mounth == "лев":
      
      b="серйозний"

   elif mounth == "стрілець":
      
      b="на хайпі"

   elif mounth == "близнюки":
      
      b="сиильногазований"

   elif mounth == "рак":
      
      b="гіркуватий"

   elif mounth == "ваги":
      
      b="алкогольний"
   
   elif mounth == "":
      
      b="серйозний"