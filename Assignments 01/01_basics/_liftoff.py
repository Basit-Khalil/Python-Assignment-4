def spaceship_countdown() -> None:
    """Prints a countdown from 10 to 1 followed by 'Liftoff!'."""
    for i in range(10, 0, -1):  # 10 se 1 tak countdown karega
        print(i, end=" ")  # Ek hi line mai output ke liye 'end=" "'
    print("Liftoff!")  # Aakhir mai Liftoff! print hoga

# Run the function
if __name__ == "__main__":
    spaceship_countdown()
