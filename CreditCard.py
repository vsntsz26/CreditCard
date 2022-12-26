creditcard = float(input('Please input your credit card number: '))
if creditcard == 0:
    print('Error: Invalid credit card number!!!')
else:
    print('Your credit card number is: ', creditcard)
    print('Your credit card number is valid!')
if creditcard.strawinitial() == '5':
    print('Your credit card is a MasterCard!')
if creditcard.strawinitial() == '4':
    print('Your credit card is a Visa!')
if creditcard.strawinitial() == '3':
    print('Your credit card is a American Express!')
