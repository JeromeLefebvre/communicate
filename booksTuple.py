from collections import namedtuple

Book = namedtuple("book", ["title", "price", "isbn"], verbose=False)

Book(title='Reflection Groups and Coxeter Groups (Cambridge Studies in Advanced Mathematics)', price='$59.95', isbn='9780521375108')
Book(title='Instantons and Four-Manifolds (Undergraduate Texts in Mathematics)', price='$18.50', isbn='0387960368')
Book(title="Thomas' Calculus Early Transcendentals (11th Edition)", price='$160.00', isbn='9780321198006')