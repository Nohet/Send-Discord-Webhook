from dhooks import Webhook, Embed

gethook = input("Type ur webhook url: ")

hook = Webhook(gethook)

getmethod = input("Normal message or embed? (message/embed): ")

if getmethod == ("message"):
    getmessage = input("Enter the text of the message: ")
    hook.send(getmessage)
    print(f"Message successfully sent! ({getmessage})")

elif getmethod == ("embed"):
    getauthor = input("Set author: ")
    getfield1 = input("Set name of field: ")
    getfield2 = input("Set value of field: ")
    getfooter = input("Set footer: ")
    embed = Embed(
        color=0x5CDBF0,
        timestamp='now'  # sets the timestamp to current time
    )

    embed.set_author(name=getauthor)
    embed.add_field(name=getfield1, value=getfield2)
    embed.set_footer(text=getfooter)
    hook.send(embed=embed)
