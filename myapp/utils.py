import random

def create_new_ref_number():
      return "CARG-" + str(random.randint(1000000000, 9999999999))

def customer_ref():
      return "CARG-C-" + str(random.randint(1000000000, 9999999999))

def product_ref():
      return "CPN" + str(random.randint(1000000000, 9999999999))

def carrier_ref():
      return "CA-" + str(random.randint(1000000000, 9999999999))