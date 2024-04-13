from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
Puzz0 = And(AKnight, AKnave)
knowledge0 = And(
    Not(Biconditional(AKnight ,AKnave)), # Not Both at the same time (XOR)
    Or(Biconditional(AKnight, Puzz0),
       Biconditional(AKnave, Not(Puzz0)))

)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
Puzz1 = And(AKnave, BKnave)
knowledge1 = And(
    # Not Knight and Knave at the same time
    Not(Biconditional(AKnight, AKnave)),
    Not(Biconditional(BKnight, BKnave)),
    Or(Biconditional(AKnight, Puzz1)), #If Puzz1 is true implies A is a Knight
    Biconditional(AKnave, Not(Puzz1))

)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
PuzzA2 = Or(And(AKnight, BKnight), And(AKnave, BKnave))
PuzzB2 = Or(And(AKnight, BKnave), And(AKnave, BKnight))
knowledge2 = And(
    Not(Biconditional(AKnave, AKnight)), #A cannot be Knave and Knight at the same time
    Not(Biconditional(BKnave, BKnight)),
    Or(Biconditional(AKnight, PuzzA2),
       Biconditional(AKnave, Not(PuzzA2))), # If is Knight PuzzA2 is True
    Or(Biconditional(BKnight, PuzzB2),
       Biconditional(BKnave, Not(PuzzB2)))

)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
PuzzA3 = Or(AKnight, AKnave)
PuzzB3 = Or(Biconditional(AKnight, AKnave),
             Biconditional(AKnave, Not(AKnave)))
PuzzB4 = CKnight
PuzzC1 = AKnight
knowledge3 = And(
    # Everyone cannot be both at the same time
    Not(Biconditional(AKnight,AKnave)),
    Not(Biconditional(BKnight,BKnave)),
    Not(Biconditional(CKnight,CKnave)),
    Or(Biconditional(AKnight, PuzzA3),
       Biconditional(AKnave, Not(PuzzA3))),
    Or(Biconditional(BKnight, PuzzB3),
       Biconditional(BKnave, Not(PuzzB3))),
    Or(Biconditional(BKnight, PuzzB4),
       Biconditional(BKnave, Not(PuzzB4))),
    Or(Biconditional(CKnight, PuzzC1),
       Biconditional(CKnave, Not(PuzzC1)))
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
