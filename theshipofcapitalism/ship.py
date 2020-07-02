class ship:
   def __init__(self, hp, speed, shield, attack, overwhelming):
      self.hp = hp
      self.speed = speed
      self.shield = shield
      self.attack = attack
      self.overwhelming = overwhelming



   def seperated(self):
      self.hp = self.hp / 2
      self.speed = self.speed / 2
      self.shield = self.shield / 2
      self.attack = self.attack / 2
      self.overwhelming = self.overwhelming / 2
      print(self.hp, self.speed, self.shield, self.attack, self.overwhelming)
      return self


class bullet:
   def __init__(self, attack, speed):
      self.attack = attack
      self.speed = speed
      print(attack)



class enemy:
   def __init__(self, hp, shield, general_attack, laser_attack, special_attack, hidden_attack, level_counter):
      self.hp = hp
      self.shield = shield
      self.general_attack = general_attack
      self.laser_attack = laser_attack
      self.special_ataack = special_attack
      self.hidden_attack = hidden_attack
      self.level_counter = level_counter

   def destroyed(self):
      if self.hp <= 0 and self.level_counter > 0:
         print('다음 단계를 출력합니다.')
         self.level_counter -= 1
         return self.level_counter

      elif self.hp <= 0 and self.level_counter <= 0:
         print('적이 완전히 처치되었습니다.')

      else:
         print('적이 아직 싸우고 있습니다')
