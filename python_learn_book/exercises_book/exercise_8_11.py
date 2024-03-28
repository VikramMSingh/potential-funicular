def sending_messages(usm, sm):
    while usm:
        a=usm.pop()
        print(f"Sending {a}")
        sm.append(a)
    print(f"Original list: {usm}")
    print(f"Sent list : {sm}")
    #print(f"Copied list : {usm[:]}")

unsent_messages = ["Hello", "How are you?", "May I offer you something"]
sent_messages = []

sending_messages(unsent_messages[:], sent_messages)

print(unsent_messages)
