def generate_ticket(airline,source,destination,no_of_passengers):
    ticket_number_list=[]
    #Write your logic here
    if no_of_passengers<5:
        n1=1
        a=101
    else:
        n1=no_of_passengers-5+1
        a=100+n1
    for i in range(n1,no_of_passengers+1):        
        string2=airline+":"+source[:3]+":"+destination[:3]+":"+str(a)
        a+=1
        ticket_number_list.append(string2)
    #Use the below return statement wherever applicable
    return ticket_number_list

#Provide different values for airline,source,destination,no_of_passengers and test your program
print(generate_ticket("AI","Bangalore","London",7))
