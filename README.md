#  Blockchain Consensus Mechanism Simulation

This is a fun and simple simulation that compares how three popular blockchain consensus mechanisms work:

- **PoW (Proof of Work)**
- **PoS (Proof of Stake)**
- **DPoS (Delegated Proof of Stake)**

It uses mock data to demonstrate how validators are selected based on power, stake, or votes.

---

## Objective

> Understand how different blockchains choose who gets to validate a block — and why each method matters.

---

##  How It Works

We simulate each mechanism with fake data:

### Proof of Work (PoW)

- Each miner has a random **power** level.
- The one with the **highest power** wins.
- Simulates mining power competition (like Bitcoin).

### Proof of Stake (PoS)

- Each validator has a random **stake** (number of tokens).
- The one with the **highest stake** is selected.
- Simulates networks like Ethereum 2.0 or Cardano.

### Delegated PoS (DPoS)

- Voters cast votes for trusted delegates.
- The **most voted delegate** wins.
- Simulates systems like EOS and TRON.

---

##  Output Example

```bash
 Consensus Mechanism Simulation

===  Proof of Work (PoW) ===
Miner Powers: {'MinerA': 84, 'MinerB': 63, 'MinerC': 40}
Selected Miner: MinerA
Reason: MinerA has the highest power → 84

=== Proof of Stake (PoS) ===
Staker Stakes: {'StakerX': 730, 'StakerY': 410, 'StakerZ': 630}
Selected Staker: StakerX
Reason: StakerX has the most stake → 730

===  Delegated PoS (DPoS) ===
Votes from Voters: {'Voter1': 'Delegate2', 'Voter2': 'Delegate3', 'Voter3': 'Delegate2'}
Vote Count: {'Delegate2': 2, 'Delegate3': 1}
Selected Delegate: Delegate2
Reason: Delegate2 got the most votes → 2
