import  json 
import argparse


parser = argparse.ArgumentParser(description='prossess input file')
parser.add_argument("-n", "--name", help="playername")
parser.add_argument("-c", "--clas", help="playerclass")
parser.add_argument("-e", "--ep", help="playerEP")
parser.add_argument("-g", "--gp", help="playerGP")
args = parser.parse_args()

unpregnant = {args.name:{"name":args.name, "class":args.clas, "ep":args.ep, "gp":args.gp}}

with open('epgp.json', 'a') as f:
    pregnant = json.dumps(unpregnant)
    f.write(pregnant)

