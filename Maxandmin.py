def min(swal):
    smallest= None
def max(swal):
    largest= None
smallest= None
largest= None
while True :
    swal= input("Enter a number: ")
    if swal== 'done' :
        break
    try :
        fswal = float(swal)
    except :
        print('Invalid input')
        continue
for swal in swal :
    if smallest is None or swal<smallest:
        smallest = swal
#if largest is None or swal>largest:
#largest= swal
#return smallest
#return largest

print (largest, smallest)
