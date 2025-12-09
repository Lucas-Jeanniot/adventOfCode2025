def solve():
    with open("input.txt", "r") as f:
        instructions = [line.strip() for line in f if line.strip()]
    
    dial_size = 100
    position = 50
    times_at_zero = 0
    times_passed_zero = 0
    
    for instruction in instructions:
        direction = instruction[0]
        amount = int(instruction[1:])
        
        if direction == 'L':
            new_position = (position - amount) % dial_size
            
            if amount > position:
                times_passed_zero += (amount - position - 1) // dial_size + 1
        else:
            new_position = (position + amount) % dial_size
            
            if position + amount >= dial_size:
                times_passed_zero += (position + amount) // dial_size
        
        position = new_position
        
        if position == 0:
            times_at_zero += 1
    
    print(f"Times passed through 0: {times_passed_zero}")
    print(f"Password (times dial left pointing at 0): {times_at_zero}")
    
    return times_at_zero

if __name__ == "__main__":
    solve()
