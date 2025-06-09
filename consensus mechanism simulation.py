import random

pow_miners = {
    "MinerA": random.randint(1, 100),
    "MinerB": random.randint(1, 100),
    "MinerC": random.randint(1, 100)
}

pos_stakers = {
    "StakerX": random.randint(100, 1000),
    "StakerY": random.randint(100, 1000),
    "StakerZ": random.randint(100, 1000)
}

delegates = ["Delegate1", "Delegate2", "Delegate3"]
voters = {
    "Voter1": random.choice(delegates),
    "Voter2": random.choice(delegates),
    "Voter3": random.choice(delegates)
}

pow_winner = max(pow_miners, key=pow_miners.get)

pos_winner = max(pos_stakers, key=pos_stakers.get)

vote_counts = {}
for vote in voters.values():
    vote_counts[vote] = vote_counts.get(vote, 0) + 1
dpos_winner = max(vote_counts, key=vote_counts.get)


print("\nConsensus Mechanism Simulation\n")

print(" Proof of Work (PoW)")
print("Miner Powers:", pow_miners)
print(f"Selected Miner: {pow_winner}")
print(f"Reason: {pow_winner} has the highest power {pow_miners[pow_winner]}")
print("Logic: More power = higher chance to solve the puzzle first.\n")

print("Proof of Stake (PoS)")
print("Staker Stakes:", pos_stakers)
print(f"Selected Staker: {pos_winner}")
print(f"Reason: {pos_winner} has the most stake {pos_stakers[pos_winner]}")
print("Logic: More tokens = more trust & responsibility.\n")

print("Delegated PoS (DPoS)")
print("Votes from Voters:", voters)
print("Vote Count:", vote_counts)
print(f"Selected Delegate: {dpos_winner}")
print(f"Reason: {dpos_winner} got the most votes {vote_counts[dpos_winner]}")
print("Logic: Voters elect trusted delegates to validate on their behalf.\n")

