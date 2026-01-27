if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    q_mark = student_marks[query_name]
    avg = sum(q_mark) / len(q_mark)
    
    print(f'{avg:.2f}')