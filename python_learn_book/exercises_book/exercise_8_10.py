unsent_message = ["Hello", "How are you?", "We have an offer for you!"]
sent_message=[]

def sending_message(usm, sm):
    while usm:
        a=usm.pop()
        print(f"Sending {a}")
        sm.append(a)
    print(usm)
    print(sm)

sending_message(unsent_message, sent_message)        
