def dump_statistics(msg_per_user):
    total_msgs = 0
    print('Message Summary:')
    print('-----------------------')
    for user in msg_per_user.keys():
        total_msgs += msg_per_user[user]
        print(f"{user}: {msg_per_user[user]}")
    print('-----------------------')
    print(f"Total mesages: {total_msgs}")
    print(f'Biggest message is from {author} made on {date}: {len(largest_msg)}')

def list_messages(group_message_repository):
    msg_per_user = {}
    largest_msg = ''
    author = ''
    date = ''
    for message in group_message_repository.get_messages():
        if len(largest_msg) < len(message.content):
            largest_msg = message.content
            author = message.member.name
            date = message.date

        if message.member.name not in msg_per_user.keys():
            msg_per_user[message.member.name] = 1
            continue

        msg_per_user[message.member.name] += 1
        i =+ 1
        
    dump_statistics(msg_per_user)
