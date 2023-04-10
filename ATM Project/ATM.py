#ATM.py
from ATMMenu  import menu
from ATMExceptions import DepositError,WithDrawError,InSuffFundError
from ATMOperations import deposit,withdraw,balenq
import sys
while(True):
	try:
		menu()
		ch=int(input("Enter ur Choice:"))
		match(ch):
			case 1:
				try:
					deposit()
				except DepositError:
					print("Don't enter -ve amount / zero to deposit")
				except ValueError:
					print("Don't enter alnums,str and symbols for Deposit Operations")
			case 2: 
				try:
					withdraw()
				except WithDrawError:
					print("Don't enter -ve amount / zero to Withdraw")
				except ValueError:
					print("Don't enter alnums,str and symbols for Withdraw Operations")
				except InSuffFundError:
					print("Ur Account has no Sufficient Balance")
			case 3:
				balenq()
			case 4:
				print("Thx for using this ATM")
				sys.exit()
			case _:
				print("Ur Selection Operation is wrong--try again")
	except ValueError:
		print("Don't enter alnums,strs and symbols for Choice of Operation:")