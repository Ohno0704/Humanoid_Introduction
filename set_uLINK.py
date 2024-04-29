# リンク構造の初期化と表示関数
class Link:
    def __init__(self, name, sister, child, m):
        self.name = name
        self.sister = sister
        self.child = child
        self.m = m

def print_links_info(links):
    print("[[[[[ uLINK struct was set as following ]]]]]")
    print("-------------------------------------")
    print("ID     name    sister child   mass")
    print("-------------------------------------")
    for n, link in enumerate(links):
        print(f"{n+1}  {link.name:8s}     {link.sister:2d}    {link.child:2d}    {link.m:7.2f}")
    print()

def pause_and_execute(command, description):
    print(description)
    exec(command)
    input("Press Enter to continue...")

def print_link_name(link_id):
    if link_id == 0:
        return
    print(uLINK[link_id - 1].name)
    print_link_name(uLINK[link_id - 1].child)
    print_link_name(uLINK[link_id - 1].sister)

def total_mass(link_id):
    if link_id == 0:
        return 0
    return uLINK[link_id - 1].m + total_mass(uLINK[link_id - 1].child) + total_mass(uLINK[link_id - 1].sister)