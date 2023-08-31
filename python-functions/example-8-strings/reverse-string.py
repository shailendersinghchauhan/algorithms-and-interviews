def reverse_string(name: str) -> str:
    """
    f'{s} {t}'               # 78.2 ns
    s + '  ' + t             # 104 ns
    ' '.join((s, t))         # 135 ns
    '%s %s' % (s, t)         # 188 ns
    '{} {}'.format(s, t)     # 283 ns
    Template('$s $t').substitute(s=s, t=t)  # 898 ns
    """
    new_name = []
    print("String:{0}".format(name))
    for i in range(len(name) - 1, -1, -1):
        print(i)
        new_name.append(name[i])
    revstring = "".join(new_name)
    print(f'New reveresed name is:{revstring}')

if __name__ == '__main__':
    reverse_string("shail")