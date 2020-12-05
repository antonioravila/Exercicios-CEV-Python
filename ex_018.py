import math

angulo = float(input('digite um ângulo: '))
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print(f'o seno do ângulo de {angulo}° é {sen:.2f}')
print(f'o cosceno do ângulo de {angulo}° é {cos:.2f}')
print(f'a tangente do ângulo de {angulo}° é {tan:.2f}')
