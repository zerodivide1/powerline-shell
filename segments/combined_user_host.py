def add_combined_user_host_segment(powerline):
    import os
    if powerline.args.shell == 'bash':
        user_prompt = ' \\u@\\h '
    elif powerline.args.shell == 'zsh':
        user_prompt = ' %n@%m '
    else:
        import socket
        user_prompt = ' %s@%s ' % (os.getenv('USER'),socket.gethostname().split('.')[0])

    if os.getenv('USER') == 'root':
        bgcolor = Color.USERNAME_ROOT_BG
    else:
        bgcolor = Color.USERNAME_BG

    powerline.append(user_prompt, Color.USERNAME_FG, bgcolor)
