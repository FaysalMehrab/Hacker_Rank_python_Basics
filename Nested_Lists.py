from collections import defaultdict

if __name__ == '__main__':
    scores = defaultdict(list)
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        scores[score].append(name) 
        
    l_s = list(sorted(scores.keys()))[1] # sored so at index 1 we have the second lowest score
  
    for name in sorted(scores[l_s]):
        print(name)