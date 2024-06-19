while True:
  import random
  numero_random=random.randint(1,10)
  print("\nIngresa un numero del 1 al 10")
  numero=int(input())
  if numero==numero_random:
    print("JAJAJA, Escogiste el numero random, que gay")
  if numero>=11:
    print("Opcion No Valida")
  if numero!=numero_random:
    print("Te Salvaste brother")
    print(f"El numero era {numero_random}")
    print("Felicidades, NO eres GAY")
    
