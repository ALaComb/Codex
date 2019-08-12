import random
import re
from discord.ext import commands


class citizen(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Event Sample
    @commands.Cog.listener()
    async def on_ready(self):
        print('Citizen has entered the inn.')

    @commands.command()
    async def test(self, ctx):
        await ctx.send('Oh yeah!')

    # Roll command.
    @commands.command(aliases=['r'])
    async def roll(self, ctx, *, dice="1d20"):
        """
        Use this to roll dice or do math.

        The roll command supports NdX rolls and PEMDAS operations.

        Dice
        N   = number of dice
        X   = die size
        khY = keep highest Y number of dice. Ex: 2d20kh1
        klY = keep lowest Y number of dice. Ex: 2d20kl1

        PEMDAS
         + = addition
         - = subtraction
         * = multiplication
         / = division
         ^ = exponential
        () = parenthesis supported
        """
        dice = dice.replace(" ", "")
        roll_return = roll_calc(dice)
        if "Error:" in roll_return:
            await ctx.send(roll_return)
        else:
            await ctx.send("""``` /\\' .\\    _____
/: \\___\\  / .  /\\
\\' / . / /____/..\\
 \\/___/  \\'  '\\  /
          \\'__'\\/```""" +
                           f'\nRolling **{dice.lower()}**... ' +
                           f'Rolled **{roll_return}**!')


def setup(client):
    client.add_cog(citizen(client))


def roll_calc(roll_command):
    dice = roll_command.upper().strip()
    new_dice = ""
    curr_unit = ""
    for i in dice:
        if i not in r"0123456789+-*/%^().dkhl":
            return (f"Error: Invalid character in roll command. Valid " +
                    "characters are `0123456789+-*/%^().dkhl`\nInvalid " +
                    "character: {i}")
        if i in ['(', ')', '*', '/', '%', '+', '-']:
            if curr_unit != "":
                new_dice = new_dice + str(dice_eval(curr_unit))
                curr_unit = ""
            new_dice += i
        elif i == '^':
            new_dice += '**'
        else:
            curr_unit += i
    new_dice = new_dice + str(dice_eval(curr_unit))
    return eval_expr(new_dice)


def dice_eval(unit):
    die_eval = {}
    rolls = []
    if "D" in unit:
        working = unit.split('D')
        if working[0].isdigit() and len(working) == 2:
            die_eval["N"] = int(working[0])
            if "K" in working[1]:
                if "H" in working[1]:
                    working[1] = working[1].split("KH")
                    die_eval["X"] = int(working[1][0])
                    die_eval["KH"] = int(working[1][1])
                    for i in range(die_eval["N"]):
                        rolls.append(random.randrange(1, die_eval["X"]))
                    rolls.sort(reverse=True)
                    return sum(rolls[:die_eval["KH"]])
                elif "L" in working[1]:
                    working[1] = working[1].split("KL")
                    die_eval["X"] = int(working[1][0])
                    die_eval["KL"] = int(working[1][1])
                    for i in range(die_eval["N"]):
                        rolls.append(random.randrange(1, die_eval["X"]))
                    rolls.sort()
                    return sum(rolls[:die_eval["KL"]])
            else:
                die_eval["X"] = int(working[1])
                for i in range(die_eval["N"]):
                    rolls.append(random.randrange(1, die_eval["X"]))
                return sum(rolls)
    elif unit.isdigit():
        return int(unit)
    return ""


def eval_expr(expr):
    paren_pattern = re.compile(r"\(.+?\)")
    while paren_pattern.findall(expr) != []:
        paren_expr = paren_pattern.findall(expr)[0]
        expr = expr.replace(paren_expr,
                            eval_expr(paren_expr[1:len(paren_expr)-1]), 1)
    exp_pattern = re.compile(r"(\d+)(\*\*)(\d+)")
    while exp_pattern.findall(expr) != []:
        exp_expr = ''.join(exp_pattern.findall(expr)[-1])
        expr = rreplace(expr, exp_expr, str(eval(exp_expr)), 1)
    mult_pattern = re.compile(r"(\d+)(\.?\d*)(\*|/|%)(\d+)(\.?\d*)")
    while mult_pattern.findall(expr) != []:
        mult_expr = ''.join(mult_pattern.findall(expr)[0])
        expr = expr.replace(mult_expr, str(eval(mult_expr)), 1)
    add_pattern = re.compile(r"(\d+)(\.?\d*)(\+|-)(\d+)(\.?\d*)")
    while add_pattern.findall(expr) != []:
        add_expr = ''.join(add_pattern.findall(expr)[0])
        expr = expr.replace(add_expr, str(eval(add_expr)), 1)
    return expr


def rreplace(s, old, new, occurrence):
    li = s.rsplit(old, occurrence)
    return new.join(li)
