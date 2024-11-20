#region debai
"""
--- ma debai / id
hi(name)

--- nopbai
00 fork tu bainopmau tren replit tu trang web duoiday 
   https://replit.com/@NamG1/toya03hi

01 lam bai vao tep s00_bailam.py, chay Run de co ketqua tatca la 1
02a tao github repo, mo kiemtra tep s00_bailam.py, va lay diachi/url aka githubbailamourl

02b dan diachi githubbailamourl tu trang web duoiday
    https://forms.gle/s46X7pPDY7p79NQr5

--- debai / problem
Khi chay voi input           | Ketqua output
---------------------------- | -----------------
hi(name='Mom')               | Hi Mom!
hi('Mom')                    | Hi Mom!
hi('')                       | Hi!
hi()                         | Hi!
hi(None)                     | Hi!

------------------- mucdo: kho -----------------
hi('Mom', 'Dad')             | Hi Mom, and Dad!
hi('A', 'B', 'C')            | Hi A, B, and C!
hi('1', '22', '333', '4444') | Hi 1, 22, 333, and 4444!
"""
#endregion debai

#region bailam
def hi(*args, name=None):
    if name:
        return f"Hi {name}!"
    # Remove any empty or None values from args
    args = [arg for arg in args if arg]
    # If no valid names are provided, return "Hi!"
    if not args:
        return "Hi!"
    if len(args) == 1:
        return f"Hi {args[0]}!"
    # If two names are provided, return greeting with "and"
    if len(args) == 2:
        return f"Hi {args[0]} and {args[1]}!"
    return f"Hi {', '.join(args[:-1])}, and {args[-1]}!"
#endregion bailam
