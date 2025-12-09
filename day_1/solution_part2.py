def solve():
    with open("input.txt", "r") as f:
        instructions = [line.strip() for line in f if line.strip()]
    
    dial_size = 100
    position = 50
    times_at_zero = 0
    
    for instruction in instructions:
        direction = instruction[0]
        amount = int(instruction[1:])
        
        if direction == 'L':
            new_position = (position - amount) % dial_size
            
            if position > 0 and amount >= position:
                times_at_zero += (amount - position) // dial_size + 1
            elif position == 0 and amount >= dial_size:
                times_at_zero += amount // dial_size
        else:
            new_position = (position + amount) % dial_size
            
            if position > 0:
                first_zero = dial_size - position
                if amount >= first_zero:
                    times_at_zero += (amount - first_zero) // dial_size + 1
            else:
                if amount >= dial_size:
                    times_at_zero += amount // dial_size
        
        position = new_position
    
    print(f"Password (times dial points at 0): {times_at_zero}")
    
    return times_at_zero

if __name__ == "__main__":
    solve()
