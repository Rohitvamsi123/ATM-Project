#ATMOperations.py
from ATMExceptions import DepositError,WithDrawError,InSuffFundError
bal=500.00
def  deposit():
	damt=float(input("Enter how much u want to deposit:"))
	if(damt<=0):
		raise DepositError
	else:
		global bal
		bal=bal+damt
		print("Ur Account xxxxxx123 creadited with INR:{}".format(damt))
		print("Now Ur Account xxxxxx123  Bal INR:{}".format(bal))

def withdraw():
	global bal
	wamt=float(input("Enter how much u want to Withdraw:"))
	if(wamt<=0):
		raise WithDrawError
	elif((wamt+500)>bal):
		raise InSuffFundError
	else:
		bal=bal-wamt
		print("Ur Account xxxxxx123 Debited with INR:{}".format(wamt))
		print("Now Ur Account xxxxxx123  Bal INR:{}".format(bal))

def  balenq():
	print("Ur Account xxxxxx123  Bal INR:{}".format(bal))

