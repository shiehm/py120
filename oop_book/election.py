"""
Requirements
- A candidate class that tracks how many votes they got, through self...
- An election class that displays results of the vote 

Note: In general, you shouldn't customize + and += when you need to create an 
unwanted new object. Use something like an add_vote method instead.

The key difference between += (__iadd__) and + (__add__) is that:

+= modifies the existing object (in-place)
+ must create and return a new object

So if we implemented __add__, this would happen:

candidate = Candidate("Jane")  # Original object assigned to 'candidate'
result = candidate + 5        # Creates new Candidate object assigned to 'result'
# Now we have two objects: 'candidate' and 'result'

This could lead to problems because:

Multiple objects represent the same candidate
Each object has its own separate vote count
Vote totals could become inconsistent

That's why __iadd__ is better here - it modifies the single, original object.
"""

class Election:
    
    def __init__(self, candidates):
        self.candidates = candidates
    
    def results(self):
        votes = [candidate.votes for candidate in candidates]
        total_votes = sum(votes)
        max_vote = max(votes)
        winner = [candidate.name for candidate in candidates if candidate.votes == max_vote][0]
        
        for candidate in self.candidates:
            print(f'{candidate.name}: {candidate.votes} votes')
        print()
        print(f'{winner} won: {max_vote/total_votes:.1%} of votes')

class Candidate:
    
    def __init__(self, name):
        self.name = name
        self.votes = 0
    
    # This was the tricky part, understanding that += implies itself, and you have to tell which instance variable to change, and also to return self 
    def __iadd__(self, num):
        if not isinstance(num, int):
            return NotImplemented
        self.votes += num
        return self

mike_jones = Candidate('Mike Jones')
susan_dore = Candidate('Susan Dore')
kim_waters = Candidate('Kim Waters')

candidates = {
    mike_jones,
    susan_dore,
    kim_waters,
}

votes = [
    mike_jones,
    susan_dore,
    mike_jones,
    susan_dore,
    susan_dore,
    kim_waters,
    susan_dore,
    mike_jones,
]

for candidate in votes:
    candidate += 1

election = Election(candidates)
election.results()

"""
Output:
Mike Jones: 3 votes
Susan Dore: 4 votes
Kim Waters: 1 votes

Susan Dore won: 50.0% of votes
"""