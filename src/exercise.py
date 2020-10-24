from payment_card import PaymentCard
def main():
  pauls_card = PaymentCard(20)
  matts_card = PaymentCard(30)

  pauls_card.eat_heartily()
  matts_card.eat_affordably()
  print("Paul: %s"%pauls_card)
  print("Matt: %s"%matts_card)

  pauls_card.add_money(20)
  matts_card.eat_heartily()
  print("Paul: %s"%pauls_card)
  print("Matt: %s"%matts_card)

  pauls_card.eat_affordably()
  pauls_card.eat_affordably()
  matts_card.add_money(50)
  print("Paul: %s"%pauls_card)
  print("Matt: %s"%matts_card)
  

if __name__ == '__main__':
    main()
