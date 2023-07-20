class LeaderBoard:
  def __init__(self):
    self.highest_scores = []
    
  def update(self, value):
    if len(self.highest_scores) < 3:
      self.highest_scores.append(value)
      self.highest_scores.sort(reverse=True)
    else:
      if value > self.highest_scores[-1]:
        self.highest_scores[-1] = value
        self.highest_scores.sort(reverse=True)
    
  def get_highest_score(self):
    return self.highest_scores[0]
